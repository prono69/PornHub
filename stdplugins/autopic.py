"""
Time In Profile Pic.....
Command: `.autopp`

:::::Credit Time::::::
1) Coded By: @s_n_a_p_s
2) Ported By: @r4v4n4 (Legend)
3) End Game Help By: @spechide
4) All credits goes to @NeoMatrix90

#curse: who ever edits this credit section will goto hell
"""
import asyncio
import os
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions

from uniborg.util import admin_cmd

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


@borg.on(admin_cmd(pattern="autopp ?(.*)"))
async def autopic(event):
    downloaded_file_name = "./ravana/original_pic.png"
    downloader = SmartDL(Config.RAVANA_LEELA, downloaded_file_name, progress_bar=True)
    downloader.start(blocking=False)
    photo = "photo_pfp.png"
    while not downloader.isFinished():
        pass
    counter = -30
    while True:
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        file_test = im.rotate(counter, expand=False).save(photo, "PNG")
        current_time = datetime.now().strftime(
            "⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ \n ⚡PORNHUB TIMEZONE⚡ \n  Time: %H:%M:%S \n  Date: %d.%m.%y \n⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡"
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((30, 200), current_time, font=fnt, fill=(255, 255, 0))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)
            counter -= 30
            await asyncio.sleep(90)
        except BaseException:
            return
