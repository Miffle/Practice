import Functions.calc.main
import Functions.memes.main
import Functions.translation.main
import Functions.weather.main
import bot_components.reply
from bot_components.keyboard.ButtonsText import *
from bot_components.keyboard.StartKeyboard import startKeyboard, newKeyboard, keyboard
from bot_components.tg_bot_register import bot


@bot.message_handler(commands=["start"])
def start(message):
    reply_text = "Привет я недоБОТ, там есть кнопка INFO внизу, почитай"
    bot_components.reply.reply(message, reply_text, "/start")


@bot.message_handler(content_types=['text'])
def menu(message):
    text = message.text
    if text == calcBtnText:
        msg = bot.send_message(message.chat.id, '_', reply_markup=keyboard)
        bot.register_next_step_handler(msg, Functions.calc.main.computing)
    elif text == weatherBtnText:
        msg = bot.send_message(message.chat.id, "Введи название города", reply_markup=newKeyboard)
        bot.register_next_step_handler(msg, Functions.weather.main.weather_searching)
    elif text == translateBtnText:
        msg = bot.send_message(message.chat.id, "Какую фразу будем переводить?", parse_mode="HTML",
                               reply_markup=newKeyboard)
        bot.register_next_step_handler(msg, Functions.translation.main.translating)
    elif text == memeBtnText:
        Functions.memes.main.meme_sending(message)
    elif text == infoBtnText:
        bot.send_message(message.chat.id, info_text, reply_markup=startKeyboard)
    else:
        bot.send_message(message.chat.id, "Я не знаю такую команду, нажимай на кнопки снизу",
                         reply_markup=startKeyboard)


bot.infinity_polling()
