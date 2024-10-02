
FROM tiangolo/uvicorn-gunicorn:python3.11-slim

WORKDIR /app

COPY main.py ./main.py
COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./requirements.txt

EXPOSE 8080
CMD ["python", "main.py"]
