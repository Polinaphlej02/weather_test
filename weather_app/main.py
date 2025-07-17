from re import fullmatch
from flask import Flask, render_template, request, flash

from api import get_weather
from config import FLASK_SECRET_KEY
from database import insert_data, get_weather_data


app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        city = request.form['city'].strip()
        if fullmatch(r'^[a-zA-Z\- ]+$', city):

            if get_weather(city) != "City not found":
                weather, temp, humidity, icon_url = get_weather(city)
                insert_data(city.capitalize(), weather, temp)
                weather = {'city': city.capitalize(),
                           'temp': temp,
                           'weather': weather,
                           'humidity': humidity,
                           'icon_url': icon_url}
                return render_template('home.html', weather=weather)
        else:
            flash("Wrong city name")
        return render_template('home.html')
    return render_template('welcome.html')


@app.route("/search-history",methods=['POST', 'GET'])
def history():
    weather_list = get_weather_data()

    return render_template("history.html", weather_list=weather_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
