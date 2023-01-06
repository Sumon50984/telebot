from ..bot import app
from pyrogram import filters
import asyncio

@app.on_message(filters.command("add", "*") & filters.me)
async def file_adder(app, message):
   replied = message.reply_to_message
   if not replied or not replied.document:
       return await message.edit("Reply to a message where have the file!")
   file = replied.document.file_name
   path = f"{message.command[1]}/{file}"
   try:
      await replied.download(file_name=path)
      await message.edit(f"file added to {path}")
   except Exception as e:
      await message.edit(f"{e}")
   await asyncio.sleep(3)
   await message.delete()
