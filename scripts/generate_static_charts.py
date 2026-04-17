from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from shared.data_loader import ensure_generated_dir  # noqa: E402
from tools import bokeh_demo, matplotlib_demo, plotly_demo  # noqa: E402


def main() -> None:
    output_dir = ensure_generated_dir()
    generators = [
        ("Matplotlib", matplotlib_demo.create_all_charts),
        ("Plotly", plotly_demo.create_all_charts),
        ("Bokeh", bokeh_demo.create_all_charts),
    ]

    print(f"Writing outputs to: {output_dir}")
    for label, generator in generators:
        print(f"\nGenerating {label} charts...")
        outputs = generator(output_dir)
        for path in outputs:
            print(f"- {path}")


if __name__ == "__main__":
    main()
