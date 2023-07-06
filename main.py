import weather.main
from bot_components.bot_register import bot
from bot_components.keyboard.StartKeyboard import startKeyboard
import calc.main
from bot_components.keyboard.ButtonsText import *


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет", reply_markup=startKeyboard)


@bot.message_handler(content_types=['text'])
def start_keyboard_answer(message):
    text = message.text
    if text == calcBtnText:
        msg = bot.send_message(message.chat.id, "Введи пример в формате - {1} {знак} {2}")
        bot.register_next_step_handler(msg, calc.main.computing)
    elif text == weatherBtnText:
        msg = bot.send_message(message.chat.id, "Введи название города")
        bot.register_next_step_handler(msg, weather.main.weather_searching)


bot.infinity_polling()
