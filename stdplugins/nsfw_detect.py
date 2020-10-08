# Copyright (C) 2020 BY - GitHub.com/code-rgb [TG - @deleteduser420]
# All rights reserved.
# Ported from userge by @kirito6969

"""Detects Nsfw content with the help of A.I."""

import os
from asyncio import sleep

import requests

from uniborg.util import admin_cmd, edit_or_reply


@bot.on(admin_cmd(pattern="detect ?(.*)"))
async def detect_(message):
    """detect nsfw"""
    reply = await bot.download_media(
        await message.get_reply_message(),
    )
    chat = message.chat_id
    a = await edit_or_reply(message, "`Detecting NSFW limit...`")
    if not reply:
        await a.edit("`Reply to media !`")
        await sleep(2)
        await a.delete()
        return
    if Config.DEEP_AI is None:
        await a.edit("Add VAR `DEEP_AI` get Api Key from https://deepai.org/")
        await sleep(2)
        await a.delete()
        return
    api_key = Config.DEEP_AI
    photo = reply
    r = requests.post(
        "https://api.deepai.org/api/nsfw-detector",
        files={
            "image": open(photo, "rb"),
        },
        headers={"api-key": api_key},
    )
    os.remove(photo)
    if "status" in r.json():
        await a.edit(r.json()["status"])
        await sleep(2)
        await a.delete()
        return
    r_json = r.json()["output"]
    pic_id = r.json()["id"]
    percentage = r_json["nsfw_score"] * 100
    detections = r_json["detections"]
    link = f"https://api.deepai.org/job-view-file/{pic_id}/inputs/image.jpg"
    result = f"<b><u>Detected Nudity</u> :</b>\n<a href='{link}'>>>></a> <code>{percentage:.3f}%</code>\n\n"

    if detections:
        for parts in detections:
            name = parts["name"]
            confidence = int(float(parts["confidence"]) * 100)
            result += f"• {name}:\n   <code>{confidence} %</code>\n"
    await bot.send_message(
        chat,
        result,
        link_preview=False,
        parse_mode="HTML",
        reply_to=message.reply_to_msg_id,
    )
    await a.delete()
