from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt

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


TOOL_NAME = "matplotlib"


def plot_event_type_distribution(ax, df) -> None:
    data = event_type_distribution(df)
    ax.bar(data["event_type"], data["count"], color="#2f7ed8")
    ax.set_title("Event Type Distribution")
    ax.set_xlabel("Event type")
    ax.set_ylabel("Count")


def plot_price_distribution(ax, df) -> None:
    ax.hist(df["price"], bins=5, color="#4caf50", edgecolor="white")
    ax.set_title("Price Distribution")
    ax.set_xlabel("Price")
    ax.set_ylabel("Frequency")


def plot_brand_count(ax, df) -> None:
    data = brand_count(df)
    ax.bar(data["brand"], data["count"], color="#f28e2b")
    ax.set_title("Brand Count")
    ax.set_xlabel("Brand")
    ax.set_ylabel("Count")
    ax.tick_params(axis="x", rotation=35)


def plot_events_over_time(ax, df) -> None:
    data = events_over_time(df)
    ax.plot(data["event_second"], data["event_count"], marker="o", color="#7b4ab8")
    ax.set_title("Events Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Events")
    ax.tick_params(axis="x", rotation=35)


def plot_category_distribution(ax, df) -> None:
    data = category_distribution(df)
    ax.barh(data["category"], data["count"], color="#d84a4a")
    ax.set_title("Category Distribution")
    ax.set_xlabel("Count")
    ax.set_ylabel("Category")
    ax.invert_yaxis()


def save_individual_chart(df, output_dir: Path, filename: str, plotter) -> Path:
    fig, ax = plt.subplots(figsize=(8, 5))
    plotter(ax, df)
    fig.tight_layout()
    output_path = output_dir / filename
    fig.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close(fig)
    return output_path


def create_dashboard(df, output_dir: Path) -> Path:
    fig, axes = plt.subplots(3, 2, figsize=(14, 14))
    plot_event_type_distribution(axes[0, 0], df)
    plot_price_distribution(axes[0, 1], df)
    plot_brand_count(axes[1, 0], df)
    plot_events_over_time(axes[1, 1], df)
    plot_category_distribution(axes[2, 0], df)
    axes[2, 1].axis("off")
    axes[2, 1].text(
        0.05,
        0.75,
        "Matplotlib is best for\nstatic report-ready figures.",
        fontsize=14,
        va="top",
    )
    fig.suptitle("Ecommerce Visualization Demo - Matplotlib", fontsize=16)
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    output_path = output_dir / f"{TOOL_NAME}_dashboard.png"
    fig.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close(fig)
    return output_path


def create_all_charts(output_dir: str | Path | None = None) -> list[Path]:
    df = load_events()
    output_dir = ensure_generated_dir(output_dir) if output_dir else ensure_generated_dir()

    outputs = [
        save_individual_chart(
            df,
            output_dir,
            f"{TOOL_NAME}_event_type_distribution.png",
            plot_event_type_distribution,
        ),
        save_individual_chart(
            df,
            output_dir,
            f"{TOOL_NAME}_price_distribution.png",
            plot_price_distribution,
        ),
        save_individual_chart(df, output_dir, f"{TOOL_NAME}_brand_count.png", plot_brand_count),
        save_individual_chart(
            df,
            output_dir,
            f"{TOOL_NAME}_events_over_time.png",
            plot_events_over_time,
        ),
        save_individual_chart(
            df,
            output_dir,
            f"{TOOL_NAME}_category_distribution.png",
            plot_category_distribution,
        ),
        create_dashboard(df, output_dir),
    ]
    return outputs


def main() -> None:
    outputs = create_all_charts()
    print("Generated Matplotlib files:")
    for path in outputs:
        print(f"- {path}")


if __name__ == "__main__":
    main()
