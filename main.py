from bot.bot_register import bot
from bot.keyboard.StartKeyboard import startKeyboard
import calc.main


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет", reply_markup=startKeyboard)


@bot.message_handler(content_types=['text'])
def start_keyboard_answer(message):
    text = message.text
    if text == "Калькулятор":
        msg = bot.send_message(message.chat.id, "Введи пример в формате - {1} {знак} {2}")
        bot.register_next_step_handler(msg, calc.main.computing)


bot.infinity_polling()
