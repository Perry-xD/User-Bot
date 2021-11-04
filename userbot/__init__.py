import logging
import time
from os import getenv

from telethon import TelegramClient
from telethon.sessions import StringSession

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
)

help = {}

(
    SESSION,
    API_ID,
    API_HASH,
) = (
    getenv("SESSION"),
    getenv("API_ID"),
    getenv("API_HASH"),
)


bot = TelegramClient(StringSession(SESSION), API_ID, API_HASH)


start_time = time.time()
