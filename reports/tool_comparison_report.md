# Báo Cáo Phân Tích Và So Sánh Tool Data Visualization

## 1. Introduction

Mục tiêu của báo cáo này là phân tích và so sánh các công cụ visualization đã được thử nghiệm trên cùng một dataset e-commerce nhỏ. Các công cụ gồm Matplotlib, Plotly, Streamlit, Dash, Mermaid.js và Bokeh. Dataset đã được chuẩn hóa tại `data/ecommerce_events_clean.csv`, gồm các trường chính: `event_time`, `event_type`, `product_id`, `category_code`, `brand`, `price`, `user_id`.

Các biểu đồ đã thực hiện gồm:

- Event type distribution
- Price distribution
- Brand count
- Events over time
- Category distribution

Một điểm quan trọng cần làm rõ ngay từ đầu: các biểu đồ nhìn giống nhau không có nghĩa tool giống nhau. Với dataset nhỏ, số lượng bản ghi ít và cấu trúc dữ liệu đơn giản, biểu đồ dạng bar chart, histogram hoặc line chart thường có hình dạng gần giống nhau giữa các thư viện. Lý do là tất cả tool đều đang biểu diễn cùng một phép tổng hợp dữ liệu: đếm số event, nhóm theo brand/category, hoặc vẽ phân bố giá.

Vì vậy, báo cáo này không đánh giá tool chỉ dựa trên việc chart "đẹp hơn" hay "xấu hơn". Sự khác biệt thực sự nằm ở mục đích sử dụng, khả năng tương tác, khả năng tích hợp web, mức độ tùy biến, khả năng dashboard, khả năng mở rộng và mức phù hợp trong quy trình làm việc thực tế.

## 2. Tổng Quan Từng Tool

### 2.1 Matplotlib

Matplotlib là thư viện visualization nền tảng trong hệ sinh thái Python. Nó được thiết kế chủ yếu để tạo biểu đồ tĩnh, có độ kiểm soát cao, phù hợp cho notebook, báo cáo, paper, slide hoặc tài liệu kỹ thuật.

Điểm mạnh lớn nhất của Matplotlib là tính ổn định và khả năng kiểm soát chi tiết. Người dùng có thể can thiệp vào gần như mọi thành phần của biểu đồ: trục, label, tick, legend, màu sắc, kích thước, layout, font, figure size và chất lượng ảnh export. Với báo cáo PDF hoặc slide, Matplotlib rất đáng tin vì có thể xuất PNG/SVG/PDF ổn định.

Điểm yếu của Matplotlib là interactivity gần như không phải trọng tâm. Nếu cần hover, zoom, filter động hoặc dashboard web, Matplotlib phải kết hợp với công cụ khác hoặc framework bổ sung. Code Matplotlib cũng có thể trở nên dài khi cần layout phức tạp.

Nên dùng Matplotlib khi cần chart tĩnh chất lượng tốt, kiểm soát chi tiết, dùng trong báo cáo học thuật, phân tích offline hoặc tài liệu cần tái lập kết quả.

### 2.2 Plotly

Plotly là thư viện visualization hiện đại, tập trung vào biểu đồ tương tác và tích hợp web. Trong project này, Plotly được dùng để tạo cả HTML chart và PNG chart thông qua Kaleido.

Điểm mạnh của Plotly là interactivity mặc định rất tốt. Các thao tác như hover tooltip, zoom, pan, toggle legend và export chart thường có sẵn mà không cần viết nhiều code. Output HTML độc lập cũng giúp Plotly dễ chia sẻ và dễ nhúng vào web hoặc dashboard.

Điểm yếu của Plotly là file HTML có thể nặng hơn ảnh tĩnh, và việc tùy biến cực sâu đôi khi không trực tiếp như Matplotlib. Với yêu cầu in ấn hoặc paper có style rất nghiêm ngặt, Plotly thường cần thêm tinh chỉnh để đạt chuẩn học thuật.

Nên dùng Plotly khi cần interactive chart, demo web, dashboard, notebook presentation hoặc các chart cần người xem tự khám phá dữ liệu.

### 2.3 Streamlit

Streamlit không chỉ là thư viện vẽ chart, mà là framework để dựng data app nhanh bằng Python. Trong project này, Streamlit dùng Plotly chart bên trong để tạo dashboard đơn giản có filter, metric và bảng dữ liệu.

Điểm mạnh của Streamlit là tốc độ phát triển. Với ít code, người dùng có thể tạo một dashboard local hoặc web demo có sidebar filter, tab, metric card, dataframe và chart tương tác. Đây là công cụ rất phù hợp cho prototype, demo nội bộ, phân tích nhanh và trình bày kết quả data analytics.

Điểm yếu của Streamlit là khả năng kiểm soát UI/frontend không sâu bằng Dash hoặc web app tự viết. Layout, state management và custom interaction phức tạp có thể bị giới hạn khi dự án lớn hơn.

Nên dùng Streamlit khi cần biến notebook hoặc script phân tích thành app demo nhanh, đặc biệt trong giai đoạn trình bày kết quả cho stakeholder hoặc team nội bộ.

### 2.4 Dash

Dash là framework dashboard web dựa trên Flask, React component và Plotly. So với Streamlit, Dash có cấu trúc web app rõ hơn, callback explicit hơn và phù hợp hơn với dashboard nhiều tương tác.

Điểm mạnh của Dash là khả năng xây dựng dashboard chuyên nghiệp bằng Python. Người dùng có thể tạo layout, component, filter, callback và update chart theo logic rõ ràng. Dash phù hợp hơn Streamlit khi cần app có cấu trúc production-style, nhiều trang, nhiều input hoặc nhiều trạng thái tương tác.

Điểm yếu của Dash là learning curve cao hơn. Người dùng cần hiểu layout, callback, component tree và cách dữ liệu đi qua app. Với demo nhỏ, Dash có thể cảm giác dài dòng hơn Streamlit.

Nên dùng Dash khi cần dashboard nghiêm túc, có nhiều filter, nhiều biểu đồ liên kết, nhiều callback hoặc có khả năng triển khai production.

### 2.5 Mermaid.js

Mermaid.js là công cụ diagram-as-code, không phải thư viện data visualization dạng plotting library. Nó phù hợp để viết flowchart, sequence diagram, architecture diagram, state diagram hoặc pie chart đơn giản ngay trong Markdown.

Điểm mạnh của Mermaid là cực kỳ tiện cho tài liệu kỹ thuật. Người viết có thể mô tả data pipeline, kiến trúc hệ thống hoặc luồng xử lý bằng text, dễ version control và dễ nhúng vào README/report.

Điểm yếu của Mermaid là không phù hợp cho histogram, time series, dashboard hoặc chart dữ liệu tương tác phức tạp. Mermaid không nên được so sánh trực tiếp với Plotly hoặc Matplotlib ở vai trò vẽ chart phân tích dữ liệu.

Nên dùng Mermaid khi cần minh họa luồng xử lý dữ liệu, kiến trúc project, quan hệ thành phần hoặc diagram trong tài liệu.

### 2.6 Bokeh

Bokeh là thư viện visualization Python tập trung vào biểu đồ tương tác trên browser. Nó có thể xuất HTML độc lập và hỗ trợ các tương tác như pan, zoom, hover hoặc selection.

Điểm mạnh của Bokeh là khả năng tạo interactive chart Python-native, có thể hoạt động tốt trong browser mà không cần xây dựng full dashboard app. So với Plotly, Bokeh cho cảm giác gần hơn với mô hình xây dựng figure thủ công, phù hợp khi cần kiểm soát chart ở mức thấp hơn.

Điểm yếu của Bokeh là ecosystem và mức phổ biến trong dashboard hiện đại thường kém Plotly + Dash/Streamlit. Với người mới, API của Bokeh có thể ít trực quan hơn Plotly Express.

Nên dùng Bokeh khi cần interactive visualization dạng HTML, muốn ở trong hệ Python và cần nhiều kiểm soát hơn so với chart nhanh kiểu Plotly Express.

## 3. So Sánh Theo Tiêu Chí

### 3.1 Ease of Use

Streamlit là tool dễ dùng nhất nếu mục tiêu là tạo một demo dashboard nhanh. Người dùng chỉ cần viết Python, gọi `st.dataframe`, `st.plotly_chart`, `st.sidebar` và có ngay một app chạy local. Với người làm data analytics, Streamlit rất gần với tư duy notebook.

Plotly cũng rất dễ dùng ở cấp độ chart đơn lẻ, đặc biệt với Plotly Express. Ví dụ, bar chart hoặc histogram có thể tạo bằng một hàm ngắn. Nếu chỉ cần interactive chart, Plotly dễ hơn Bokeh và Dash.

Matplotlib dễ bắt đầu nhưng code có thể dài hơn khi cần nhiều chart trong cùng dashboard tĩnh. Người dùng phải tự quản lý `fig`, `axes`, layout, rotation, label và export.

Dash phức tạp hơn vì yêu cầu hiểu layout và callback. Bokeh cũng cần nhiều cấu hình hơn Plotly Express. Mermaid dễ viết nếu là flowchart đơn giản, nhưng không dễ áp dụng cho chart dữ liệu dạng bảng.

Xếp hạng ease of use cho project này:

1. Streamlit
2. Plotly
3. Matplotlib
4. Mermaid.js
5. Bokeh
6. Dash

### 3.2 Learning Curve

Streamlit có learning curve thấp nhất đối với người đã biết Python. Người dùng không cần hiểu nhiều về frontend, routing hoặc callback phức tạp để tạo demo.

Plotly cũng dễ học ở mức cơ bản, nhưng để tùy biến sâu layout, hover template, animation, facet, secondary axis hoặc export ảnh chất lượng cao thì cần học thêm.

Matplotlib có learning curve trung bình. Cú pháp ban đầu đơn giản, nhưng hệ thống `figure`, `axes`, `artist`, `style`, `subplot`, `tight_layout` có thể mất thời gian để thành thạo.

Dash có learning curve cao hơn vì nó là web framework. Người dùng cần hiểu callback, input/output, state, component id và cấu trúc app. Đây là chi phí hợp lý nếu mục tiêu là dashboard chuyên nghiệp.

Bokeh nằm giữa Plotly và Dash. Nó không khó như full web framework, nhưng API hơi dài và ít "one-line chart" hơn Plotly Express.

Mermaid rất dễ cho diagram cơ bản, nhưng không phải learning curve về data chart mà là learning curve về syntax diagram.

### 3.3 Static Visualization

Matplotlib là lựa chọn tốt nhất cho static visualization. Nó xuất ảnh tĩnh ổn định, nhẹ, dễ đưa vào PDF, slide hoặc report. Khi cần kiểm soát kích thước figure, DPI, font, axis, label và layout, Matplotlib thường đáng tin nhất.

Plotly có thể xuất PNG thông qua Kaleido, nhưng bản chất Plotly mạnh hơn ở interactive HTML. Plotly PNG nhìn hiện đại, nhưng phụ thuộc thêm engine export và đôi khi cần cấu hình môi trường.

Bokeh có thể xuất HTML tốt hơn là ảnh tĩnh. Streamlit và Dash chủ yếu là app, không phải công cụ sinh ảnh tĩnh. Mermaid có thể render diagram trong Markdown, phù hợp với tài liệu hệ thống hơn là biểu đồ phân tích.

Kết luận cho static visualization: Matplotlib là lựa chọn số 1, Plotly là lựa chọn phụ khi muốn chart có style web hiện đại nhưng vẫn cần PNG.

### 3.4 Interactivity

Plotly mạnh nhất ở interactive chart độc lập. Hover tooltip, zoom, pan, select, legend toggle và HTML export đều hoạt động tốt. Với cùng dataset nhỏ, chart Plotly có thể nhìn giống Matplotlib ở ảnh tĩnh, nhưng trải nghiệm người dùng khác hoàn toàn khi mở HTML.

Dash và Streamlit có interactivity ở cấp dashboard. Sự khác biệt là Plotly tương tác ở cấp chart, còn Dash/Streamlit tương tác ở cấp app: filter event type, update nhiều chart, hiển thị metric, xem bảng dữ liệu.

Bokeh cũng có interactivity tốt, nhất là pan/zoom và browser-based output. Tuy nhiên, trong project nhỏ này, lợi thế của Bokeh không nổi bật bằng Plotly vì biểu đồ đơn giản.

Matplotlib gần như không có interactivity nếu chỉ xuất PNG. Mermaid cũng gần như không có interactivity dữ liệu, dù có thể render diagram trong web/Markdown.

Kết luận: Plotly tốt nhất cho interactive chart, Dash tốt nhất cho interactive dashboard có logic rõ, Streamlit tốt nhất cho interactive demo nhanh.

### 3.5 Web Integration

Plotly tích hợp web rất tốt vì output HTML có thể mở trực tiếp hoặc nhúng vào web app. Khi dùng với Dash, Plotly gần như là lựa chọn tự nhiên cho dashboard Python.

Streamlit có web integration tốt ở dạng data app. Chỉ cần chạy server local là có giao diện web. Tuy nhiên, Streamlit phù hợp hơn cho app nội bộ hoặc demo nhanh, không phải frontend tùy biến sâu.

Dash có web integration mạnh nhất nếu nhìn theo hướng app web có cấu trúc. Nó dựa trên Flask/React component, có thể deploy như web service và mở rộng tốt hơn Streamlit khi yêu cầu phức tạp.

Bokeh xuất HTML độc lập tốt, nhưng nếu cần dashboard app hoàn chỉnh thì thường không phổ biến bằng Streamlit/Dash.

Matplotlib phù hợp local/report hơn là web. Mermaid tích hợp web tốt trong Markdown renderer, GitHub, docs site hoặc static documentation, nhưng không phải web charting library cho dữ liệu bảng.

### 3.6 Dashboard Capability

Dash là lựa chọn mạnh nhất cho dashboard chuyên nghiệp. Nó có mô hình callback rõ, nhiều component và khả năng kiểm soát layout tốt. Nếu dashboard cần nhiều filter, nhiều chart liên kết, cập nhật động và logic tương tác rõ ràng, Dash phù hợp nhất.

Streamlit là lựa chọn tốt nhất cho dashboard nhanh. Nó giúp tạo demo rất nhanh, nhưng khi dashboard lớn, nhiều state, nhiều component tùy biến, Streamlit có thể khó kiểm soát hơn Dash.

Plotly không phải dashboard framework độc lập, nhưng là chart engine rất tốt trong dashboard. Plotly thường đi cùng Dash hoặc Streamlit.

Bokeh có thể làm dashboard, nhưng trong thực tế hiện đại, nếu team Python muốn demo nhanh thì Streamlit phổ biến hơn; nếu muốn app dashboard có cấu trúc thì Dash rõ hơn.

Matplotlib và Mermaid không phù hợp làm dashboard chính. Matplotlib tạo ảnh tĩnh; Mermaid tạo diagram tài liệu.

### 3.7 Customization

Matplotlib có khả năng tùy biến chart rất sâu. Nó phù hợp khi cần kiểm soát từng chi tiết hình ảnh cho báo cáo hoặc publication.

Dash có khả năng tùy biến app tốt hơn Streamlit vì layout và component rõ ràng hơn. Có thể kết hợp CSS, HTML component và callback để tạo dashboard chuyên nghiệp.

Plotly có khả năng tùy biến chart tốt: màu sắc, template, hover, annotation, axis, legend, subplot. Tuy nhiên, khi muốn kiểm soát từng pixel như Matplotlib, Plotly không phải lúc nào cũng tiện hơn.

Streamlit dễ dùng nhưng tùy biến UI có giới hạn. Có thể chỉnh layout, sidebar, tabs và theme, nhưng không linh hoạt bằng Dash hoặc frontend riêng.

Bokeh cho phép tùy biến nhiều ở cấp figure/model, nhưng API dài hơn. Mermaid tùy biến được diagram ở mức vừa phải, không phù hợp tùy biến chart dữ liệu phức tạp.

### 3.8 Suitability for Project

Với dataset nhỏ và yêu cầu viết báo cáo so sánh tool, Matplotlib và Plotly là hai tool quan trọng nhất. Matplotlib phù hợp để sinh ảnh tĩnh đưa vào báo cáo; Plotly phù hợp để chứng minh năng lực interactive và web output.

Streamlit phù hợp nhất để demo nhanh cho người xem không cần đọc code. Nó cho thấy dữ liệu có thể biến thành data app chỉ bằng Python.

Dash phù hợp để chứng minh hướng production/dashboard chuyên nghiệp. Tuy nhiên, với dataset nhỏ, Dash có thể hơi "nặng" nếu chỉ cần vài chart đơn giản.

Mermaid rất phù hợp cho phần documentation, đặc biệt khi cần giải thích data pipeline hoặc kiến trúc project. Nó không nên bị đánh giá thấp chỉ vì không vẽ histogram tốt.

Bokeh là lựa chọn bổ sung tốt để so sánh với Plotly về interactive HTML. Tuy nhiên, với phạm vi project này, Plotly có tính thực tế cao hơn vì dễ học, dễ demo và tích hợp tốt với Dash/Streamlit.

## 4. 🎨 ĐÁNH GIÁ “ĐỘ ĐẸP”

### 4.1 Đẹp Cho Báo Cáo Học Thuật

Trong ngữ cảnh báo cáo học thuật, "đẹp" không có nghĩa là nhiều hiệu ứng. Một biểu đồ đẹp cho PDF/slide cần rõ ràng, dễ đọc, font ổn định, màu không gây nhiễu, label đầy đủ và export sắc nét.

Matplotlib là lựa chọn đẹp nhất cho báo cáo học thuật nếu được tinh chỉnh đúng. Lý do là Matplotlib cho phép kiểm soát DPI, figure size, trục, label, tick và layout rất tốt. Biểu đồ Matplotlib có thể nhìn basic nếu dùng mặc định, nhưng khi chỉnh style hợp lý, nó phù hợp nhất với paper, PDF và slide nghiêm túc.

Plotly PNG nhìn hiện đại hơn mặc định, nhưng style của Plotly thiên về web. Trong PDF học thuật, Plotly có thể hơi "dashboard-like" nếu không chỉnh template, font và spacing.

Bokeh không phải lựa chọn đẹp nhất cho PDF vì output chính là HTML interactive. Streamlit và Dash là app, nên ảnh chụp màn hình có thể dùng trong báo cáo nhưng không phải nguồn ảnh học thuật lý tưởng.

Mermaid đẹp trong ngữ cảnh sơ đồ hệ thống. Một flowchart Mermaid rõ ràng có giá trị cao trong báo cáo kỹ thuật, nhưng không thay thế chart phân tích dữ liệu.

Kết luận cho báo cáo học thuật: Matplotlib đẹp nhất cho chart dữ liệu tĩnh; Mermaid đẹp nhất cho diagram giải thích luồng xử lý.

### 4.2 Đẹp Cho Web/App Demo

Trong ngữ cảnh web/app demo, "đẹp" liên quan đến cảm giác hiện đại, khả năng tương tác, tooltip, spacing, responsiveness và trải nghiệm khi người dùng xem trên browser.

Plotly là đẹp nhất cho chart web đơn lẻ. Hover tooltip, toolbar, zoom và template mặc định giúp chart nhìn hiện đại hơn Matplotlib khi mở trong browser.

Streamlit đẹp theo hướng nhanh và thực dụng. Giao diện có metric card, sidebar, tabs và dataframe, phù hợp để demo nội bộ. Tuy nhiên, nếu cần brand identity hoặc UI tùy biến sâu, Streamlit không phải đẹp nhất.

Dash có thể đẹp và chuyên nghiệp hơn Streamlit nếu đầu tư CSS/layout. Trong project này, Dash có nhiều tiềm năng hơn cho web app nghiêm túc, nhưng cần nhiều công chỉnh UI hơn để đạt độ polished.

Bokeh nhìn ổn trong browser và có toolbar tương tác, nhưng cảm giác hiện đại mặc định thường kém Plotly. Matplotlib PNG trên web thường chỉ như ảnh nhúng, không tạo cảm giác app. Mermaid đẹp khi nằm trong docs, không phải app analytics.

Kết luận cho web/app demo: Plotly đẹp nhất cho chart interactive; Streamlit đẹp nhất nếu ưu tiên demo nhanh; Dash đẹp nhất nếu có thời gian đầu tư UI dashboard.

### 4.3 Đẹp Về Mặt Interactive

Đẹp về mặt interactive không chỉ là màu sắc. Một interactive visualization đẹp cần phản hồi tốt khi hover, zoom mượt, tooltip dễ hiểu, legend có thể bật/tắt, và không làm người dùng bị rối.

Plotly nổi bật nhất ở điểm này. Với cùng một bar chart hoặc line chart, ảnh tĩnh có thể giống Matplotlib, nhưng khi mở HTML, Plotly cho cảm giác khám phá dữ liệu tốt hơn. Người xem có thể hover để xem giá trị chính xác, zoom vào vùng thời gian, hoặc bật/tắt nhóm dữ liệu.

Dash đẹp về interaction ở cấp dashboard vì filter có thể cập nhật nhiều chart cùng lúc. Đây là kiểu đẹp mang tính hệ thống: người dùng thay đổi input và cả dashboard phản hồi.

Streamlit cũng đẹp ở cấp dashboard demo, nhưng interaction thường đơn giản hơn Dash. Nó phù hợp với filter cơ bản, tab, metric và chart update nhanh.

Bokeh có interactive tốt nhưng cần cấu hình thêm để đạt trải nghiệm ngang Plotly trong các chart phổ biến. Matplotlib PNG và Mermaid gần như không có trải nghiệm interactive dữ liệu.

Kết luận cho interactive: Plotly đẹp nhất cho chart; Dash đẹp nhất cho dashboard logic phức tạp; Streamlit đẹp nhất cho demo tương tác nhanh.

### 4.4 Kết Luận Về Độ Đẹp

Không thể nói chung chung "Plotly đẹp hơn" hoặc "Matplotlib xấu hơn". Độ đẹp phụ thuộc vào ngữ cảnh sử dụng.

Nếu mục tiêu là báo cáo PDF hoặc slide học thuật, Matplotlib đẹp hơn vì dễ kiểm soát tính rõ ràng, bố cục và chất lượng ảnh. Nếu mục tiêu là chart web tương tác, Plotly đẹp hơn vì tooltip, zoom và HTML output tạo trải nghiệm hiện đại. Nếu mục tiêu là demo data app nhanh, Streamlit đẹp vì toàn bộ dashboard có thể chạy ngay với ít code. Nếu mục tiêu là dashboard chuyên nghiệp, Dash đẹp khi được đầu tư layout và CSS. Nếu mục tiêu là mô tả hệ thống, Mermaid đẹp vì diagram rõ ràng, dễ đọc và sống ngay trong tài liệu.

Vì dataset nhỏ, biểu đồ output có thể giống nhau ở mức hình ảnh, nhưng "độ đẹp thực tế" nằm ở cách người dùng tiêu thụ biểu đồ: đọc trong PDF, tương tác trên browser, demo trong dashboard hay hiểu kiến trúc trong documentation.

## 5. Bảng So Sánh Tổng Hợp

| Tool | Ease | Interactive | Web | Dashboard | Custom | Độ đẹp | Best Use Case |
|------|------|-------------|-----|-----------|--------|--------|---------------|
| Matplotlib | Medium | Low | Low | Low | Very high | Đẹp nhất cho PDF/report nếu tinh chỉnh | Static chart, academic report, export PNG/PDF |
| Plotly | High | Very high | Very high | Medium | High | Đẹp nhất cho chart web interactive | Interactive chart, HTML demo, notebook presentation |
| Streamlit | Very high | High | High | High | Medium | Đẹp cho demo nhanh, UI đủ tốt | Quick data app, internal demo, prototype dashboard |
| Dash | Medium | Very high | Very high | Very high | Very high | Đẹp nhất cho dashboard nếu đầu tư UI | Production-style dashboard, multi-filter analytics app |
| Mermaid.js | High | Low | High | Low | Medium | Đẹp cho diagram tài liệu | Data pipeline, architecture diagram, technical docs |
| Bokeh | Medium | High | High | Medium | High | Đẹp vừa phải cho browser chart | Interactive HTML chart, Python-native web visualization |

## 6. Kết Luận

### 6.1 Tool Tốt Nhất Cho Từng Mục Đích

Học và báo cáo PDF: Matplotlib là lựa chọn tốt nhất. Nó giúp người học hiểu rõ cấu trúc biểu đồ và tạo ảnh tĩnh phù hợp cho báo cáo.

Interactive chart: Plotly là lựa chọn tốt nhất. Nó cung cấp hover, zoom, pan và HTML output gần như ngay lập tức.

Web demo nhanh: Streamlit là lựa chọn tốt nhất. Nó biến script Python thành data app rất nhanh, phù hợp demo stakeholder hoặc bài nộp thực nghiệm.

Dashboard chuyên nghiệp: Dash là lựa chọn tốt nhất. Nó có callback rõ ràng, layout có cấu trúc và phù hợp mở rộng hơn khi dashboard lớn.

Diagram và mô tả hệ thống: Mermaid.js là lựa chọn tốt nhất. Nó giúp tài liệu kỹ thuật dễ hiểu hơn và rất hợp với Markdown.

Bokeh: phù hợp như lựa chọn bổ sung khi cần interactive HTML chart trong hệ Python, nhưng trong project này không vượt Plotly về tính tiện dụng.

### 6.2 Recommendation Thực Tế Cho AI/Data Analytics Project

Giai đoạn explore data: dùng Pandas kết hợp Matplotlib và Plotly. Matplotlib giúp kiểm tra nhanh và xuất ảnh ổn định; Plotly giúp khám phá dữ liệu tương tác hơn khi cần hover/zoom.

Giai đoạn demo: dùng Streamlit kết hợp Plotly. Đây là combo rất hiệu quả để trình bày kết quả nhanh, ít code, dễ chạy local và đủ thuyết phục với người xem.

Giai đoạn production: dùng Dash kết hợp Plotly nếu sản phẩm là dashboard analytics nghiêm túc. Dash phù hợp hơn khi có nhiều filter, nhiều callback, nhiều user flow và cần deploy như web app.

Giai đoạn documentation: dùng Mermaid.js để mô tả pipeline, kiến trúc xử lý dữ liệu và quan hệ giữa các thành phần. Mermaid không thay chart dữ liệu, nhưng làm báo cáo kỹ thuật rõ hơn nhiều.

Giai đoạn báo cáo học thuật: dùng Matplotlib cho ảnh chính, Mermaid cho diagram, và có thể bổ sung Plotly screenshot nếu cần minh họa trải nghiệm interactive.

## 7. Insight Nâng Cao

Visualization tools should not be evaluated only by visual output, especially on small datasets, but by their capabilities, scalability, and integration potential.

Với dataset nhỏ, sự khác biệt giữa các chart thường bị "nén" lại: bar chart vẫn là bar chart, histogram vẫn là histogram, line chart vẫn là line chart. Nếu chỉ nhìn ảnh cuối, ta dễ kết luận sai rằng các tool gần như giống nhau. Nhưng trong thực tế, một visualization tool là một phần của workflow lớn hơn.

Matplotlib mạnh vì nó phục vụ báo cáo ổn định. Plotly mạnh vì nó biến chart thành trải nghiệm tương tác. Streamlit mạnh vì nó biến phân tích thành app rất nhanh. Dash mạnh vì nó đưa dashboard Python gần hơn với web app production. Mermaid mạnh vì nó làm rõ hệ thống và pipeline. Bokeh có giá trị khi cần interactive HTML chart Python-native.

Do đó, đánh giá đúng một tool visualization cần đặt nó vào ngữ cảnh: ai là người xem, xem ở đâu, có cần tương tác không, có cần deploy không, có cần xuất PDF không, có cần bảo trì lâu dài không. Một tool tốt không chỉ tạo ra chart đẹp, mà còn phù hợp với mục tiêu giao tiếp dữ liệu và khả năng vận hành trong dự án thực tế.
