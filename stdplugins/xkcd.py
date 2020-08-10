"""XKCD Search
Syntax: .xkcd <search>"""
from telethon.tl.types import Channel
import asyncio
import json
import requests
from urllib.parse import quote
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="xkcd ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    xkcd_id = None
    if input_str:
        if input_str.isdigit():
            xkcd_id = input_str
        else:
            xkcd_search_url = "https://relevantxkcd.appspot.com/process?"
            queryresult = requests.get(
                xkcd_search_url,
                params={
                    "action":"xkcd",
                    "query":quote(input_str)
                }
            ).text
            xkcd_id = queryresult.split(" ")[2].lstrip("\n")
    if xkcd_id is None:
        xkcd_url = "https://xkcd.com/info.0.json"
    else:
        xkcd_url = "https://xkcd.com/{}/info.0.json".format(xkcd_id)
    r = requests.get(xkcd_url)
    if r.ok:
        data = r.json()
        year = data.get("year")
        month = data["month"].zfill(2)
        day = data["day"].zfill(2)
        xkcd_link = "https://xkcd.com/{}".format(data.get("num"))
        safe_title = data.get("safe_title")
        transcript = data.get("transcript")
        alt = data.get("alt")
        img = data.get("img")
        title = data.get("title")
        link_preview = f"[\u2060]({img})"
        output_str = """**{}**
[XKCD ]({})
Title: {}
Alt: {}
Day: {}
Month: {}
Year: {}""".format(input_str, xkcd_link, safe_title, alt, day, month, year)
        input_chat = await event.get_chat()
        if isinstance(input_chat, Channel) and input_chat.default_banned_rights.embed_links:
            rep = event
            if event.reply_to_msg_id:
                rep = await event.get_reply_message()
            await rep.reply(output_str, link_preview=False, file=img)
            await event.delete()
        else:
            final_output = link_preview + output_str
            await event.edit(final_output, link_preview=True)
    else:
        await event.edit("xkcd n.{} not found!".format(xkcd_id))
