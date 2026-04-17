from __future__ import annotations

import sys
from pathlib import Path

from dash import Dash, Input, Output, dcc, html
import plotly.express as px

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


df = load_events()


def build_app() -> Dash:
    app = Dash(__name__)
    app.title = "Visualization Tools Demo"

    event_options = [{"label": value, "value": value} for value in sorted(df["event_type"].unique())]
    metrics = summary_metrics(df)

    app.layout = html.Main(
        [
            html.H1("Ecommerce Visualization Demo"),
            html.P("Dash app using the shared ecommerce dataset."),
            html.Div(
                [
                    html.Div([html.Strong("Rows"), html.Span(metrics["rows"])]),
                    html.Div([html.Strong("Users"), html.Span(metrics["unique_users"])]),
                    html.Div([html.Strong("Products"), html.Span(metrics["unique_products"])]),
                    html.Div([html.Strong("Avg price"), html.Span(metrics["avg_price"])]),
                ],
                className="metrics",
            ),
            html.Label("Filter event type"),
            dcc.Dropdown(
                id="event-filter",
                options=event_options,
                value=[option["value"] for option in event_options],
                multi=True,
                clearable=False,
            ),
            html.Div(
                [
                    dcc.Graph(id="event-type-chart"),
                    dcc.Graph(id="price-chart"),
                    dcc.Graph(id="brand-chart"),
                    dcc.Graph(id="time-chart"),
                    dcc.Graph(id="category-chart"),
                ],
                className="chart-grid",
            ),
        ]
    )

    app.index_string = """
    <!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
            <style>
                body { margin: 0; font-family: Arial, sans-serif; background: #f7f8fa; color: #20242a; }
                main { max-width: 1180px; margin: 0 auto; padding: 28px 20px; }
                h1 { margin-bottom: 4px; }
                .metrics { display: grid; grid-template-columns: repeat(4, minmax(140px, 1fr)); gap: 12px; margin: 20px 0; }
                .metrics div { background: white; border: 1px solid #dde1e6; border-radius: 8px; padding: 14px; }
                .metrics strong { display: block; color: #4d5662; margin-bottom: 6px; }
                .chart-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; margin-top: 18px; }
                .chart-grid > div { background: white; border: 1px solid #dde1e6; border-radius: 8px; }
                @media (max-width: 800px) {
                    .metrics, .chart-grid { grid-template-columns: 1fr; }
                }
            </style>
        </head>
        <body>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
    """

    @app.callback(
        Output("event-type-chart", "figure"),
        Output("price-chart", "figure"),
        Output("brand-chart", "figure"),
        Output("time-chart", "figure"),
        Output("category-chart", "figure"),
        Input("event-filter", "value"),
    )
    def update_charts(selected_events):
        selected_events = selected_events or []
        filtered = df[df["event_type"].isin(selected_events)].copy()
        template = "plotly_white"
        return (
            px.bar(
                event_type_distribution(filtered),
                x="event_type",
                y="count",
                title="Event Type Distribution",
                text="count",
                template=template,
            ),
            px.histogram(filtered, x="price", nbins=5, title="Price Distribution", template=template),
            px.bar(
                brand_count(filtered),
                x="brand",
                y="count",
                title="Brand Count",
                text="count",
                template=template,
            ),
            px.line(
                events_over_time(filtered),
                x="event_second",
                y="event_count",
                title="Events Over Time",
                markers=True,
                template=template,
            ),
            px.bar(
                category_distribution(filtered),
                x="count",
                y="category",
                orientation="h",
                title="Category Distribution",
                text="count",
                template=template,
            ),
        )

    return app


app = build_app()


if __name__ == "__main__":
    app.run(debug=True, port=8050, use_reloader=False)
