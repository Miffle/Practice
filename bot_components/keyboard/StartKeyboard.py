from telebot import types
from bot_components.keyboard.ButtonsText import *
startKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

calcBtn = types.KeyboardButton(text=calcBtnText)
weatherBtn = types.KeyboardButton(text=weatherBtnText)
translateBtn = types.KeyboardButton(text=translateBtnText)
memeBtn = types.KeyboardButton(text=memeBtnText)

startKeyboard.add(calcBtn, weatherBtn, translateBtn, memeBtn)
