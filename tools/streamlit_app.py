from __future__ import annotations

import sys
from pathlib import Path

import plotly.express as px
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from shared.data_loader import (  # noqa: E402
    brand_count,
    category_distribution,
    event_type_distribution,
    events_over_time,
    load_events,
    summary_metrics,
)


st.set_page_config(page_title="Visualization Tools Demo", layout="wide")


@st.cache_data
def get_data():
    return load_events()


def metric_cards(df) -> None:
    metrics = summary_metrics(df)
    columns = st.columns(5)
    labels = {
        "rows": "Rows",
        "unique_users": "Users",
        "unique_products": "Products",
        "avg_price": "Avg price",
        "max_price": "Max price",
    }
    for column, key in zip(columns, labels):
        column.metric(labels[key], metrics[key])


def main() -> None:
    df = get_data()
    st.title("Ecommerce Visualization Demo")
    st.caption("Same dataset, multiple chart patterns, dashboard-ready Streamlit app.")

    event_options = sorted(df["event_type"].unique().tolist())
    selected_events = st.sidebar.multiselect(
        "Filter event type",
        options=event_options,
        default=event_options,
    )
    filtered = df[df["event_type"].isin(selected_events)].copy()

    metric_cards(filtered)
    st.dataframe(filtered, use_container_width=True)

    tab1, tab2, tab3 = st.tabs(["Distribution", "Time", "Category"])

    with tab1:
        left, right = st.columns(2)
        left.plotly_chart(
            px.bar(
                event_type_distribution(filtered),
                x="event_type",
                y="count",
                title="Event Type Distribution",
                text="count",
            ),
            use_container_width=True,
        )
        right.plotly_chart(
            px.histogram(filtered, x="price", nbins=5, title="Price Distribution"),
            use_container_width=True,
        )

    with tab2:
        left, right = st.columns(2)
        left.plotly_chart(
            px.bar(
                brand_count(filtered),
                x="brand",
                y="count",
                title="Brand Count",
                text="count",
            ),
            use_container_width=True,
        )
        right.plotly_chart(
            px.line(
                events_over_time(filtered),
                x="event_second",
                y="event_count",
                title="Events Over Time",
                markers=True,
            ),
            use_container_width=True,
        )

    with tab3:
        st.plotly_chart(
            px.bar(
                category_distribution(filtered),
                x="count",
                y="category",
                orientation="h",
                title="Category Distribution",
                text="count",
            ),
            use_container_width=True,
        )


if __name__ == "__main__":
    main()
