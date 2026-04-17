# Mermaid Examples

Mermaid is included here as a documentation and architecture visualization tool. It can draw simple pie charts from prepared counts, but it is not a full data visualization library like Matplotlib, Plotly, Bokeh, Dash, or Streamlit.

## Data Processing Flow

```mermaid
flowchart LR
    A[CSV dataset] --> B[shared.data_loader.load_events]
    B --> C[Clean event_time, price, brand, category]
    C --> D[Reusable summary tables]
    D --> E[Matplotlib static PNG]
    D --> F[Plotly HTML and optional PNG]
    D --> G[Bokeh HTML]
    D --> H[Streamlit dashboard]
    D --> I[Dash dashboard]
    D --> J[Markdown report]
```

## Event Type Distribution

```mermaid
pie showData
    title Event Type Distribution
    "view" : 4
    "cart" : 2
    "purchase" : 2
```

## Demo Architecture

```mermaid
flowchart TB
    subgraph Shared
        L[data_loader.py]
        C[ecommerce_events_sample.csv]
    end

    subgraph Static_outputs
        M[matplotlib_demo.py]
        P[plotly_demo.py]
        B[bokeh_demo.py]
    end

    subgraph Web_apps
        S[streamlit_app.py]
        D[dash_app.py]
    end

    C --> L
    L --> M
    L --> P
    L --> B
    L --> S
    L --> D
```
