import bot_components.reply


# TODO Переделать калькулятор

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
    if len(splited_message) == 3:
        return first_number, second_number, sign
    else:
        return


def computing(msg):
    command = "Калькулятор"
    try:
        first_number, second_number, sign = spliting(msg)
    except TypeError:
        reply_text = "Ожидались цифорки, жми на кнопку Калькулятор"
        bot_components.reply.reply(msg, reply_text, command)
        return
    try:
        match sign:
            case "+":
                result = first_number + second_number
            case "-":
                result = first_number - second_number
            case "*":
                result = first_number * second_number
            case "/":
                result = first_number / second_number
            case "^":
                result = first_number ** second_number
            case _:
                reply_text = "Я не знаю такой знак, жми на кнопку Калькулятор"
                bot_components.reply.reply(msg, reply_text, command)
                return
        try:
            reply_text = f"Результат вычисления: <b>{result}</b>"
        except ValueError:
            reply_text = "Слишком большое число получается, бери меньше"
    except ZeroDivisionError:
        reply_text = "Нельзя так, деление на ноль запрещено, жми на кнопку Калькулятор"
    bot_components.reply.reply(msg, reply_text, command)
