from bot_components.bot_register import bot
import requests


def weather_searching(message):
    city = message.text
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    weather_data = requests.get(url).json()
    print(weather_data)
    if 'message' not in weather_data:
        weather_type = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        temperature_feels = weather_data['main']['feels_like']

        bot.send_message(message.chat.id, f"В городе {message.text} {weather_type} -\n"
                                          f"Температура - {temperature}°C\n"
                                          f"Ощущается, как - {temperature_feels}°C\n")
    else:
        bot.send_message(message.chat.id, "Город не найден")
