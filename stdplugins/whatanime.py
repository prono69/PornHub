# https://soruly.github.io/trace.moe/#/
import html
import json
from io import BytesIO, StringIO
from urllib.parse import quote as urlencode

import aiohttp
import pendulum
from telethon.errors.rpcerrorlist import FilePartsInvalidError
from telethon.tl.types import (
    DocumentAttributeAnimated,
    DocumentAttributeFilename,
    MessageMediaDocument,
)
from telethon.utils import is_image, is_video

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="areverse"))
async def areverse(e):
    media = e.media
    if not media:
        r = await e.get_reply_message()
        media = getattr(r, "media", None)
    if not media:
        await e.edit("err \\\nMedia required")
        return
    ig = is_gif(media) or is_video(media)
    if not is_image(media) and not ig:
        await e.edit("err \\\nMedia must be an image or gif or video")
        return
    filename = "file.jpg"
    if not ig and isinstance(media, MessageMediaDocument):
        attribs = media.document.attributes
        for i in attribs:
            if isinstance(i, DocumentAttributeFilename):
                filename = i.file_name
                break
    await e.edit("`Downloading image...`")
    content = await e.client.download_media(media, bytes, thumb=-1 if ig else None)
    await e.edit("`Searching for result...`")
    file = memory_file(filename, content)
    async with aiohttp.ClientSession() as session:
        url = "https://trace.moe/api/search"
        async with session.post(url, data={"image": file}) as raw_resp0:
            resp0 = await raw_resp0.text()
        js0 = json.loads(resp0)["docs"]
        if not js0:
            await e.edit("err \\\nNo results found")
            return
        js0 = js0[0]
        text = f'<b>{html.escape(js0["title_romaji"])}'
        if js0["title_native"]:
            text += f' ({html.escape(js0["title_native"])})'
        text += "</b>\n"
        if js0["episode"]:
            text += f'<b>Episode:</b> {html.escape(str(js0["episode"]))}\n'
        percent = round(js0["similarity"] * 100, 2)
        text += f"<b>Similarity:</b> {percent}%\n"
        dt = pendulum.from_timestamp(js0["at"])
        text += f"<b>At:</b> {html.escape(dt.to_time_string())}"
        await e.edit(text, parse_mode="html")
        dt0 = pendulum.from_timestamp(js0["from"])
        dt1 = pendulum.from_timestamp(js0["to"])
        ctext = (
            f"{html.escape(dt0.to_time_string())} - {html.escape(dt1.to_time_string())}"
        )
        url = (
            "https://trace.moe/preview.php"
            f'?anilist_id={urlencode(str(js0["anilist_id"]))}'
            f'&file={urlencode(js0["filename"])}'
            f'&t={urlencode(str(js0["at"]))}'
            f'&token={urlencode(js0["tokenthumb"])}'
        )
        async with session.get(url) as raw_resp1:
            file = memory_file("preview.mp4", await raw_resp1.read())
        try:
            await e.reply(ctext, file=file, parse_mode="html")
        except FilePartsInvalidError:
            await e.reply("`Cannot send preview :/`")


def memory_file(name=None, contents=None, *, bytes=True):
    if isinstance(contents, str) and bytes:
        contents = contents.encode()
    file = BytesIO() if bytes else StringIO()
    if name:
        file.name = name
    if contents:
        file.write(contents)
        file.seek(0)
    return file


def is_gif(file):
    # ngl this should be fixed, telethon.utils.is_gif but working
    # lazy to go to github and make an issue kek
    if not is_video(file):
        return False
    return DocumentAttributeAnimated() in getattr(file, "document", file).attributes
