from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, save

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


TOOL_NAME = "bokeh"


def make_event_type_distribution(df):
    data = event_type_distribution(df)
    source = ColumnDataSource(data)
    plot = figure(
        x_range=data["event_type"].tolist(),
        title="Event Type Distribution",
        height=320,
        width=460,
        toolbar_location="above",
    )
    plot.vbar(x="event_type", top="count", width=0.65, source=source, color="#2f7ed8")
    plot.xaxis.axis_label = "Event type"
    plot.yaxis.axis_label = "Count"
    return plot


def make_price_distribution(df):
    hist, edges = np.histogram(df["price"], bins=5)
    plot = figure(
        title="Price Distribution",
        height=320,
        width=460,
        toolbar_location="above",
    )
    plot.quad(
        top=hist,
        bottom=0,
        left=edges[:-1],
        right=edges[1:],
        fill_color="#4caf50",
        line_color="white",
    )
    plot.xaxis.axis_label = "Price"
    plot.yaxis.axis_label = "Frequency"
    return plot


def make_brand_count(df):
    data = brand_count(df)
    source = ColumnDataSource(data)
    plot = figure(
        x_range=data["brand"].tolist(),
        title="Brand Count",
        height=320,
        width=460,
        toolbar_location="above",
    )
    plot.vbar(x="brand", top="count", width=0.65, source=source, color="#f28e2b")
    plot.xaxis.axis_label = "Brand"
    plot.yaxis.axis_label = "Count"
    plot.xaxis.major_label_orientation = 0.7
    return plot


def make_events_over_time(df):
    data = events_over_time(df)
    source = ColumnDataSource(data)
    plot = figure(
        x_axis_type="datetime",
        title="Events Over Time",
        height=320,
        width=460,
        toolbar_location="above",
    )
    plot.line("event_second", "event_count", source=source, line_width=2, color="#7b4ab8")
    plot.scatter("event_second", "event_count", source=source, size=8, color="#7b4ab8")
    plot.xaxis.axis_label = "Time"
    plot.yaxis.axis_label = "Events"
    return plot


def make_category_distribution(df):
    data = category_distribution(df)
    source = ColumnDataSource(data)
    plot = figure(
        y_range=list(reversed(data["category"].tolist())),
        title="Category Distribution",
        height=320,
        width=460,
        toolbar_location="above",
    )
    plot.hbar(y="category", right="count", height=0.55, source=source, color="#d84a4a")
    plot.xaxis.axis_label = "Count"
    plot.yaxis.axis_label = "Category"
    return plot


def create_dashboard(df):
    return gridplot(
        [
            [make_event_type_distribution(df), make_price_distribution(df)],
            [make_brand_count(df), make_events_over_time(df)],
            [make_category_distribution(df), None],
        ]
    )


def create_all_charts(output_dir: str | Path | None = None) -> list[Path]:
    df = load_events()
    output_dir = ensure_generated_dir(output_dir) if output_dir else ensure_generated_dir()
    output_path = output_dir / f"{TOOL_NAME}_dashboard.html"
    output_file(output_path, title="Ecommerce Visualization Demo - Bokeh")
    save(create_dashboard(df))
    return [output_path]


def main() -> None:
    outputs = create_all_charts()
    print("Generated Bokeh files:")
    for path in outputs:
        print(f"- {path}")


if __name__ == "__main__":
    main()
