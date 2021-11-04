from telethon import events, client
import os
import asyncio

chat = os.getenv("LOGGER_ID")

@events.register(events.NewMessage(incoming=True))
async def taglogger(e):
  mesage = await e.message
  await mesage.forward_to(chat)
