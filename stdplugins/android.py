# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to android"""

import asyncio
import json
import re

from bs4 import BeautifulSoup
from html_telegraph_poster import TelegraphPoster
from requests import get

from uniborg import MODULE, SYNTAX
from uniborg.util import admin_cmd, edit_or_reply

MODULE.append("android")

GITHUB = "https://github.com"
DEVICES_DATA = (
    "https://raw.githubusercontent.com/androidtrackers/"
    "certified-android-devices/master/devices.json"
)


@borg.on(admin_cmd(pattern="magisk ?(.*)"))
async def magisk(request):
    """ magisk latest releases """
    magisk_dict = {
        "Stable": "https://raw.githubusercontent.com/topjohnwu/magisk_files/master/stable.json",
        "Beta": "https://raw.githubusercontent.com/topjohnwu/magisk_files/master/beta.json",
        "Canary": "https://raw.githubusercontent.com/topjohnwu/magisk_files/canary/debug.json",
    }
    releases = "__**Latest Magisk Releases:**__\n\n"
    for name, release_url in magisk_dict.items():
        data = get(release_url).json()
        releases += (
            f'**{name} :** [ZIP v{data["magisk"]["version"]}]({data["magisk"]["link"]}) | '
            f'[APK v{data["app"]["version"]}]({data["app"]["link"]}) | '
            f'[Uninstaller]({data["uninstaller"]["link"]})\n'
        )
    await request.edit(releases)


@borg.on(admin_cmd(pattern=r"device(?: |$)(\S*)"))
async def device_info(request):
    """ get android device basic info from its codename """
    textx = await request.get_reply_message()
    codename = request.pattern_match.group(1)
    if codename:
        pass
    elif textx:
        codename = textx.text
    else:
        await edit_or_reply(request, "`Usage: .device <codename> / <model>`")
        return
    data = json.loads(
        get(
            "https://raw.githubusercontent.com/androidtrackers/"
            "certified-android-devices/master/by_device.json"
        ).text
    )
    results = data.get(codename)
    if results:
        reply = f"**Search results for {codename}**:\n\n"
        for item in results:
            reply += (
                f"**Brand**: `{item['brand']}`\n"
                f"**Name**: `{item['name']}`\n"
                f"**Model**: `{item['model']}`\n\n"
            )
    else:
        reply = f"`Couldn't find info about {codename}!`\n"
    await edit_or_reply(request, reply)


@borg.on(admin_cmd(pattern=r"codename(?: |)([\S]*)(?: |)([\s\S]*)"))
async def codename_info(request):
    """ search for android codename """
    textx = await request.get_reply_message()
    brand = request.pattern_match.group(1).lower()
    device = request.pattern_match.group(2).lower()

    if brand and device:
        pass
    elif textx:
        brand = textx.text.split(" ")[0]
        device = " ".join(textx.text.split(" ")[1:])
    else:
        await edit_or_reply(request, "`Usage: .codename <brand> <device>`")
        return

    data = json.loads(
        get(
            "https://raw.githubusercontent.com/androidtrackers/"
            "certified-android-devices/master/by_brand.json"
        ).text
    )
    devices_lower = {k.lower(): v for k, v in data.items()}  # Lower brand names in JSON
    devices = devices_lower.get(brand)
    results = [
        i
        for i in devices
        if i["name"].lower() == device.lower() or i["model"].lower() == device.lower()
    ]
    if results:
        reply = f"**Search results for {brand} {device}**:\n\n"
        if len(results) > 8:
            results = results[:8]
        for item in results:
            reply += (
                f"**Codename**: `{item['device']}`\n"
                f"**Name**: `{item['name']}`\n"
                f"**Model**: `{item['model']}`\n\n"
            )
    else:
        reply = f"`Can't find {device} codename!`\n"
    await edit_or_reply(request, reply)


@borg.on(admin_cmd(pattern=r"specs(?: |)([\S]*)(?: |)([\s\S]*)"))
async def devices_specifications(request):
    """ Mobile devices specifications """
    textx = await request.get_reply_message()
    brand = request.pattern_match.group(1).lower()
    device = request.pattern_match.group(2).lower()
    if brand and device:
        pass
    elif textx:
        brand = textx.text.split(" ")[0]
        device = " ".join(textx.text.split(" ")[1:])
    else:
        await request.edit("`Usage: .specs <brand> <device>`")
        return
    all_brands = (
        BeautifulSoup(
            get("https://www.devicespecifications.com/en/brand-more").content, "lxml"
        )
        .find("div", {"class": "brand-listing-container-news"})
        .findAll("a")
    )
    brand_page_url = None
    try:
        brand_page_url = [
            i["href"] for i in all_brands if brand == i.text.strip().lower()
        ][0]
    except IndexError:
        await request.edit(f"`{brand} is unknown brand!`")
    devices = BeautifulSoup(get(brand_page_url).content, "lxml").findAll(
        "div", {"class": "model-listing-container-80"}
    )
    device_page_url = None
    try:
        device_page_url = [
            i.a["href"]
            for i in BeautifulSoup(str(devices), "lxml").findAll("h3")
            if device in i.text.strip().lower()
        ]
    except IndexError:
        await request.edit(f"`can't find {device}!`")
    if len(device_page_url) > 2:
        device_page_url = device_page_url[:2]
    reply = ""
    for url in device_page_url:
        info = BeautifulSoup(get(url).content, "lxml")
        reply = "\n**" + info.title.text.split("-")[0].strip() + "**\n\n"
        info = info.find("div", {"id": "model-brief-specifications"})
        specifications = re.findall(r"<b>.*?<br/>", str(info))
        for item in specifications:
            title = re.findall(r"<b>(.*?)</b>", item)[0].strip()
            data = (
                re.findall(r"</b>: (.*?)<br/>", item)[0]
                .replace("<b>", "")
                .replace("</b>", "")
                .strip()
            )
            reply += f"**{title}**: {data}\n"
    await request.edit(reply)


@borg.on(admin_cmd(pattern=r"twrp(?: |$)(\S*)"))
async def twrp(request):
    """ get android device twrp """
    textx = await request.get_reply_message()
    device = request.pattern_match.group(1)
    if device:
        pass
    elif textx:
        device = textx.text.split(" ")[0]
    else:
        await request.edit("`Usage: .twrp <codename>`")
        return
    url = get(f"https://dl.twrp.me/{device}/")
    if url.status_code == 404:
        reply = f"`Couldn't find twrp downloads for {device}!`\n"
        await request.edit(reply)
        return
    page = BeautifulSoup(url.content, "lxml")
    download = page.find("table").find("tr").find("a")
    dl_link = f"https://dl.twrp.me{download['href']}"
    dl_file = download.text
    size = page.find("span", {"class": "filesize"}).text
    date = page.find("em").text.strip()
    reply = (
        f"**Latest TWRP for {device}:**\n"
        f"[{dl_file}]({dl_link}) - __{size}__\n"
        f"**Updated:** __{date}__\n"
    )
    await request.edit(reply)


# By @deleteduser420
# Ported for PepeBot by @kirito6969


@borg.on(admin_cmd(pattern="ofox ?(.*)"))
async def ofox_(message):
    if not message.pattern_match.group(1):
        await edit_or_reply(message, "`Provide a device codename to search recovery`")
        await asyncio.sleep(3)
        await message.delete()
        return
    t = TelegraphPoster(use_api=True)
    t.create_api_token("PepeBot")
    await edit_or_reply(message, "🔍 `Searching for recovery...`")
    await asyncio.sleep(2)
    await message.delete()
    photo = "https://i.imgur.com/582uaSk.png"
    API_HOST = "https://api.orangefox.download/v2/device/"
    codename = message.pattern_match.group(1)
    try:
        cn = get(f"{API_HOST}{codename}")
        r = cn.json()
    except ValueError:
        await edit_or_reply(message, f"`Recovery not found for {codename}!`")
        await asyncio.sleep(3)
        await message.delete()
        return
    s = get(f"{API_HOST}{codename}/releases/stable/last").json()
    info = f"📱 <b>Device:</b> {r['fullname']}\n"
    info += f"👤 <b>Maintainer:</b> {r['maintainer']['name']}\n\n"
    recovery = f"🦊 <code>{s['file_name']}</code>\n"
    recovery += f"📅 {s['date']}\n"
    recovery += f"ℹ️ <b>Version:</b> {s['version']}\n"
    recovery += f"📌 <b>Build Type:</b> {s['build_type']}\n"
    recovery += f"🔰 <b>Size:</b> {s['size_human']}\n\n"
    recovery += "📍 <b>Changelog:</b>\n"
    recovery += f"<code>{s['changelog']}</code>\n\n"
    msg = info
    msg += recovery
    notes_ = s.get("notes")
    if notes_:
        notes = t.post(title="READ Notes", author="", text=notes_)
        msg += f"🗒️ <a href={notes['url']}>NOTES</a>\n"
    msg += f"⬇️ <a href={s['url']}>DOWNLOAD</a>"
    await borg.send_file(message.chat_id, file=photo, caption=msg, parse_mode="HTML")


SYNTAX.update(
    {
        "android": "**android**\
\n\n**Syntax : **`.magisk`\
\n**Usage :** Get latest Magisk releases\
\n\n**Syntax : **`.device <codename>`\
\n**Usage :** Get info about android device codename or model.\
\n\n**Syntax : **`.codename <brand> <device>`\
\n**Usage :** Search for android device codename.\
\n\n**Syntax : **`.specs <brand> <device>`\
\n**Usage :** Get device specifications info.\
\n\n**Syntax :** `.ofox <codename>`\
\n**Usage :** Get latest Orange Fox recovery for your device.\
\n\n**Syntax : **`.twrp <codename>`\
\n**Usage :** Get latest twrp download for android device."
    }
)
