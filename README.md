# Weather test task

## Description
This app allows users to enter a city name, fetch current weather data from a public API, and store the query history. It`s implemented as a test task.

## Setup instructions
1. Install all requirements locally:\
`pip install -r requirements.txt`
2. Copy .env.example content into .env file:\
`cp .env.example .env`
3. Fill empty .env file fields
4. Build docker image using the following command:\
`docker build -t weather_app .`
5. Run docker compose up command:\
`docker-compose up -d`
6. \* If you are running this app for the first time you have to create empty project tables:\
`python create_tables_script.py`
7. \* To fill db table with test data use the following command:
`python fill_city_weather_table.py`
8. To turn off the app use the following command:\
`docker-compose down`