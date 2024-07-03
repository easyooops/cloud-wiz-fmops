FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY src/backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/backend/ .

CMD ["uvicorn", "app.main:create_app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--loop", "asyncio"]