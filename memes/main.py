from memes.REDDIT_INFO import reddit
from bot_components.bot_register import bot
from bot_components.keyboard.StartKeyboard import startKeyboard
import DBase.commands_insert


def meme_getting():
    subred1 = reddit.subreddit("ProgrammerHumor")
    meme = subred1.top("day", limit=20)
    for submission in meme:
        url = submission.url
        if url.endswith("jpg") or url.endswith("png") or url.endswith("jpeg"):
            return {"url": url,
                    "type": "photo"}
        elif url.endswith("gif"):
            return {"url": url,
                    "type": "gif"}


def meme_sending(message):
    meme = meme_getting()
    if meme['type'] == "photo":
        bot.send_photo(message.chat.id, photo=meme["url"], caption="Мем дня", reply_markup=startKeyboard)
    else:
        bot.send_animation(message.chat.id, photo=meme["url"], caption="Мем дня", reply_markup=startKeyboard)
    DBase.commands_insert.command_inserting(message, "Какой-то мем", meme["url"])
   