from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

import plotly.express as px
import plotly.io as pio
from plotly.graph_objects import Figure

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from shared.data_loader import (  # noqa: E402
    brand_count,
    category_distribution,
    ensure_generated_dir,
    event_type_distribution,
    events_over_time,
    load_events,
)


TOOL_NAME = "plotly"
TMP_DIR = PROJECT_ROOT / "tmp"


def _configure_temp_dir() -> None:
    """Keep Kaleido temp files inside the workspace (sandbox-friendly)."""
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    os.environ["TMP"] = str(TMP_DIR)
    os.environ["TEMP"] = str(TMP_DIR)
    tempfile.tempdir = str(TMP_DIR)


def create_figures() -> dict[str, Figure]:
    df = load_events()
    return {
        "event_type_distribution": px.bar(
            event_type_distribution(df),
            x="event_type",
            y="count",
            title="Event Type Distribution",
            text="count",
        ),
        "price_distribution": px.histogram(
            df,
            x="price",
            nbins=5,
            title="Price Distribution",
        ),
        "brand_count": px.bar(
            brand_count(df),
            x="brand",
            y="count",
            title="Brand Count",
            text="count",
        ),
        "events_over_time": px.line(
            events_over_time(df),
            x="event_second",
            y="event_count",
            title="Events Over Time",
            markers=True,
        ),
        "category_distribution": px.bar(
            category_distribution(df),
            x="count",
            y="category",
            orientation="h",
            title="Category Distribution",
            text="count",
        ),
    }


def save_png_if_available(fig: Figure, path: Path) -> Path | None:
    try:
        fig.write_image(path, scale=2)
    except Exception as exc:  # Kaleido is optional for local static export.
        print(f"Skip PNG export for {path.name}: {exc}")
        return None
    return path


def create_all_charts(output_dir: str | Path | None = None) -> list[Path]:
    _configure_temp_dir()
    output_dir = ensure_generated_dir(output_dir) if output_dir else ensure_generated_dir()
    outputs: list[Path] = []

    for name, fig in create_figures().items():
        fig.update_layout(template="plotly_white")
        html_path = output_dir / f"{TOOL_NAME}_{name}.html"
        pio.write_html(fig, file=html_path, auto_open=False, include_plotlyjs="cdn")
        outputs.append(html_path)

        png_path = output_dir / f"{TOOL_NAME}_{name}.png"
        exported_png = save_png_if_available(fig, png_path)
        if exported_png:
            outputs.append(exported_png)

    return outputs


def main() -> None:
    outputs = create_all_charts()
    print("Generated Plotly files:")
    for path in outputs:
        print(f"- {path}")


if __name__ == "__main__":
    main()
