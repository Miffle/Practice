import Functions.memes.main
import Functions.translation.main
import Functions.weather.main
from bot_components.tg_bot_register import bot
from bot_components.keyboard.StartKeyboard import startKeyboard,newKeyboard,keyboard
import Functions.calc.main
from bot_components.keyboard.ButtonsText import *
import bot_components.reply



@bot.message_handler(commands=["start"])
def start(message):
    reply_text = "Привет я недоБОТ"
    bot_components.reply.reply(message, reply_text, "/start")
    bot.reply_to(message,"Выберите действие используя клавиатуру:", reply_markup=startKeyboard)

info_text="Я недоБОТ\n" \
    "Созданный @I_am_still_right_here и @brizzy_9\n"\
        "Могу посчитать на калькуляторе\nСообщить погоду в выбранном населенном пункте\n"\
    "Перевести предложение на английский язык\nПоказать мем дня для IT\n"


@bot.message_handler(content_types=['text'])
def start_keyboard_answer(message):
    text = message.text
    if text == calcBtnText:
        msg = bot.send_message(message.chat.id, '_',reply_markup=keyboard)
        bot.register_next_step_handler(msg, Functions.calc.main.computing)
    elif text == weatherBtnText:
        msg = bot.send_message(message.chat.id, "Введи название города")
        bot.register_next_step_handler(msg, Functions.weather.main.weather_searching)
    elif text == translateBtnText:
        msg = bot.send_message(message.chat.id, "Какую фразу перевести на <b>английский</b>?", parse_mode="HTML")
        bot.register_next_step_handler(msg, Functions.translation.main.translating)
    elif text == memeBtnText:
        Functions.memes.main.meme_sending(message)
    elif text == infoBtnText:
        bot.send_message(message.chat.id, info_text, reply_markup=startKeyboard)
    else:
        bot.send_message(message.chat.id, "Я не знаю такую команду, нажимай на кнопки снизу", reply_markup=startKeyboard)


bot.infinity_polling()
