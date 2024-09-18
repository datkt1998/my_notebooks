# AI Text Summarizer Development and Deployment Guide 

Xây dựng và triển khai một mô hình AI có khả năng tóm tắt văn bản (text summarization). Chúng ta sẽ phát triển mô hình trên môi trường cục bộ, sau đó đóng gói mô hình bằng Docker và triển khai nó lên Google Cloud Platform (GCP) với Vertex AI. Các bước chi tiết bao gồm:

1. **Phát triển mô hình tóm tắt văn bản AI cục bộ**: Thiết lập môi trường phát triển, xây dựng mô hình, tích hợp với BigQuery và tạo giao diện với Streamlit.
2. **Đóng gói mô hình**: Tạo file `requirements.txt`, xây dựng Docker image và kiểm tra cục bộ.
3. **Triển khai mô hình lên GCP**: Đẩy Docker image lên Google Artifact Registry và triển khai mô hình với Vertex AI.<a name="service-overview"></a>

**Cấu trúc folder**
```bash
text-summarizer-project/
│
├── app.py                    # Ứng dụng chính sử dụng Streamlit để tương tác người dùng
├── Dockerfile                # File để đóng gói ứng dụng vào Docker
├── requirements.txt          # Liệt kê các thư viện cần thiết cho project
├── summarizer/               # Thư mục chứa mã nguồn cho mô hình tóm tắt văn bản và các tiện ích liên quan
│   ├── __init__.py           # File khởi tạo cho module
│   ├── model.py              # Mô hình tóm tắt văn bản
│   ├── bigquery_utils.py      # Tương tác với BigQuery
│   └── config.py             # Các cấu hình dự án
└── logs/                     # Thư mục lưu trữ các file log (nếu cần thiết)

```
## Phát triển mô hình
### 2.1. Thiết lập môi trường phát triển

Trước tiên, chúng ta cần thiết lập môi trường phát triển. Các bước chính bao gồm cài đặt các thư viện cần thiết và chuẩn bị môi trường lập trình:

Theo **virtualenv**
```bash
# Tạo môi trường ảo
python3 -m venv venv

# Kích hoạt môi trường ảo
source venv/bin/activate

# Cài đặt các thư viện cần thiết
pip install transformers torch streamlit google-cloud-bigquery
```

Theo **conda**
```bash
# Tạo môi trường ảo
conda create -n venv python=3.9

# Kích hoạt môi trường ảo
conda activate venv

# Cài đặt các thư viện cần thiết
conda install transformers torch streamlit google-cloud-bigquery
```