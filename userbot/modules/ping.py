from telethon import events
import asyncio

@events.register(events.NewMessage(pattern="!check"))
async def eval_(e):
    await e.edit("**✔USERBOT ONLINE!**")
