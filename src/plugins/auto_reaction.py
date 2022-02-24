from ..bot import app
from pyrogram import filters

@app.on_message(filters.group)
async def reaction(app, message):
   chat_id = int("-1001274256730")
   message_id = message.message_id
   await app.send_reaction(chat_id, message_id, "")
