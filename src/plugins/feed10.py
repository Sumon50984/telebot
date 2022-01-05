from pyrogram import filters
from ..bot import bot, app
import feedparser


@app.on_message(filters.command("feed"))
def rss(Bot, message):
  try:
    c = message.command
    feed = feedparser.parse(c[1])
    # lmao we can't return loop
    a1 = feed.entries[0]
    a2 = feed.entries[1]
    a3 = feed.entries[2]
    a4 = feed.entries[3]
    a5 = feed.entries[4]
    a6 = feed.entries[5]
    a7 = feed.entries[6]
    a8 = feed.entries[7]
    a9 = feed.entries[8]
    a10 = feed.entries[9]

    message.reply_text(f"<a href={a1.link}>{a1.title}</a>\n`{a1.summary}`")
    message.reply_text(f"<a href={a2.link}>{a2.title}</a>\n`{a2.summary}`")
    message.reply_text(f"<a href={a3.link}>{a3.title}</a>\n`{a3.summary}`")
    message.reply_text(f"<a href={a4.link}>{a4.title}</a>\n`{a4.summary}`")
    message.reply_text(f"<a href={a5.link}>{a5.title}</a>\n`{a5.summary}`")
    message.reply_text(f"<a href={a6.link}>{a6.title}</a>\n`{a6.summary}`")
    message.reply_text(f"<a href={a7.link}>{a7.title}</a>\n`{a7.summary}`")
    message.reply_text(f"<a href={a8.link}>{a8.title}</a>\n`{a8.summary}`")
    message.reply_text(f"<a href={a9.link}>{a9.title}</a>\n`{a9.summary}`")
    message.reply_text(f"<a href={a10.link}>{a10.title}</a>\n`{a10.summary}`")
  except:
    return

@app.on_message(filters.command("test", "*") & filters.me)
async def test(app, message):
        await message.edit_text("Done")


@bot.on_message(filters.command("go") & filters.private)
async def go(bot, message):
        await message.reply_text("going!")
