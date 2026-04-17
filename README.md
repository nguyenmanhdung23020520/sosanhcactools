# Data Visualization Tools Mini Project

Mini project này giúp thực nghiệm và so sánh nhiều tool visualization trên cùng một dataset ecommerce nhỏ.

## 1. Cấu Trúc Project

```text
.
├── data/
│   └── ecommerce_events_sample.csv
├── shared/
│   ├── __init__.py
│   └── data_loader.py
├── tools/
│   ├── __init__.py
│   ├── matplotlib_demo.py
│   ├── plotly_demo.py
│   ├── streamlit_app.py
│   ├── dash_app.py
│   ├── bokeh_demo.py
│   └── mermaid_examples.md
├── scripts/
│   └── generate_static_charts.py
├── reports/
│   ├── tool_comparison_report.md
│   ├── comparison_matrix.csv
│   └── comparison_matrix.md
├── screenshots/
│   └── generated/
├── requirements.txt
└── README.md
```

## 2. Cài Đặt

Tạo virtual environment:

```bash
python -m venv .venv
```

Kích hoạt trên Windows PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

Cài thư viện:

```bash
pip install -r requirements.txt
```

Nếu muốn Plotly xuất thêm PNG, cài thêm Kaleido khi package index của bạn hỗ trợ:

```bash
python -m pip install kaleido
```

## 3. Dataset Và Module Chung

Dataset:

```text
data/ecommerce_events_clean.csv
```

Module xử lý dữ liệu:

```text
shared/data_loader.py
```

Các file demo đều dùng module này để tránh lặp code load/preprocess.

File `data/ecommerce_events_sample.csv` có thể giữ dữ liệu gốc bạn copy từ Kaggle. File clean dùng để chạy chart là `data/ecommerce_events_clean.csv`.

Bạn có thể trỏ toàn bộ demo sang file CSV khác bằng env var `EVENTS_DATA_PATH`, ví dụ:

```bash
set EVENTS_DATA_PATH=data/ecommerce_events_clean.csv
python scripts/generate_static_charts.py
```

## 4. Sinh Chart Tĩnh Và HTML Một Lần

Chạy script tổng hợp:

```bash
python scripts/generate_static_charts.py
```

Output được ghi vào:

```text
screenshots/generated/
```

Nếu bạn vừa copy dataset từ Kaggle và file CSV bị lệch delimiter/format, chuẩn hóa nhanh:

```bash
python scripts/normalize_dataset.py --input data/ecommerce_events_sample.csv --output data/ecommerce_events_clean.csv
```

Hoặc overwrite file gốc (có backup):

```bash
python scripts/normalize_dataset.py --input data/ecommerce_events_sample.csv --in-place
```

Script sẽ sinh:

- PNG từ Matplotlib.
- HTML từ Plotly.
- PNG từ Plotly nếu cài thêm Kaleido và môi trường local hỗ trợ static image export.
- HTML dashboard từ Bokeh.

## 5. Chạy Từng Tool

### Matplotlib

```bash
python tools/matplotlib_demo.py
```

Output:

```text
screenshots/generated/matplotlib_*.png
```

Phù hợp nhất cho ảnh tĩnh trong báo cáo.

### Plotly

```bash
python tools/plotly_demo.py
```

Output:

```text
screenshots/generated/plotly_*.html
screenshots/generated/plotly_*.png
```

PNG chỉ được tạo nếu Kaleido chạy được. Nếu không, mở file HTML rồi chụp màn hình.

### Streamlit

```bash
python -m streamlit run tools/streamlit_app.py
```

Mở:

```text
http://localhost:8501
```

Phù hợp nhất cho demo dashboard nhanh.

Ảnh minh họa: Streamlit không tự sinh file ảnh. Khi cần chèn báo cáo, chụp màn hình và lưu vào:

```text
screenshots/manual/streamlit_*.png
```

### Dash

```bash
python tools/dash_app.py
```

Mở:

```text
http://127.0.0.1:8050
```

Phù hợp cho dashboard web có cấu trúc callback rõ ràng.

Ảnh minh họa: Dash không tự sinh file ảnh. Khi cần chèn báo cáo, chụp màn hình và lưu vào:

```text
screenshots/manual/dash_*.png
```

### Bokeh

```bash
python tools/bokeh_demo.py
```

Output:

```text
screenshots/generated/bokeh_dashboard.html
```

Mở file HTML bằng browser để xem dashboard tương tác.

### Mermaid.js

Mở file:

```text
tools/mermaid_examples.md
```

Mermaid dùng để minh họa data pipeline, architecture và pie chart đơn giản. Đây không phải thư viện chính cho histogram/time-series/dashboard dữ liệu.

## 6. Báo Cáo

Báo cáo chính:

```text
reports/tool_comparison_report.md
```

Ma trận so sánh:

```text
reports/comparison_matrix.csv
reports/comparison_matrix.md
```

## 7. Thứ Tự Chạy Đề Xuất

1. Cài thư viện bằng `pip install -r requirements.txt`.
2. Chạy `python scripts/generate_static_charts.py` để sinh output ban đầu.
3. Mở `reports/tool_comparison_report.md` để đọc báo cáo.
4. Chạy `python -m streamlit run tools/streamlit_app.py` để demo dashboard nhanh.
5. Chạy `python tools/dash_app.py` để demo dashboard kiểu web app.

## 8. Recommendation Nhanh

- Demo web nhanh: Streamlit + Plotly.
- Dashboard production-style: Dash + Plotly.
- Báo cáo học thuật: Matplotlib + Mermaid.
- Interactive HTML độc lập: Plotly hoặc Bokeh.
