from telethon import events, client
from userbot import bot
import asyncio

@bot.on(events.NewMessage(pattern="!jinda"))
async def alive_me(event):
  me = await client.get_me()
  await event.edit(f"**Aha Meh Alive {me.first_name} Sir!**")
