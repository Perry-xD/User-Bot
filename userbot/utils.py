import glob
import importlib
import sys
from pathlib import Path

from telethon import events

from userbot import bot

CMD_HANDLER = "!"


def userbot(**args):
    args["pattern"] = "^{}".format(CMD_HANDLER) + args["pattern"]

    def decorator(func):
        async def wrapper(c):
            try:
                await func(c)
            except:
                return

        bot.add_event_handler(wrapper, events.NewMessage(**args))

    return decorator



