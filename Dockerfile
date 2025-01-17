FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопировать всё приложение, включая wait-for-it.sh (должен лежать в корне или где-то рядом)
COPY . .

EXPOSE 8000