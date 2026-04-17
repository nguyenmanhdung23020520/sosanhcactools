from __future__ import annotations

import argparse
import csv
import re
from datetime import datetime
from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = [
    "event_time",
    "event_type",
    "product_id",
    "category_id",
    "category_code",
    "brand",
    "price",
    "user_id",
    "user_session",
]

# Common Kaggle/export variants -> canonical column names
COLUMN_ALIASES = {
    "eventtime": "event_time",
    "time": "event_time",
    "timestamp": "event_time",
    "eventtype": "event_type",
    "type": "event_type",
    "productid": "product_id",
    "categoryid": "category_id",
    "categorycode": "category_code",
    "usersession": "user_session",
    "session": "user_session",
    "userid": "user_id",
}


EVENT_TIME_RE = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}(?: UTC)?$")
UUID_RE = re.compile(
    r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
)


def sniff_delimiter(path: Path) -> str:
    sample = path.read_bytes()[:4096]
    text = sample.decode("utf-8", errors="replace")
    try:
        dialect = csv.Sniffer().sniff(text, delimiters=[",", ";", "\t", "|"])
        return dialect.delimiter
    except Exception:
        # Safe default: Kaggle usually uses commas.
        return ","


def normalize_columns(columns: list[str]) -> list[str]:
    normalized: list[str] = []
    for col in columns:
        key = "".join(ch for ch in str(col).strip().lower() if ch.isalnum() or ch == "_")
        normalized.append(COLUMN_ALIASES.get(key, str(col).strip().lower()))
    return normalized


def looks_like_vertical_copy(path: Path) -> bool:
    lines = [line.strip() for line in path.read_text(encoding="utf-8", errors="replace").splitlines()]
    if len(lines) < 12:
        return False
    return "," in lines[0] and any(EVENT_TIME_RE.match(line) for line in lines[1:10])


def parse_vertical_copy(path: Path) -> pd.DataFrame:
    lines = [line.strip() for line in path.read_text(encoding="utf-8", errors="replace").splitlines()]
    header = [col.strip() for col in lines[0].split(",")]
    if normalize_columns(header) != REQUIRED_COLUMNS:
        raise ValueError("Vertical copy parser only supports the canonical ecommerce event header.")

    records: list[dict[str, object]] = []
    skipped = 0
    current: list[str] = []
    for value in [line for line in lines[1:] if line != ""]:
        if EVENT_TIME_RE.match(value) and current:
            try:
                records.append(record_from_vertical_values(current))
            except ValueError:
                skipped += 1
            current = [value]
        else:
            current.append(value)

    if current:
        try:
            records.append(record_from_vertical_values(current))
        except ValueError:
            skipped += 1

    if skipped:
        print(f"Skipped {skipped} incomplete record(s) from vertical copy input.")

    return pd.DataFrame(records, columns=REQUIRED_COLUMNS)


def record_from_vertical_values(values: list[str]) -> dict[str, object]:
    if len(values) < 7:
        raise ValueError(f"Cannot parse incomplete record: {values}")

    event_time, event_type, product_id, category_id = values[:4]
    tail = values[4:]

    session_index = next((i for i, value in enumerate(tail) if UUID_RE.match(value)), None)
    if session_index is None or session_index < 2:
        raise ValueError(f"Cannot find user_session in record: {values}")

    user_session = tail[session_index]
    user_id = tail[session_index - 1]
    price = tail[session_index - 2]
    optional = tail[: session_index - 2]

    category_code = "unknown"
    brand = "unknown"
    if len(optional) >= 2:
        category_code = optional[-2] or "unknown"
        brand = optional[-1] or "unknown"
    elif len(optional) == 1:
        value = optional[0] or "unknown"
        if "." in value or value in {"unknown", "electronics", "appliances", "computers"}:
            category_code = value
        else:
            brand = value

    return {
        "event_time": event_time.replace(" UTC", ""),
        "event_type": event_type,
        "product_id": product_id,
        "category_id": category_id,
        "category_code": category_code,
        "brand": brand,
        "price": price,
        "user_id": user_id,
        "user_session": user_session,
    }


def coerce_price(series: pd.Series) -> pd.Series:
    # Handle decimal comma (e.g. "1,234" or "489,07") and stray spaces.
    as_text = series.astype(str).str.strip()
    looks_like_decimal_comma = as_text.str.contains(",", regex=False) & ~as_text.str.contains(
        r"\.", regex=True
    )
    as_text = as_text.where(~looks_like_decimal_comma, as_text.str.replace(",", ".", regex=False))
    return pd.to_numeric(as_text, errors="coerce")


def normalize(input_path: Path) -> pd.DataFrame:
    if looks_like_vertical_copy(input_path):
        df = parse_vertical_copy(input_path)
    else:
        delimiter = sniff_delimiter(input_path)
        df = pd.read_csv(input_path, sep=delimiter, engine="python")

    df.columns = normalize_columns(list(df.columns))

    # Drop unnamed index columns if present.
    df = df.loc[:, [c for c in df.columns if not c.startswith("unnamed")]].copy()

    missing = sorted(set(REQUIRED_COLUMNS) - set(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    df = df[REQUIRED_COLUMNS].copy()

    df["event_time"] = pd.to_datetime(df["event_time"], errors="coerce", utc=False)
    df["price"] = coerce_price(df["price"])

    for col in ["event_type", "category_code", "brand", "user_session"]:
        df[col] = df[col].astype(str).str.strip()
        df[col] = df[col].replace({"": "unknown", "nan": "unknown"}).fillna("unknown")

    for col in ["product_id", "category_id", "user_id"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["event_time", "price", "product_id", "category_id", "user_id"]).copy()

    # Canonical formatting for event_time in CSV export
    df["event_time"] = df["event_time"].dt.strftime("%Y-%m-%d %H:%M:%S")

    # Ensure stable types
    df["product_id"] = df["product_id"].astype("int64")
    df["category_id"] = df["category_id"].astype("int64")
    df["user_id"] = df["user_id"].astype("int64")

    return df


def backup_path(path: Path) -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return path.with_name(f"{path.stem}.bak_{ts}{path.suffix}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize Kaggle ecommerce events CSV to project schema.")
    parser.add_argument(
        "--input",
        default=str(Path("data") / "ecommerce_events_sample.csv"),
        help="Input CSV path",
    )
    parser.add_argument(
        "--output",
        default=str(Path("data") / "ecommerce_events_clean.csv"),
        help="Output CSV path (ignored if --in-place)",
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite input file (creates .bak_YYYYmmdd_HHMMSS backup)",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise SystemExit(f"Input not found: {input_path}")

    df = normalize(input_path)

    if args.in_place:
        bak = backup_path(input_path)
        input_path.replace(bak)
        output_path = input_path
        df.to_csv(output_path, index=False, encoding="utf-8", lineterminator="\n")
        print(f"Wrote normalized CSV: {output_path}")
        print(f"Backup saved at:     {bak}")
    else:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False, encoding="utf-8", lineterminator="\n")
        print(f"Wrote normalized CSV: {output_path}")


if __name__ == "__main__":
    main()
