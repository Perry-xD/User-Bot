from telethon import events
import asyncio

@bot.on(events.NewMessage(pattern="!check"))
async def eval_(e):
    await e.edit("**✔USERBOT ONLINE!**")
