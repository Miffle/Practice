from googletrans import Translator

import bot_components.reply
from bot_components.keyboard.ButtonsText import backwardsBtnText


def translating(message):
    command = "Перевод"
    translator = Translator()
    text = message.text
    language = translator.detect(text).lang
    if language == "en":
        dest = 'ru'
        translated_text = translator.translate(text=text, dest=dest).text
    else:
        translated_text = translator.translate(text=text).text

    if message.text == backwardsBtnText:
        reply_text = 'возврат к главному меню'
    elif len(message.text) < 3000:
        reply_text = f"Вот перевод: {translated_text}"
    else:
        reply_text = "Текст слишком большой, уменьши его"
    bot_components.reply.reply(message, reply_text, command)
