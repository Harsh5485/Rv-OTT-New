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
from rvdb import mydb # <--- FIX: jvdb ki jagah rvdb kiya
from pytz import timezone
from psutil import virtual_memory, cpu_percent
from jvdrive import GoogleDriveHelper
from util import *
from jvripper import *
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
    # Koyeb variable PORT use karega
    port = int(os.environ.get('PORT', 8000))
    health_app.run(host='0.0.0.0', port=port)

# Background mein health server chalane ke liye
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

# Baki ka aapka poora original code (TGBot initialization, Command Handlers, etc.) 
# niche bilkul waise hi rahega jaise aapne bheja tha.
