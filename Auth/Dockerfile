FROM python:3.12-slim

WORKDIR /auth
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Запуск скрипта для генерации ключей
RUN python generate_keys.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
