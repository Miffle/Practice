import sqlite3


def command_inserting(msg, command, reply_message_text):
    dbase = sqlite3.connect("A:\\Projects\\PycharmProjects\\practica\\identifier.sqlite")
    cursor = dbase.cursor()
    from_user_id = msg.chat.id
    user_message_text = msg.text
    cursor.execute("INSERT INTO commands (user_id, used_command, user_text, reply_text) VALUES (?,?,?,?)",
                   (from_user_id, command, user_message_text, reply_message_text))
    dbase.commit()
    dbase.close()
