"""Color Plugin for @UniBorg
Syntax: .color <color_code>"""
import logging
import os

from PIL import Image, ImageColor

from uniborg.util import admin_cmd

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.WARN
)


@borg.on(admin_cmd(pattern="color ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    if input_str.startswith("#"):
        try:
            usercolor = ImageColor.getrgb(input_str)
        except Exception as e:
            await event.edit(str(e))
            return False
        else:
            im = Image.new(mode="RGB", size=(1280, 720), color=usercolor)
            im.save("PepeBot.png", "PNG")
            input_str = input_str.replace("#", "#COLOR_")
            await borg.send_file(
                event.chat_id,
                "PepeBot.png",
                force_document=False,
                caption=input_str,
                reply_to=message_id,
            )
            os.remove("PepeBot.png")
            await event.delete()
    else:
        await event.edit("Syntax: `.color <color_code>`")
