from __future__ import annotations

import os
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CLEAN_PATH = PROJECT_ROOT / "data" / "ecommerce_events_clean.csv"
DEFAULT_SAMPLE_PATH = PROJECT_ROOT / "data" / "ecommerce_events_sample.csv"
DATA_PATH = Path(
    os.environ.get(
        "EVENTS_DATA_PATH",
        str(DEFAULT_CLEAN_PATH if DEFAULT_CLEAN_PATH.exists() else DEFAULT_SAMPLE_PATH),
    )
)
GENERATED_DIR = PROJECT_ROOT / "screenshots" / "generated"

REQUIRED_COLUMNS = {
    "event_time",
    "event_type",
    "product_id",
    "category_id",
    "category_code",
    "brand",
    "price",
    "user_id",
    "user_session",
}


def load_events(path: str | Path = DATA_PATH) -> pd.DataFrame:
    """Load and lightly clean the shared ecommerce event dataset."""
    path = Path(path)
    df = pd.read_csv(path)

    missing = REQUIRED_COLUMNS.difference(df.columns)
    if missing:
        missing_text = ", ".join(sorted(missing))
        raise ValueError(f"Dataset is missing required columns: {missing_text}")

    df["event_time"] = pd.to_datetime(df["event_time"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["brand"] = df["brand"].fillna("unknown").replace("", "unknown")
    df["category_code"] = df["category_code"].fillna("unknown").replace("", "unknown")
    df["event_type"] = df["event_type"].fillna("unknown").replace("", "unknown")

    df = df.dropna(subset=["event_time", "price"]).copy()
    df["category_root"] = df["category_code"].str.split(".").str[0].fillna("unknown")
    df["event_date"] = df["event_time"].dt.date
    df["event_second"] = df["event_time"].dt.floor("s")
    df["price_log"] = df["price"].round(2)
    return df.sort_values("event_time").reset_index(drop=True)


def event_type_distribution(df: pd.DataFrame) -> pd.DataFrame:
    return _count_table(df, "event_type", "event_type")


def brand_count(df: pd.DataFrame) -> pd.DataFrame:
    return _count_table(df, "brand", "brand")


def category_distribution(df: pd.DataFrame) -> pd.DataFrame:
    return _count_table(df, "category_root", "category")


def events_over_time(df: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        df.groupby("event_second")
        .size()
        .reset_index(name="event_count")
        .sort_values("event_second")
    )
    return grouped


def summary_metrics(df: pd.DataFrame) -> dict[str, float | int]:
    return {
        "rows": int(len(df)),
        "unique_users": int(df["user_id"].nunique()),
        "unique_products": int(df["product_id"].nunique()),
        "avg_price": round(float(df["price"].mean()), 2),
        "max_price": round(float(df["price"].max()), 2),
    }


def ensure_generated_dir(path: str | Path = GENERATED_DIR) -> Path:
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def _count_table(df: pd.DataFrame, column: str, label_name: str) -> pd.DataFrame:
    return (
        df[column]
        .value_counts(dropna=False)
        .rename_axis(label_name)
        .reset_index(name="count")
        .sort_values(["count", label_name], ascending=[False, True])
        .reset_index(drop=True)
    )
