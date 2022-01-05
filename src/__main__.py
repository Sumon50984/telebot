from .bot import bot, app
from pyrogram import idle, Client

if __name__ == "__main__":
  app.start()
  bot.start()
  idle()
