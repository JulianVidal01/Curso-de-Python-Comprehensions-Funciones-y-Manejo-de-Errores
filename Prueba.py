import re
import random
import requests

def find_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&units=metric&APPID=d3b3cec9ac3b9a9b3c6a70d3a3f6d10e"
    response = requests.get(url)
    data = response.json()
    if data["cod"] != "404":
        # print(data)
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        return "The temperature in {} is {} degree Celsius and the weather is {}".format(city, temp, weather)
    else:
        return "City not found!"

def chatbot_response(user_input):
    user_input = user_input.lower()
    if re.search("weather", user_input):
        city = user_input.replace("what's the weather in ", "")
        return find_weather(city)
    elif re.search