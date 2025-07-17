import os
import psycopg2

from dotenv import load_dotenv
from weather_app.config import (
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_TABLES_FOLDER
)


load_dotenv()


DOCKER_DB_HOST = os.getenv('DOCKER_DB_HOST')
DOCKER_DB_OUT_PORT = os.getenv('DOCKER_DB_OUT_PORT')


def create_weather_table():
    try:
        conn = psycopg2.connect(
            host=DOCKER_DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DOCKER_DB_OUT_PORT
        )

        cursor = conn.cursor()

        with open(os.path.join(DB_TABLES_FOLDER, 'city_weather.sql'), 'r') as f:
            create_table_query = f.read()
            cursor.execute(create_table_query)
            conn.commit()
            print("Successfully created db tables")
    except Exception as ex:
        print("[INFO] error", ex)
    finally:
        if conn:
            cursor.close()
            conn.close()


if __name__ == '__main__':
    create_weather_table()