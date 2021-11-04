import sys
import os 
from userbot import bot
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
import glob
import importlib
from userbot import CMD_HELP
import sys
from pathlib import Path


CHAT = os.getenv("LOGGER_ID")

try:
    bot.start()
except:
    print("Check Your STRING SESSION, Failed to auth.")
    sys.exit(0)

async def startupmessage():
    await bot(functions.channels.JoinChannelRequest(channel="@simple_userbot"))


for x in glob.glob("userbot/modules/*.py"):
    name = Path(open(x).name).stem.replace(".py", "")
    spec = importlib.util.spec_from_file_location(
        "userbot.modules.{}".format(name), Path("userbot/modules/{}.py".format(name))
    )
    mod = importlib.util.module_from_spec(spec)
    mod.bot = bot
    spec.loader.exec_module(mod)
    sys.modules["userbot.modules." + name] = mod
    print("Imported " + name.capitalize())
    

bot.loop.create_task(startupmessage())

bot.run_until_disconnected()
