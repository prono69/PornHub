"""Image to dot
	   .doti <count> + reply to img for COLOUR dot
	   .doty <count> + reply to img for BW dot
	   the bigger, the slower and bugger
	   recommended not more 1000"""

import io
import logging
import os
from re import sub

from PIL import Image, ImageDraw
from requests import get

from uniborg.util import admin_cmd, edit_delete

logger = logging.getLogger(__name__)


@borg.on(admin_cmd(pattern="tgs ?(.*)"))
async def tgscmd(message):
    """Tgs Killer"""
    reply = await message.get_reply_message()
    if not reply:
        await edit_delete(message, "`Reply to an animated sticker`", 3)
        return
    if not reply.file:
        await edit_delete(message, "`Reply to an animated sticker`", 3)
        return
    if not reply.file.name.endswith(".tgs"):
        await edit_delete(message, "`Reply to an animated sticker`", 3)
        return
        await reply.download_media("tgs.tgs")
        await message.edit("`Fixing this sticker...`")
        os.system("lottie_convert.py tgs.tgs json.json")
        json = open("json.json", "r")
        jsn = json.read()
        json.close()
        jsn = (
            jsn.replace("[1]", "[20]")
            .replace("[2]", "[30]")
            .replace("[3]", "[40]")
            .replace("[4]", "[50]")
            .replace("[5]", "[60]")
        )

        open("json.json", "w").write(jsn)
        os.system("lottie_convert.py json.json tgs.tgs")
        await reply.reply(file="tgs.tgs")
        os.remove("json.json")
        os.remove("tgs.tgs")
        await message.delete()


@borg.on(admin_cmd(pattern="ip ?(.*)"))
async def ipcmd(message):
    """Use as .ip <ip> (optional)"""
    ip = message.pattern_match.group(1)
    if not ip:
        await message.edit("`Give me ip address :(`")

    lookup = get(f"http://ip-api.com/json/{ip}").json()
    fixed_lookup = {}

    for key, value in lookup.items():
        special = {
            "lat": "Latitude",
            "lon": "Longitude",
            "isp": "ISP",
            "as": "AS",
            "asname": "AS name",
        }
        if key in special:
            fixed_lookup[special[key]] = str(value)
            continue

        key = sub(r"([a-z])([A-Z])", r"\g<1> \g<2>", key)
        key = key.capitalize()

        if not value:
            value = "None"

        fixed_lookup[key] = str(value)

    text = ""

    for key, value in fixed_lookup.items():
        text = text + f"<b>{key}:</b> <code>{value}</code>\n"

    await message.edit(
        f"<b><i><u>IP Information for PepeBot</u></i></b>\n\n{text}", parse_mode="html"
    )


@borg.on(admin_cmd(pattern="doti ?(.*)"))
async def dotifycmd(message):
    """Image to RGB dots"""
    mode = False
    reply, pix = await parse(message)
    if reply:
        await dotify(message, reply, pix, mode)


@borg.on(admin_cmd(pattern="doty ?(.*)"))
async def dotificmd(message):
    """Image to BW dots"""
    mode = True
    reply, pix = await parse(message)
    if reply:
        await dotify(message, reply, pix, mode)


async def parse(message):
    reply = await message.get_reply_message()
    if not reply:
        await edit_delete(message, "<b>Reply to Image!</b>", 3, parse_mode="html")
        return None, None
    args = message.pattern_match.group(1).split(" ", 1)
    pix = 100
    if args:
        args = args[0]
        if args.isdigit():
            pix = int(args) if int(args) > 0 else 100
    return reply, pix


async def dotify(message, reply, pix, mode):
    await edit_delete(message, "<b>Putting dots...</b>", 3, parse_mode="html")
    count = 24
    im_ = Image.open(io.BytesIO(await reply.download_media(bytes)))
    if im_.mode == "RGBA":
        temp = Image.new("RGB", im_.size, "#000")
        temp.paste(im_, (0, 0), im_)
        im_ = temp

    im = im_.convert("L")
    im_ = im if mode else im_
    [_.thumbnail((pix, pix)) for _ in [im, im_]]
    w, h = im.size
    img = Image.new(im_.mode, (w * count + (count // 2), h * count + (count // 2)), 0)
    ImageDraw.Draw(img)

    def cirsle(im, x, y, r, fill):
        x += r // 2
        y += r // 2
        draw = ImageDraw.Draw(im)
        draw.ellipse((x - r, y - r, x + r, y + r), fill)
        return im

    _x = _y = count // 2
    for x in range(w):
        for y in range(h):
            r = im.getpixel((x, y))
            fill = im_.getpixel((x, y))
            cirsle(img, _x, _y, r // count, fill)
            _y += count
        _x += count
        _y = count // 2

    out = io.BytesIO()
    out.name = "out.png"
    img.save(out)
    out.seek(0)
    await reply.reply(file=out)
    await message.delete()
