"""Check if userbot alive or not . """

import time
from platform import python_version

from telethon import version

from uniborg import MODULE
from uniborg.util import admin_cmd
from userbot import StartTime, get_readable_time, pepe

ALIVE_NAME = Config.ALIVE_NAME
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𠘨 工 长 工 丅 卂"
IMG = Config.ALIVE_PIC
MODULE.append("alive")


@borg.on(admin_cmd(pattern="alive", allow_sudo=True))
async def amireallyalive(alive):
    reply_to_id = alive.message
    uptime = await get_readable_time((time.time() - StartTime))
    hmm = borg.uid
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    output = f"""
**✮PEPEBOT IS UP AND RUNNING✮**

       😴 __Lazy as a Sloth__ 😴

✧ **System** : `Linux`
✧ **Uptime** : `{uptime}`
✧ **Telethon version** : `{version.__version__}`
✧ **Python Version** : `{python_version()}`
✧ **PepeBot Version** : `{pepe}`
✧ **Database** : `Functioning Normally`
✧ **My Master** : [{DEFAULTUSER}](tg://user?id={hmm})

**Pepe is always with you, My Master!**

✧ **Repo** : [PEPEBOT](https://github.com/prono69/PepeBot)"""

    #####sticker = await borg.get_messages("LazyAF_Pepe", 26)
    #####await borg.send_file(alive.chat_id, file=sticker)
    await borg.send_file(
        alive.chat_id, IMG, caption=output, reply_to=reply_to_id, link_preview=False
    )
    await alive.delete()
