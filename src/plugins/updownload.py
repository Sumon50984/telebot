from pyrogram import filters
from ..bot import app
import asyncio
import os
from pySmartDL import SmartDL

dir = "DOWNLOADS/"
@app.on_message(filters.command("u", "*") & filters.me)
async def upload(app, message):
     if len(message.command)> 1:
        file = str(message.command[1])
        try:
           await app.send_document(
               document = file,
               caption = os.path.basename(file),
               chat_id = message.chat.id
           )
        except:
             await message.edit_text("File not found!")
             await asyncio.sleep(5)

     await message.delete()

@app.on_message(filters.command("d", "*") & filters.me)
async def download(app, message):
    if len(message.command) > 1:
       downloader = SmartDL(message.command[1], dir, progress_bar=False)
       downloader.start(blocking=False)
       while not downloader.isFinished():
          try:
             downloader.get_progress() * 100
          finally:
             return

       if downloader.isSuccessful():
             await message.edit("File downloaded")
             await asyncio.sleep(1)

    else:
         for e in downloader.get_errors():
            await message.edit(str(e))
            await asyncio.sleep(5)

    await message.delete()

@app.on_message(filters.command("up", "*") & filters.me)
async def downupload(app, message):
    if len(message.command)>1:
       downloader = SmartDL(message.command[1], dir, progress_bar=False)
       downloader.start(blocking=False)
       while not downloader.isFinished():
          try:
             downloader.get_progress() * 100
          finally:
             return

       if downloader.isSuccessful():
             await message.edit("File downloaded")
             await asyncio.sleep(1)
    else:
       for e in downloader.get_errors():
          await message.edit(str(e))
          await asyncio.sleep(2)

    await message.delete()

    file = downloader.get_dest()
    try:
       await app.send_document(
             document = file,
             caption = os.path.basename(file),
             chat_id = message.chat.id
       )
    except:
       await message.edit("Failed!")
       await message.delete()

    os.remove(str(file))
