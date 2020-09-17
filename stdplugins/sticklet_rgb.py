# Random RGB Sticklet by @PhycoNinja13b
# Modified by @kirito6969

import io
import random
import textwrap

from PIL import Image, ImageDraw, ImageFont

from uniborg.util import admin_cmd

"""Type
\n`.ilet` <reply to a message> or <input str>
"""


@borg.on(admin_cmd(pattern="ilet ?(.*)", allow_sudo=True))
async def sticklet(event):
    R = random.randint(0, 256)
    G = random.randint(0, 256)
    B = random.randint(0, 256)
    sticktext = event.pattern_match.group(1)

    if not sticktext:
        get = await event.get_reply_message()
        sticktext = get.text

    await event.delete()
    if not sticktext:
        await event.edit("`I need text to sticklet!`")
        return

    sticktext = textwrap.wrap(sticktext, width=10)
    sticktext = "\n".join(sticktext)

    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 230
    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", size=fontsize
    )

    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", size=fontsize
        )

    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(
        ((512 - width) / 2, (512 - height) / 2), sticktext, font=font, fill=(R, G, B)
    )

    image_stream = io.BytesIO()
    image_stream.name = "sticker.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)

    await event.edit(await event.client.send_file(event.chat_id, image_stream))
