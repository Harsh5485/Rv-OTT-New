# Use it your own risk
# The Developer will not be responsible for any misuse of this bot/script

import io
import string 
import asyncio
import os
import traceback
import logging
import shutil
import random
import threading
from pyrogram import Client, filters, idle
from pyrogram.errors import FloodWait, UserIsBlocked, PeerIdInvalid, InputUserDeactivated
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup
from time import time, strftime, gmtime
from flask import Flask
from config import Config
from rvdb import mydb # <--- FIXED: jvdb se rvdb kiya
from pytz import timezone
from psutil import virtual_memory, cpu_percent
from rvdrive import GoogleDriveHelper # <--- Rename your jvdrive.py to rvdrive.py
from util import *
from rvripper import * # <--- Rename your jvripper.py to rvripper.py
from logging.handlers import RotatingFileHandler
from expiringdict import ExpiringDict
from urllib.parse import quote
from datetime import datetime

# --- KOYEB HEALTH CHECK SERVER ---
health_app = Flask(__name__)

@health_app.route('/')
def health_check():
    return {'status': 'ok', 'service': 'rv-ott-bot'}

def start_health_server():
    # Koyeb assigns port via environment variable
    port = int(os.environ.get('PORT', 8000))
    health_app.run(host='0.0.0.0', port=port)

# Run health server in a separate thread
threading.Thread(target=start_health_server, daemon=True).start()
# ---------------------------------

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("log.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger(__name__)

TGBot = Client("TGPaidBot",
               api_id=Config.API_ID,
               api_hash=Config.API_HASH,
               bot_token=Config.BOT_TOKEN,
               workers=50,
               max_concurrent_transmissions=200)

if Config.SESSION_STRING:
    TGUser = Client(
        "TGUserClient",
        session_string=Config.SESSION_STRING,
        api_id = Config.API_ID,
        api_hash = Config.API_HASH,
        sleep_threshold = 30,
        no_updates = True,
        max_concurrent_transmissions=200
    )
else:
    TGUser = None

USER_DATA = ExpiringDict(max_len=1000, max_age_seconds=60*60)
BOT_UPSTATE = datetime.now(timezone('Asia/Kolkata')).strftime("%d/%m/%y %I:%M:%S %p")
BOT_START_TIME = time()
CHECK_ONCE = []

ST1 = [ 
    [
        InlineKeyboardButton(text="Updates Channel", url="https://t.me/jv"),
        InlineKeyboardButton(text="Support Grp", url="https://t.me/jv")
    ],
    [
        InlineKeyboardButton(f"About", callback_data="About"),
        InlineKeyboardButton(f"Help", callback_data="Help"),
        InlineKeyboardButton(f"Contact Us", callback_data="ContactUs"),
    ],
    [
        InlineKeyboardButton(f"Usage", callback_data="usage"),
        InlineKeyboardButton(f"Plans", callback_data="plans"),   
    ]
]

# --- Commands ---
@TGBot.on_message(filters.command("start"))
async def start_handler(bot: Client, message: Message):
    await mydb.add_user(message.from_user.id)
    await message.reply_text(text=f"**Hello👋 {message.from_user.mention} I am RV DRM Downloader Bot.**", reply_markup=InlineKeyboardMarkup(ST1))

# --- Bot Runner ---
async def StartBot():
    await TGBot.start()
    if TGUser:
        await TGUser.start()
    print("----------Bot Started (RV Version)----------")
    await idle()
    await TGBot.stop()
    if TGUser:
        await TGUser.stop()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(StartBot())
