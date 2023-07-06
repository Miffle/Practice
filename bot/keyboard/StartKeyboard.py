from telebot import types

startKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

calcBtn = types.KeyboardButton(text="Калькулятор")
weatherBtn = types.KeyboardButton(text="Посмотреть погоду")
translateBtn = types.KeyboardButton(text="Перевести текст")
memeBtn = types.KeyboardButton(text="Какой-то мем")

startKeyboard.add(calcBtn, weatherBtn, translateBtn, memeBtn)
