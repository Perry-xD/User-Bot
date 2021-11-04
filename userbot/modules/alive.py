from telethon import events, client
import asyncio

@events.register(events.NewMessage(pattern="!jinda"))
async def alive_me(event):
  me = await client.get_me()
  await event.edit(f"**Aha Meh Alive {me.first_name} Sir!**")
