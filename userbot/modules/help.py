from telethon import events
from userbot import CMD_HELP
import asyncio

@events.register(events.NewMessage(pattern="!help"))
async def help(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("`Unknown module type !help to see all modules`")
    else:
        await event.edit(" **Support Channel for help & report bugs @tilak_sharma_2004** ")
        string = (f"`Use !help <module_name>`\n\n**Currently Loaded [{len(CMD_HELP)}] Modules **\n")
        for i in CMD_HELP:
            string += f" `{str(i)} `{str(i)}` `{str(i)}` "
        await event.reply(string)
        
        
CMD_HELP.update({
    "alive":
    "do !jinda for alive your userbot"
})

CMD_HELP.update({
    "ping":
    "do !check to ping your userbot"
})

CMD_HELP.update({
    "pmpermit":
    "do !allow to allow someone to pm\ndo !disallow to disallow someone to pm\ndo !listallowed to get the list of allowed users in pm"
})
