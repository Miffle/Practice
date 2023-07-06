from googletrans import Translator

import DBase.commands_insert
from bot_components.bot_register import bot
from bot_components.keyboard.StartKeyboard import startKeyboard


def translating(message):
    translator = Translator()
    text = message.text
    translated_text = translator.translate(text=text).text
    if len(message.text) < 3000:
        reply_text = f"Вот перевод: {translated_text}"
        bot.send_message(message.chat.id, reply_text, reply_markup=startKeyboard)
    else:
        reply_text = "Текст слишком большой, уменьши его"
        bot.send_message(message.chat.id, reply_text, reply_markup=startKeyboard)
    DBase.commands_insert.command_inserting(message, "Перевод", reply_text)
