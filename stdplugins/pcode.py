# Credits @buddhhu
# This software is a part of https://github.com/buddhhu/Plus

import asyncio
import os

import pygments
from pygments.formatters import ImageFormatter
from pygments.lexers import Python3Lexer

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern=r"pcode", allow_sudo=True))
async def coder_print(event):
    cmd = event.text
    a = await event.get_reply_message()
    coder = ""
    if len(cmd) > 7:
        coder = " ".join(cmd[7:])
    elif event.reply_to_msg_id and len(cmd) == 6:
        coder = a.message
    elif len(cmd) == 6:
        await event.reply("`No text Given`")
        await asyncio.sleep(2)
        await event.delete()
        return
    pygments.highlight(
        f"{coder}",
        Python3Lexer(),
        ImageFormatter(font_name="LiberationMono-Regular.ttf", line_numbers=True),
        "out.png",
    )
    await event.client.send_file(event.chat_id, "out.png", force_document=False)
    await event.delete()
    os.remove("out.png")


@borg.on(admin_cmd(pattern=r"ncode", allow_sudo=True))
async def mkc(event):
    a = await event.client.download_media(
        await event.get_reply_message(), Config.TMP_DOWNLOAD_DIRECTORY
    )
    s = open(a, "r")
    c = s.read()
    s.close()
    pygments.highlight(
        f"{c}",
        Python3Lexer(),
        ImageFormatter(font_name="LiberationMono-Regular.ttf", line_numbers=True),
        "out.png",
    )
    res = await event.client.send_message(
        event.chat_id,
        "**Pasting this code on my page...**",
        reply_to=event.reply_to_msg_id,
    )
    await event.client.send_file(
        event.chat_id, "out.png", force_document=True, reply_to=event.reply_to_msg_id
    )
    await event.client.send_file(
        event.chat_id, "out.png", force_document=False, reply_to=event.reply_to_msg_id
    )
    await res.delete()
    await event.delete()
    os.remove(a)
    os.remove("out.png")
