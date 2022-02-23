from pyrogram import Client, filters, idle
from config import BOT_TOKEN, APP_ID, API_HASH, SESSION


plugins = dict(root="src/plugins")
bot = Client(
   "bot",
   bot_token=BOT_TOKEN,
   api_id=APP_ID,
   api_hash=API_HASH,
   plugins=plugins,
   workers = 6
)

app = Client(
  api_id = APP_ID,
  api_hash = API_HASH,
  session_name= SESSION
)

