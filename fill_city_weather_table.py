import os
import psycopg2

from dotenv import load_dotenv
from weather_app.config import (
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


load_dotenv()


DOCKER_DB_HOST = os.getenv('DOCKER_DB_HOST')
DOCKER_DB_OUT_PORT = os.getenv('DOCKER_DB_OUT_PORT')


new_cities = [
            ('Minsk', 25, 'Clouds'),
            ('Mogilev', 20, 'Rain'),
            ('Rome', 28, 'Sunny'),
            ('Tokyo', 22, 'Clouds'),
            ('Antalya', 30, 'Sunny'),
            ('Mexico', 33, 'Sunny'),
            ('London', 20, 'Rain'),
        ]

try:
    conn = psycopg2.connect(
        host=DOCKER_DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DOCKER_DB_OUT_PORT
    )
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO city_weather (city_name, temp, datetime, weather) VALUES (%s, %s, now(), %s)",
        new_cities
    )
    conn.commit()
    print("Successfully inserted db test data")


except Exception as ex:
    print("[INFO] error", ex)
finally:
    if conn:
        cursor.close()
        conn.close()
