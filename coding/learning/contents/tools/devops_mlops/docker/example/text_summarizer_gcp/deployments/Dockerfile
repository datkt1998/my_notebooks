# Sử dụng Python 3.8 slim
FROM python:3.8-slim

# Đặt thư mục làm việc
WORKDIR /app

# Sao chép requirements.txt và cài đặt các thư viện
COPY requirements.txt .
RUN pip install -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Lệnh chạy ứng dụng Streamlit
CMD ["streamlit", "run", "apps/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
