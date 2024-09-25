FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

WORKDIR /app

COPY main.py ./main.py
COPY requirements.txt ./requirements.txt
COPY models ./models

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./requirements.txt

EXPOSE 8080
CMD ["python", "main.py"]