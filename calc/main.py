import bot_components.reply

def spliting(msg):
    splited_message = msg.text.split(" ")
    try:
        first_number = int(splited_message[0])
        second_number = int(splited_message[2])
    except ValueError:
        reply_text = "Ожидались цифорки, жми на кнопку Калькулятор"
        bot_components.reply.reply(msg, reply_text, "Калькулятор")
        return
    sign = splited_message[1]
    return first_number, second_number, sign


def computing(msg):
    first_number, second_number, sign = spliting(msg)
    command = "Калькулятор"
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
            bot_components.reply.reply(msg, reply_text, command)
            return
        try:
            reply_text = f"Результат вычисления: <b>{result}</b>"
            bot_components.reply.reply(msg, reply_text, command)
        except ValueError:
            reply_text = "Слишком большое число получается, бери меньше"
            bot_components.reply.reply(msg, reply_text, command)
    except ZeroDivisionError:
        reply_text = "Нельзя так, деление на ноль запрещено, жми на кнопку Калькулятор"
        bot_components.reply.reply(msg, reply_text, command)
