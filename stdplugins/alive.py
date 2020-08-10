# For UniBorg
# Syntax .alive
import sys
import platform
import psutil
from telethon import __version__
from uniborg.util import admin_cmd
from sql_helpers.global_variables_sql import SYNTAX, BUILD


@borg.on(admin_cmd(pattern="alive ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Config.USER is not None:
        user = f"\n```User: {Config.USER}```"
    else:
        user = "NIKITA #CatGang #LazyAF_Geng"
    uname = platform.uname()
    memory = psutil.virtual_memory()
    specs = f"```System: {uname.system}```\n```Release: {uname.release}```\n```Version: {uname.version}```\n```Processor: {uname.processor}```\n```Memory [RAM]: {get_size(memory.total)}```"
    help_string = f"`Chal raha hu Bsdk...Don't Distirb Meh\nAb Hoga Tera Account Ban`\n\n**General Info:**\n```Build: {BUILD}\n```USER: {str(user)}\n```By: @kirito6969```\n\n**System Specifications:**\n{specs}\n```Python {sys.version}```\n```Telethon {__version__}```"
    # await event.client.send_file(event.chat_id,
    # file="CAADBQADgAEAAiriyVcBvpocd4kH1QI")
    await event.edit(help_string + "\n\n")
    # await event.delete()


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


SYNTAX.update({
    "alive": "\
**Requested Module --> alive**\
\n\n**Detailed usage of fuction(s):**\
\n\n```.alive```\
\nUsage: Returns userbot's system stats, user's name (only if set).\
"
})
