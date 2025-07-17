FROM python:3.12-slim-bookworm

WORKDIR /app/

COPY ./weather_app/ ./weather_app/
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python3", "weather_app/main.py"]