from ..utils import userbot
import asyncio

@userbot(pattern="jinda")
async def alive_me(event):
  me = await bot.get_me()
  await event.edit(f"**Aha Meh Alive {me.first_name} Sir!**")
