from bot_components.bot_register import bot
from bot_components.keyboard.StartKeyboard import startKeyboard
import requests
import DBase.commands_insert


def weather_searching(message):
    city = message.text
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    weather_data = requests.get(url).json()
    if 'message' not in weather_data:
        weather_type = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        temperature_feels = weather_data['main']['feels_like']
        reply_text = f"В городе {message.text} {weather_type} -\nТемпература {temperature}°C\nОщущается, как {temperature_feels}°C"
        bot.send_message(message.chat.id, reply_text, reply_markup=startKeyboard)
    else:
        reply_text = "Город не найден"
        bot.send_message(message.chat.id, reply_text, reply_markup=startKeyboard)
    DBase.commands_insert.command_inserting(message, "Погода", reply_text)
