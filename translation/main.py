from googletrans import Translator
from bot_components.bot_register import bot
from bot_components.keyboard.StartKeyboard import startKeyboard


def translating(message):
    translator = Translator()
    text = message.text
    translated_text = translator.translate(text=text).text
    info = f"Вот перевод: {translated_text}"
    if len(info) > 4096:
        for x in range(0, len(info), 4096):
            bot.send_message(message.chat.id, info[x:x + 4096], reply_markup=startKeyboard)
    else:
        bot.send_message(message.chat.id, info, reply_markup=startKeyboard)
