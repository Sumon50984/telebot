from pyrogram import filters
from ..bot import bot, app
import feedparser
import asyncio
import re
import requests

# Simple script to read a rss page 

@bot.on_message(filters.command("feeds"))
def rss(bot, message):
    url = message.command[1]
    cr = re.compile("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    if not re.search(cr, url):
        return message.reply_text("Unvalid link")
    
    response = requests.get(url)

    if not response.status_code == 200:
        return message.reply_text(f"Error: {response.status_code}")

    parser = feedparser.parse(url)
    print(url, parser)
    for feeds in parser['entries']:
        message.reply_text(f"<a href={feeds.link}>{feeds.title}</a>\n`{feeds.summary}")

# For userbots

@app.on_message(filters.command("feeds", "*") & filters.me)
def rss(app, message):
    url = message.command[1]
    cr = re.compile("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +                                  "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
    if not re.search(cr, url):
        return message.edit("Unvalid link")

    response = requests.get(url)

    if not response.status_code == 200:
        return message.edit(f"Error: {response.status_code}")
    
    parser = feedparser.parse(url)
    
    for feeds in parser['entries']:
        message.reply_text(f"<a href={feeds.link}>{feeds.title}</a>\n`{feeds.summary}")
    message.delete()

@bot.on_message(filters.command("test"))
@app.on_message(filters.command("test", "*") & filters.me)
async def test(app, message):
        await message.reply_text("Working")
        await asyncio.sleep(3)
        await message.delete()
