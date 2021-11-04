from ..utils import userbot
import asyncio

@userbot(pattern="check")
async def eval_(e):
    await e.edit("**✔USERBOT ONLINE!**")
