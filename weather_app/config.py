import os
from dotenv import load_dotenv


load_dotenv()

current_directory = os.path.dirname(os.path.abspath(__file__))

DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

DB_TABLES_FOLDER = os.path.join(current_directory, 'sql', 'tables')

FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
