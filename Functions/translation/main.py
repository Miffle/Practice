from googletrans import Translator
from langdetect import detect
import bot_components.reply


def translating(message):
    command = "Перевод"
    translator = Translator()
    src = 'en'
    dest = 'ru'
    text = message.text
    translated_text = translator.translate(message.text, src=src, dest=dest).text
    if len(message.text) < 3000:
        reply_text = f"Вот перевод: {translated_text}"
    else:
        reply_text = "Текст слишком большой, уменьши его"
    bot_components.reply.reply(message, reply_text, command)
