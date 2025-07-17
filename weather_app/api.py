import requests


api_key = "f3d7f69a289d841467c7f75bbf12ec32"
base_url = "https://api.openweathermap.org/data/2.5/weather?q="


def get_weather(city_name):
    complete_url = base_url + city_name + '&APPID=' + api_key
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        weather = x["weather"][0]["main"]
        temp = round(x["main"]["temp"] - 273)
        humidity = x["main"]["humidity"]
        icon = x["weather"][0]["icon"]
        icon_url = "http://openweathermap.org/img/w/" + icon + ".png"
        return weather, temp, humidity, icon_url
    else:
        return "City not found"
