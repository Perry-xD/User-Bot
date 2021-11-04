from ..utils import userbot
import os
import asyncio

chat = os.getenv("LOGGER_ID")

@userbot(incoming=True)
async def taglogger(e):
  mesage = await e.message
  await mesage.forward_to(chat)
