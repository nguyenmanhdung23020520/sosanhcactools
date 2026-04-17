import pandas as pd

# Sample data gần giống dataset Kaggle thật
data = {
    "event_time": [
        "2019-11-01 00:00:00",
        "2019-11-01 00:00:01",
        "2019-11-01 00:00:02",
        "2019-11-01 00:00:03",
        "2019-11-01 00:00:04",
        "2019-11-01 00:00:05",
        "2019-11-01 00:00:06",
        "2019-11-01 00:00:07"
    ],
    "event_type": [
        "view", "view", "cart", "purchase",
        "view", "cart", "purchase", "view"
    ],
    "product_id": [
        1003461, 5000088, 17302664, 3601530,
        1004775, 1306894, 1306421, 15900065
    ],
    "category_id": [
        2053013555631882655,
        2053013566100866035,
        2053013553853497655,
        2053013563810775923,
        2053013555631882655,
        2053013558920217191,
        2053013558920217191,
        2053013558190408249
    ],
    "category_code": [
        "electronics.smartphone",
        "appliances.sewing_machine",
        "unknown",
        "appliances.kitchen.washer",
        "electronics.smartphone",
        "computers.notebook",
        "computers.notebook",
        "home.kitchen"
    ],
    "brand": [
        "xiaomi", "janome", "unknown", "lg",
        "apple", "hp", "hp", "rondell"
    ],
    "price": [
        489.07, 293.65, 28.31, 712.87,
        183.27, 360.09, 514.56, 30.86
    ],
    "user_id": [
        520088904, 530496790, 561587266, 518085591,
        558856683, 520772685, 514028527, 518574284
    ],
    "user_session": [
        "4d3b30da-a5e4-49df-b1a8-ba5943f1dd33",
        "8e5f4f83-366c-4f70-860e-ca7417414283",
        "755422e7-9040-477b-9bd2-6a6e8fd97387",
        "3bfb58cd-7892-48cc-8020-2f17e6de6e7f",
        "313628f1-68b8-460d-84f6-cec7a8796ef2",
        "816a59f3-f5ae-4ccd-9b23-82aa8c23d33c",
        "df8184cc-3694-4549-8c8c-6b5171877376",
        "5e6ef132-4d7c-4730-8c7f-85aa4082588f"
    ]
}

# Tạo DataFrame
df = pd.DataFrame(data)

# Chuẩn hóa kiểu dữ liệu
df["event_time"] = pd.to_datetime(df["event_time"])

# Làm sạch nhẹ (rất quan trọng khi visualize)
df["brand"] = df["brand"].fillna("unknown")
df["category_code"] = df["category_code"].fillna("unknown")

# (Optional) thêm cột giá log để vẽ đẹp hơn
df["price_log"] = df["price"].apply(lambda x: round(x, 2))