import requests

import bot_components.keyboard.StartKeyboard
import bot_components.reply
from bot_components.keyboard.ButtonsText import backwardsBtnText


def weather_searching(message):
    command = "Погода"
    city = message.text
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    weather_data = requests.get(url).json()
    if 'message' not in weather_data:
        weather_type = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        temperature_feels = weather_data['main']['feels_like']
        wind = weather_data["wind"]["speed"]
        reply_text = f"В городе {message.text} {weather_type} -\nТемпература {temperature}°C\nОщущается, как {temperature_feels}°C\nВетер:{wind} м/с"
    elif message.text == backwardsBtnText:
        reply_text = 'возврат к главному меню'
    else:
        reply_text = "Город не найден"
    bot_components.reply.reply(message, reply_text, command)
