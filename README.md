# Data Visualization Tool Comparison Report

## 1. Mục tiêu

Project này thử nghiệm nhiều tool visualization trên cùng một dataset e-commerce nhỏ để so sánh khả năng sử dụng trong phân tích dữ liệu, báo cáo, web demo và dashboard.

Dataset clean: `data/ecommerce_events_clean.csv`

Các chart đã thử:

- Event type distribution
- Price distribution
- Brand count
- Events over time
- Category distribution

Vì dataset nhỏ và phép tổng hợp khá đơn giản, nhiều biểu đồ nhìn gần giống nhau. Điều này không có nghĩa các tool giống nhau. Khác biệt chính nằm ở khả năng kỹ thuật: static export, interactivity, web integration, dashboard, customization và mức phù hợp trong thực tế.

## 2. Kết quả minh họa theo tool

### Matplotlib

![Matplotlib dashboard](screenshots/generated/matplotlib_dashboard.png)

Matplotlib phù hợp nhất cho ảnh tĩnh trong báo cáo, PDF hoặc slide. Điểm mạnh là kiểm soát chi tiết tốt, export PNG ổn định, dễ dùng trong báo cáo học thuật. Điểm yếu là gần như không có tương tác nếu chỉ dùng ảnh tĩnh.

### Plotly

![Plotly events over time](screenshots/generated/plotly_events_over_time.png)

Plotly mạnh nhất ở interactive chart. Chart có hover, zoom, pan, legend toggle và có thể export HTML/PNG. Với ảnh tĩnh, output có thể giống Matplotlib, nhưng khi mở HTML thì trải nghiệm khác rõ rệt.

### Streamlit

![Streamlit dashboard](screenshots/generated/streamlit_dashboard.png)

Streamlit phù hợp để làm web demo nhanh. Chỉ cần Python là có dashboard với filter, metric, bảng dữ liệu và chart tương tác. Điểm yếu là UI tùy biến không sâu bằng Dash hoặc frontend riêng.

### Dash

![Dash dashboard](screenshots/generated/dash_dashboard.png)

Dash phù hợp dashboard chuyên nghiệp hơn Streamlit. Nó có callback rõ ràng, layout có cấu trúc và dễ mở rộng khi app có nhiều filter hoặc nhiều chart liên kết. Đổi lại, code dài hơn và learning curve cao hơn.

### Mermaid.js

![Mermaid data pipeline](screenshots/generated/mermaid_data_pipeline.png)

Mermaid không phải tool chính để vẽ chart dữ liệu. Nó phù hợp nhất để mô tả pipeline, architecture, flowchart hoặc diagram trong tài liệu kỹ thuật.

### Bokeh

![Bokeh dashboard](screenshots/generated/bokeh_dashboard.png)

Bokeh tạo interactive chart trên browser và xuất HTML độc lập tốt. Tuy nhiên, với project nhỏ này, Plotly thực tế hơn vì dễ học hơn, phổ biến hơn và tích hợp tốt với Dash/Streamlit.

## 3. So sánh nhanh

| Tool | Ease | Interactive | Web | Dashboard | Custom | Độ đẹp | Best Use Case |
|------|------|-------------|-----|-----------|--------|--------|---------------|
| Matplotlib | Medium | Low | Low | Low | Very high | Đẹp cho PDF/report | Static chart, học thuật, báo cáo |
| Plotly | High | Very high | Very high | Medium | High | Đẹp cho chart web | Interactive chart, HTML demo |
| Streamlit | Very high | High | High | High | Medium | Đẹp cho demo nhanh | Prototype dashboard, data app |
| Dash | Medium | Very high | Very high | Very high | Very high | Đẹp nếu đầu tư UI | Dashboard chuyên nghiệp |
| Mermaid.js | High | Low | High | Low | Medium | Đẹp cho diagram | Pipeline, architecture docs |
| Bokeh | Medium | High | High | Medium | High | Khá tốt trên browser | Interactive HTML chart |

## 4. Nhận xét chính

### Ease of Use

Streamlit dễ nhất để tạo dashboard nhanh. Plotly dễ nhất để tạo interactive chart. Dash và Bokeh cần nhiều cấu hình hơn. Matplotlib dễ bắt đầu nhưng code dài hơn khi có nhiều subplot.

### Static Visualization

Matplotlib tốt nhất cho ảnh tĩnh vì export ổn định và kiểm soát chi tiết tốt. Plotly cũng xuất PNG được, nhưng bản chất mạnh hơn ở HTML interactive.

### Interactivity

Plotly tốt nhất cho chart tương tác đơn lẻ. Dash tốt nhất cho dashboard nhiều callback. Streamlit tốt nhất cho demo tương tác nhanh. Matplotlib và Mermaid gần như không phù hợp cho tương tác dữ liệu.

### Web Integration

Dash mạnh nhất nếu cần dashboard web nghiêm túc. Streamlit nhanh nhất để demo. Plotly dễ nhúng HTML. Bokeh cũng xuất HTML tốt nhưng ít phổ biến hơn Plotly trong workflow hiện đại.

### Độ đẹp

Không thể nói chung chung tool nào đẹp nhất. Với PDF/report, Matplotlib đẹp và rõ nhất nếu tinh chỉnh tốt. Với web chart, Plotly hiện đại hơn nhờ hover và zoom. Với demo nhanh, Streamlit đẹp vì có sẵn layout app. Với dashboard production, Dash đẹp nhất nếu đầu tư CSS/layout. Với tài liệu kỹ thuật, Mermaid đẹp nhất cho sơ đồ luồng xử lý.

## 5. Recommendation

| Mục đích | Tool nên dùng |
|---------|---------------|
| Học và báo cáo PDF | Matplotlib |
| Interactive chart | Plotly |
| Web demo nhanh | Streamlit + Plotly |
| Dashboard chuyên nghiệp | Dash + Plotly |
| Diagram / mô tả hệ thống | Mermaid.js |
| Interactive HTML thay thế | Bokeh |

Nếu làm project AI/Data Analytics thực tế:

- Giai đoạn explore data: dùng Matplotlib + Plotly.
- Giai đoạn demo: dùng Streamlit + Plotly.
- Giai đoạn production dashboard: dùng Dash + Plotly.
- Giai đoạn documentation: dùng Mermaid.js.

## 6. Kết luận


Với project này, lựa chọn thực tế nhất là: Matplotlib cho báo cáo tĩnh, Plotly cho interactive chart, Streamlit cho demo nhanh, Dash cho dashboard chuyên nghiệp và Mermaid cho tài liệu kỹ thuật.

- Matplotlib: đẹp theo kiểu “academic”, rõ ràng, tối giản, phù hợp báo cáo PDF.
- Plotly: đẹp theo kiểu “modern web”, có hiệu ứng hover, nhìn trực quan hơn khi tương tác.
- Streamlit: không phải chart đẹp nhất, nhưng tổng thể UI dashboard nhìn “app-like” và chuyên nghiệp.
- Dash: đẹp nhất nếu được custom CSS tốt, nhưng mặc định khá basic.
- Mermaid: đẹp theo hướng sơ đồ kỹ thuật, không phù hợp cho data chart.

## 7. Tools tìm hiểu thêm: Power BI vs Tableau

Phần này dùng cùng dataset `data/ecommerce_events_clean.csv` để tạo dashboard trên các BI tool phổ biến. Mục tiêu là so sánh theo khả năng business dashboard, không so sánh theo code.

### 7.1 Power BI

**Setup**

- Cài Power BI Desktop.
- Mở Power BI Desktop → `Get data` → `Text/CSV`.
- Chọn file `data/ecommerce_events_clean.csv`.
- Trong Power Query, kiểm tra kiểu dữ liệu:
  - `event_time`: Date/Time
  - `price`: Decimal number
  - `event_type`, `brand`, `category_code`: Text
  - `product_id`, `user_id`: Whole number hoặc Text nếu chỉ dùng làm ID
- Tạo thêm cột `category_root` bằng cách split `category_code` theo dấu `.` và lấy phần đầu.

**Chart nên tạo**

- Event type distribution: Clustered column chart, Axis = `event_type`, Values = Count of rows.
- Price distribution: Histogram bằng bin của `price`, hoặc column chart theo price range.
- Brand count: Bar chart, Axis = `brand`, Values = Count of rows.
- Events over time: Line chart, Axis = `event_time`, Values = Count of rows.
- Category distribution: Bar chart, Axis = `category_root`, Values = Count of rows.

**Dashboard + slicer**

- Thêm slicer cho `event_type`.
- Thêm slicer cho `brand` hoặc `category_root`.
- Thêm card: Total events, Average price, Unique users.
- Layout gợi ý: KPI cards ở hàng đầu, chart chính ở giữa, slicer bên trái hoặc phía trên.

**Nhận xét nhanh**

Power BI phù hợp business dashboard, báo cáo nội bộ và môi trường Microsoft. Điểm mạnh là data model, Power Query, slicer, DAX và publish lên Power BI Service. Điểm yếu là cần làm quen với DAX/data model nếu dashboard phức tạp.

### 7.2 Tableau

**Setup**

- Cài Tableau Public hoặc Tableau Desktop.
- Mở Tableau → `Connect` → `Text file`.
- Chọn file `data/ecommerce_events_clean.csv`.
- Kiểm tra kiểu dữ liệu:
  - `event_time`: Date & Time
  - `price`: Number decimal
  - `event_type`, `brand`, `category_code`: String
- Tạo calculated field `category_root`:

```text
SPLIT([category_code], ".", 1)
```

**Chart nên tạo**

- Event type distribution: Columns = `event_type`, Rows = COUNT records.
- Price distribution: dùng `price` bins, Rows = COUNT records.
- Brand count: Rows = `brand`, Columns = COUNT records, sort descending.
- Events over time: Columns = `event_time`, Rows = COUNT records, chọn line chart.
- Category distribution: Rows = `category_root`, Columns = COUNT records.

**Dashboard**

- Tạo từng worksheet cho mỗi chart.
- Tạo Dashboard mới và kéo các worksheet vào.
- Thêm filter cho `event_type`, `brand`, `category_root`.
- Bật `Use as Filter` cho chart chính nếu muốn click vào chart để lọc dashboard.

**Nhận xét nhanh**

Tableau phù hợp data exploration và tạo dashboard trực quan nhanh. Điểm mạnh là kéo-thả linh hoạt, visual đẹp, interaction tự nhiên. Điểm yếu là data modeling và transformation không tiện bằng Power Query trong Power BI.

### 7.3 Bảng so sánh

| Tiêu chí | Power BI | Tableau |
|---|---|---|
| Ease of use | Dễ nếu quen Excel/Microsoft | Dễ kéo-thả, trực quan hơn khi explore |
| Visualization quality | Tốt, business-oriented | Rất tốt, visual polished hơn mặc định |
| Dashboard capability | Rất mạnh cho báo cáo doanh nghiệp | Rất mạnh cho dashboard phân tích trực quan |
| Interactivity | Slicer, drill-down, cross-filter tốt | Filter, highlight, click-to-filter rất mượt |
| Learning curve | Cần học Power Query, DAX, data model | Cần học shelf, calculated field, dashboard action |
| Use case | Business reporting, KPI dashboard, Microsoft ecosystem | Data exploration, presentation, visual analytics |

### 7.4 Kết luận

- Beginner: Tableau dễ làm quen hơn nếu chỉ kéo-thả và khám phá dữ liệu.
- Business dashboard: Power BI phù hợp hơn vì mạnh về data model, DAX, Power Query và hệ sinh thái Microsoft.
- Data exploration: Tableau phù hợp hơn vì thao tác trực quan, kéo-thả nhanh và visual đẹp mặc định.
- Nếu làm báo cáo nội bộ công ty: ưu tiên Power BI.
- Nếu cần trình bày phân tích đẹp, nhanh, dễ demo: ưu tiên Tableau.

### 7.5 Gợi ý chụp ảnh dashboard đẹp

- Dùng layout 16:9, nền trắng hoặc xám rất nhạt.
- Hàng đầu đặt 3-4 KPI cards: Total events, Average price, Unique users, Total brands.
- Bên trái đặt slicer/filter: event type, brand, category.
- Ở giữa đặt chart quan trọng nhất: Events over time hoặc Event type distribution.
- Bên phải hoặc hàng dưới đặt Brand count và Category distribution.
- Tránh dùng quá nhiều màu; chỉ dùng 1 màu chính và 1 màu nhấn.
- Trước khi chụp, sort bar chart giảm dần và ẩn category/brand quá nhỏ nếu bị rối.

Ảnh nộp nên lưu tại:

- `screenshots/manual/powerbi_dashboard.png`
- `screenshots/manual/tableau_dashboard.png`
