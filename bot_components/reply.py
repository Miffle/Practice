from bot_components.tg_bot_register import bot
from bot_components.keyboard.StartKeyboard import startKeyboard
import DBase.commands_insert


def reply(message, reply_text, command):
    bot.send_message(message.chat.id, reply_text, reply_markup=startKeyboard, parse_mode="HTML")
    DBase.commands_insert.command_inserting(message, command, reply_text)
