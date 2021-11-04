from ..utils import userbot
import io
import os
from telethon import events
import asyncio

is_allowed = []

@events.register(events.NewMessage(incoming=True))
async def pmpermit(event):
  if event.is_private:
    pass
  else: 
    return
  sender = await event.sender_id
  if sender in is_allowed:
    return
  else:
    await event.reply("**Hey bro! This is my master's dm don't spam**")
    
@events.register(events.NewMessage(pattern="!allow"))
async def pmallow(event):
  if event.is_private:
    chat = event.get_chat()
    if chat.id in is_allowed:
      await event.edit("this user is already allowed")
    else:
      await is_allowed.append(chat.id)
      await event.edit("Allowed this user to pm")
  elif event.is_group:
    chat = await event.get_reply_message()
    if not chat:
      await event.edit("please reply to someone")
      return
    sender = chat.sender_id
    if sender in is_allowed:
      await event.edit("this user is already allowed")
    else:
      await is_allowed.append(sender)
      await event.edit("Allowed this user to pm")
  else:
    return



@events.register(events.NewMessage(pattern="!disallow"))
async def pmdallow(e):
  if event.is_private:
    chat = event.get_chat()
    if chat in is_allowed:
      await is_allowed.remove(chat.id)
      await e.edit("Removed this user from allowed user list")
  elif event.is_group:
    chat = await event.get_reply_message()
    if not chat:
      await event.edit("please reply to someone")
      return
    sender = chat.sender_id
    if sender not in is_allowed:
      await event.edit("this user is already dis-allowed")
    else:
      await is_allowed.remove(sender)
      await event.edit("dis-Allowed this user to pm")
  else:
    return
      
      
      
@events.register(events.NewMessage(pattern="!listallowed"))
async def pmlistallow(e):
  for i in is_allowed:
    if len(i) > 0:
      await event.edit(f"{i}\n")
    
    else:
      await event.edit("No approved pms lol")
    if len(i) > 4095:
      with io.BytesIO(str.encode(i)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="[Deadly bot]Current Approved PMs",
                    reply_to=event,
                )
                await event.delete()
