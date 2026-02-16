FROM python:3.11-slim

WORKDIR /app
RUN mkdir -p /output

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["python", "main.py"]
