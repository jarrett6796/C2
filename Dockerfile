FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app
RUN pip install --no-cache-dir \
    fastapi==0.111.1 \
    uvicorn[standard]==0.30.0
COPY . .
CMD ["python","main.py"]
