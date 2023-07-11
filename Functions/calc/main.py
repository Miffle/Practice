
from bot_components.tg_bot_register import bot
from bot_components.keyboard.StartKeyboard import keyboard,startKeyboard

value =''
old_value=''
def getMessage(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def computing(query):
    global  value,old_value
    data = query.data
    if data == 'no':
        pass
    elif data == 'C':
        value = ''
    elif data == '<=':
        if value !='':
            value = value[:len(value) - 1]
    elif data == '=':
        try:
            value = str(eval(value))
        except:
            value = 'Ошибка!'
    elif data == '^':
        value += '**'
    elif data == 'закрыть':
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='Ответ:'+value)
        value = ''
        bot.send_message(query.message.chat.id, 'Возврат к главному меню', reply_markup=startKeyboard)
        bot.clear_step_handler_by_chat_id(query.message.chat.id)
        bot.edit_message_reply_markup(chat_id=query.message.chat.id, message_id=query.message.message_id, reply_markup=None)




    else:
        value+=data
    if (value != old_value and value!='') or (value != old_value and value ==''):
        if value =='':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,text='0',reply_markup=keyboard)
            old_value='0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,text=value,reply_markup=keyboard)
            old_value=value
    old_value=value
    if value == 'Ошибка!':
        value = ''



