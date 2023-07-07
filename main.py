import memes.main
import translation.main
import weather.main
from bot_components.tg_bot_register import bot
from bot_components.keyboard.StartKeyboard import startKeyboard
import calc.main
from bot_components.keyboard.ButtonsText import *
import bot_components.reply


@bot.message_handler(commands=["start"])
def start(message):
    reply_text = "Привет"
    bot_components.reply.reply(message, reply_text, "/start")


@bot.message_handler(content_types=['text'])
def start_keyboard_answer(message):
    text = message.text
    if text == calcBtnText:
        msg = bot.send_message(message.chat.id, "Введи пример в формате - {1} {знак} {2}")
        bot.register_next_step_handler(msg, calc.main.computing)
    elif text == weatherBtnText:
        msg = bot.send_message(message.chat.id, "Введи название города")
        bot.register_next_step_handler(msg, weather.main.weather_searching)
    elif text == translateBtnText:
        msg = bot.send_message(message.chat.id, "Какую фразу перевести на <b>английский</b>?", parse_mode="HTML")
        bot.register_next_step_handler(msg, translation.main.translating)
    elif text == memeBtnText:
        memes.main.meme_sending(message)
    else:
        bot.send_message(message.chat.id, "Я не знаю такую команду, нажимай на кнопки снизу",
                         reply_markup=startKeyboard)


bot.infinity_polling()
