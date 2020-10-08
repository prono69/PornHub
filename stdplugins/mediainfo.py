"""MEDIA INFO"""
# Suggested by - @d0n0t (https://github.com/code-rgb/USERGE-X/issues/9)
# Copyright (C) 2020 BY - GitHub.com/code-rgb [TG - @deleteduser420]
# All rights reserved.

import os

from uniborg.util import admin_cmd
from userbot import runcmd
from userbot.anime import post_to_telegraph


@borg.on(admin_cmd(pattern="media"))
async def mediainfo(message):
    X_MEDIA = None
    reply = await message.get_reply_message()
    if not reply:
        await message.edit("reply to media first")
        return
    await message.edit("`Processing...`")
    try:
        if reply.media and reply.media.document:
            X_MEDIA = reply.media.document.mime_type
            hmm = reply.media.document.stringify()
    except:
        if reply.media and reply.media.photo:
            X_MEDIA = "photo"
            hmm = reply.media.photo.stringify()
    if not X_MEDIA:
        return await message.edit("`Reply To a Vaild Media Format`")
    if X_MEDIA.startswith(("text")):
        return await message.edit("`Reply To a Vaild Media Format`")
    file_path = await reply.download_media(Config.TMP_DOWNLOAD_DIRECTORY)
    out, err, ret, pid = await runcmd(f"mediainfo {file_path}")
    if not out:
        out = "Not Supported"
    body_text = f"""<br>
    <h2>JSON</h2>
    <code>{hmm}</code>
    <br>
    <br>
    <h2>DETAILS</h2>
    <code>{out}</code>
    """
    link = post_to_telegraph(f"{X_MEDIA}", body_text)

    await message.edit(
        f"ℹ️  <b>MEDIA INFO:  <a href ='{link}' > {X_MEDIA}</a></b>",
        parse_mode="HTML",
        link_preview=True,
    )

    os.remove(file_path)
