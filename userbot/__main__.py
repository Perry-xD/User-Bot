import sys
import os
import userbot.utils  # pylint:disable=E0602
from userbot import bot
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
import glob
import importlib
import sys
from pathlib import Path


CHAT = os.getenv("LOGGER_ID")

try:
    bot.start()
except:
    print("Check Your STRING SESSION, Failed to auth.")
    sys.exit(0)

async def startupmessage():
    await bot(functions.channels.JoinChannelRequest(channel="@deadly_userbot"))
    try:
        if CHAT != 0:
            await bot.send_message(
                CHAT,
                ("""𝐂𝐎𝐍𝐆𝐑𝐀𝐓𝐔𝐋𝐀𝐓𝐈𝐎𝐍 𝐘𝐎𝐔𝐑 USER-𝐁𝐎𝐓 𝐈𝐒 𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘 😈💖💥 .. 𝐓𝐘𝐏𝐄 (!jinda or !check) 𝐅𝐎𝐑 𝐂𝐇𝐄𝐂𝐊 𝐓𝐇𝐀𝐓 𝐁𝐎𝐓 𝐈𝐒 𝐀𝐋𝐈𝐕𝐄 𝐎𝐑 𝐍𝐎𝐓...𝐉𝐎𝐈𝐍 @simple_userbot 𝐅𝐎𝐑 𝐀𝐍𝐘 𝐇𝐄𝐋𝐏 ..𝐄𝐍𝐉𝐎𝐘 𝐔𝐑 𝐁𝐎𝐓🤘😉.""")
)
    except Exception as e:
        LOGS.info(str(e))

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
