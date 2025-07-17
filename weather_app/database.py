import os.path

import psycopg2

from psycopg2.extras import RealDictCursor
from config import (
    DB_HOST,
    DB_NAME,
    DB_USER,
    DB_PORT,
    DB_PASSWORD
)


def get_weather_data():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT
        )
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM city_weather ORDER BY id DESC")
        weather_list = cursor.fetchall()

        return weather_list
    except Exception as ex:
        print("[INFO] error", ex)
    finally:
        if conn:
            cursor.close()
            conn.close()


def insert_data(city, weather, temp):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT
        )

        cursor = conn.cursor()
        cursor.execute("INSERT INTO city_weather (city_name, temp, datetime, weather) VALUES (%s, %s, now(), %s)",
                       (city, temp, weather))
        conn.commit()
    except Exception as ex:
        print("[INFO] error", ex)
    finally:
        if conn:
            cursor.close()
            conn.close()
