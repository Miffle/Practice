import praw
from bot_components.bot_register import bot
from bot_components.keyboard.StartKeyboard import startKeyboard

reddit = praw.Reddit(
    user_agent="zalupa",
    client_id='zD7n3UGqEBpZ5qbJ4gtrvA',
    client_secret='ofyOJW9WJfOdmEjKI6MzTHGsEyi5YQ')


def meme_getting():
    subred1 = reddit.subreddit("ProgrammerHumor")
    meme = subred1.top("day", limit=5)
    for submission in meme:
        url = submission.url
        if url.endswith("jpg") or url.endswith("png") or url.endswith("jpeg"):
            return url


def meme_sending(message):
    bot.send_photo(message.chat.id, photo=meme_getting(), caption="Мем дня", reply_markup=startKeyboard)
