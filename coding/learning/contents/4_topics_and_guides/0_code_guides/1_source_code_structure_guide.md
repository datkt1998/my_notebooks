# Cấu trúc source code

**Khi tổ chức cấu trúc thư mục:**
- *Tách biệt mã nguồn và dữ liệu*: Đảm bảo dữ liệu, mã nguồn và các file kết quả luôn được tổ chức trong các thư mục riêng biệt.
- *Sử dụng notebooks cho khám phá*: Đặt các file notebook vào một thư mục riêng để tránh xung đột với mã nguồn chính.
- *Quản lý các bước xử lý dữ liệu*: Đặt các file xử lý dữ liệu vào thư mục riêng, tránh lẫn lộn với các phần khác như training mô hình.

```bash

project_name/
│
├── docs/                    # Tài liệu mô hình/dự án và tài liệu tham khảo, links, v.v.
│   └── references/          # Tài liệu tham khảo, links, v.v.
│   └── materials/           # Tài liệu mô hình/dự án
│   └── reports/             # Báo cáo, kết quả phân tích (PDF, HTML, etc.)
│
├── config/                  # Cấu hình dự án (hyperparameters, settings, etc.)
│   └── config.yaml          # Cấu hình bằng YAML
│
├── data/                    # Dữ liệu thô và dữ liệu đã xử lý
│   ├── external/            # Dữ liệu từ nguồn bên ngoài (không có update khi chạy production)
│   ├── raw/                 # Dữ liệu gốc (dữ liệu input khi model chạy production)
│   ├── interim/             # Dữ liệu trung gian trong quá trình xử lý
│   ├── processed/           # Dữ liệu đã được xử lý
│   └── features/            # (optional) Dữ liệu features được được tạo ra (chỉ lưu trong quá trình dev model, không export ra file khi run model in production)
│
├── notebooks/               # Các file notebook Jupyter
│
├── src/                     # Mã nguồn chính của dự án
│   ├── __init__.py          # File init để biến src thành module
│   ├── data/                # Xử lý dữ liệu
│   │   └── loader.py        # Hàm tải dữ liệu
│   ├── features/            # Xử lý đặc trưng dữ liệu
│   │   └── features.py      # Trích xuất và xử lý đặc trưng
│   ├── models/              # Mô hình machine learning/AI
│   │   ├── model.py         # Định nghĩa mô hình
│   │   ├── train.py         # Training mô hình
│   │   └── evaluate.py      # Đánh giá mô hình
│   ├── visualization/       # Các hàm trực quan hóa dữ liệu
│   │   └── visualization.py 
│   └── utils/               # Các hàm tiện ích, helpers
│       └── utils.py
│
├── tests/                   # Các bài test để kiểm tra module
│   └── test_model.py
│
├── output/                  # Kết quả dự đoán và các file output khác
│
├── logs/                    # File log (trong quá trình training)
│
├── scripts/                 # Các script để chạy training, inference
│   └── run_training.py      # Script chạy mô hình
│
├── models/                  # Mô hình đã được lưu lại
│ 
├── deployments/             # Tài liệu triển khai (Docker, GCP, etc.)
│   ├── Dockerfile           # Dockerfile để container hóa ứng dụng
│   ├── docker-compose.yml   # File docker-compose (nếu sử dụng nhiều container)
│   ├── gcp_deployment.yaml  # Cấu hình cho việc deploy lên GCP Vertex AI
│   ├── cloud/               # Scripts liên quan đến cloud deployment
│   │   ├── vertex_ai.py     # Script triển khai lên Vertex AI
│   │   └── cloudbuild.yaml  # Cấu hình Cloud Build trên GCP
│   └── kubernetes/          # File để triển khai trên Kubernetes (nếu sử dụng)
│       ├── deployment.yaml  # Cấu hình triển khai trên Kubernetes
│       └── service.yaml     # Cấu hình dịch vụ trên Kubernetes
│ 
├── apps/                    # Giao diện tương tác
│   └── app.py               # Ứng dụng chính sử dụng Streamlit hoặc gì đó để tương tác người dùng
│
│
├── .gitignore               # File gitignore để bỏ qua các file không cần commit
├── environment.yml          # Môi trường Anaconda/Conda (nếu dùng)
├── requirements.txt         # Thư viện cần thiết cho dự án
├── README.md                # Thông tin dự án
├── main.py                  # Script chạy chính của model
└── setup.py                 # Cài đặt dự án thành package Python (nếu cần)

```

CODE PYTHON để gen structure theo template trên

```python
import os

# Định nghĩa cấu trúc thư mục và tệp
structure = {
    "docs": {
        "references": {},
        "materials": {},
        "reports": {},
    },
    "config": {
        "config.yaml": None,
    },
    "data": {
        "external": {},
        "raw": {},
        "interim": {},
        "processed": {},
        "features": {},
    },
    "notebooks": {},
    "src": {
        "__init__.py": None,
        "data": {
            "loader.py": None,
        },
        "features": {
            "features.py": None,
        },
        "models": {
            "model.py": None,
            "train.py": None,
            "evaluate.py": None,
        },
        "visualization": {
            "visualization.py": None,
        },
        "utils": {
            "utils.py": None,
        },
    },
    "tests": {
        "test_model.py": None,
    },
    "output": {},
    "logs": {},
    "scripts": {
        "run_training.py": None,
    },
    "models": {},
    "deployments": {
        "Dockerfile": None,
        "docker-compose.yml": None,
        "gcp_deployment.yaml": None,
        "cloud": {
            "vertex_ai.py": None,
            "cloudbuild.yaml": None,
        },
        "kubernetes": {
            "deployment.yaml": None,
            "service.yaml": None,
        },
    },
	"apps": {
        "app.py": None,
    },
    ".gitignore": None,
    "environment.yml": None,
    "requirements.txt": None,
    "README.md": None,
    "setup.py": None,
    "main.py": None,
} 

# Hàm tạo cấu trúc thư mục và tệp
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if content is None:
			if not os.path.exists(path):
				open(path, "w").close()  # Tạo file trống
        else:
            # Nếu content không phải là None, tạo thư mục và đệ quy
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
            create_structure(path, content)

# Thư mục gốc của dự án
base_project_path = "."

# Tạo cấu trúc thư mục và tệp
create_structure(base_project_path, structure)
print("Structure for project created successfully!")
```