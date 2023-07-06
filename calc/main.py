from bot_components.bot_register import bot
from bot_components.keyboard.StartKeyboard import startKeyboard


def computing(msg):
    splited_message = msg.text.split(" ")
    try:
        first_number = int(splited_message[0])
        second_number = int(splited_message[2])
    except ValueError:
        bot.send_message(msg.chat.id, "Ожидались цифорки, жми на кнопку Калькулятор", reply_markup=startKeyboard)
        return
    sign = splited_message[1]

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
            bot.send_message(msg.chat.id, "Я не знаю такой знак, жми на кнопку Калькулятор", reply_markup=startKeyboard)
            return
        try:
            bot.send_message(msg.chat.id, f"Результат вычисления: <b>{result}</b>", reply_markup=startKeyboard, parse_mode="HTML")
        except ValueError:
            bot.send_message(msg.chat.id, "Слишком большое число получается, бери меньше",
                             reply_markup=startKeyboard)
    except ZeroDivisionError:
        bot.send_message(msg.chat.id, "Нельзя так, деление на ноль запрещено, жми на кнопку Калькулятор", reply_markup=startKeyboard)