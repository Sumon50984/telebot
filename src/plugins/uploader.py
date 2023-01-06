from pyrogram import filters
from ..bot import app
import asyncio
import os
from pySmartDL import SmartDL

dir = "DOWNLOADS/"
@app.on_message(filters.command("upload", "*") & filters.me)

# Upload files from downloadable links

async def uploader(app, message):
    if len(message.command)>1:
       downloader = SmartDL(message.command[1], dir, progress_bar=False)
       await message.edit("...")

       downloader.start()

       if downloader.isSuccessful():
             await message.edit("File downloaded")
             await asyncio.sleep(1)
       else:
             for e in downloader.get_errors():
                 await message.edit(str(e))

       file = downloader.get_dest()

    try:
       await app.send_document(
             document = file,
             caption = os.path.basename(file),
             chat_id = message.chat.id,
       )
    except:
       await message.edit("Failed!")
       await message.delete()
    await message.delete()
    os.remove(str(file))
