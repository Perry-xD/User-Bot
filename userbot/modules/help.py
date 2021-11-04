from ..utils import userbot
from userbot import help
import asyncio

@userbot(pattern="help")
async def help(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in help:
            await event.edit(str(help[args]))
        else:
            await event.edit("`Unknown module type !help to see all modules`")
    else:
        await event.edit(" **Support Channel for help & report bugs @tilak_sharma_2004** ")
        string = (f"`Use !help <module_name>`\n\n**Currently Loaded [{len(help)}] Modules **\n")
        for i in CMD_HELP:
            string += f" `{str(i)} `{str(i)}` `{str(i)}` "
        await event.reply(string)
        
        
help.update({
    "alive":
    "do !jinda for alive your userbot"
})

help.update({
    "ping":
    "do !check to ping your userbot"
})

help.update({
    "pmpermit":
    "do !allow to allow someone to pm\n
    do !disallow to disallow someone to pm
    do !listallowed to get the list of allowed users in pm
"
})
