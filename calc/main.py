from bot_components.bot_register import bot
from bot_components.keyboard.StartKeyboard import startKeyboard
import DBase.commands_insert


def spliting(msg):
    splited_message = msg.text.split(" ")
    try:
        first_number = int(splited_message[0])
        second_number = int(splited_message[2])
    except ValueError:
        reply_text = "Ожидались цифорки, жми на кнопку Калькулятор"
        bot.send_message(msg.chat.id, reply_text, reply_markup=startKeyboard)
        DBase.commands_insert.command_inserting(msg, "Калькулятор", reply_text)
        return
    sign = splited_message[1]
    return first_number, second_number, sign


def computing(msg):
    first_number, second_number, sign = spliting(msg)
    try:
        if sign == "+":
            result = first_number + second_number
        elif sign == "-":
            result = first_number - second_number
        elif sign == "*":
            result = first_number * second_number
        elif sign == "/":
            result = first_number / second_number
        elif sign == "^":
            result = first_number ** second_number
        else:
            reply_text = "Я не знаю такой знак, жми на кнопку Калькулятор"
            bot.send_message(msg.chat.id, reply_text, reply_markup=startKeyboard)
            DBase.commands_insert.command_inserting(msg, "Калькулятор", reply_text)
            return
        try:
            reply_text = f"Результат вычисления: <b>{result}</b>"
            bot.send_message(msg.chat.id, reply_text, reply_markup=startKeyboard,
                             parse_mode="HTML")
            DBase.commands_insert.command_inserting(msg, "Калькулятор", reply_text)
        except ValueError:
            reply_text = "Слишком большое число получается, бери меньше"
            bot.send_message(msg.chat.id, reply_text, reply_markup=startKeyboard)
            DBase.commands_insert.command_inserting(msg, "Калькулятор", reply_text)
    except ZeroDivisionError:
        reply_text = "Нельзя так, деление на ноль запрещено, жми на кнопку Калькулятор"
        bot.send_message(msg.chat.id, reply_text,
                         reply_markup=startKeyboard)
        DBase.commands_insert.command_inserting(msg, "Калькулятор", reply_text)
