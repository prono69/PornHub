"""
Time In Profile Pic.....
Command: `.cpp`

:::::Credit Time::::::
1) Coded By: @s_n_a_p_s
2) Ported By: @r4v4n4 (Legend)
3) End Game Help By: @spechide
NOTE: NO.4 IS A VIRUS WHICH HAD COME HERE ACCIDENTALLY
4) Custom / Modified Plugin for some magical effects by this Legendary Guy @PhycoNinja13b


#curse: who ever edits this credit section will goto hell

⚠️DISCLAIMER⚠️

USING THIS PLUGIN CAN RESULT IN ACCOUNT BAN + CAS BAN + SPAM BAN + ACCOUNT SUSPENSION . WE DONT CARE ABOUT BAN, SO WE ARR USING THIS.
"""
import asyncio
import os
import random
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions

from uniborg.util import admin_cmd

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = [
    "https://telegra.ph/file/8e9effb5ba79a94e44f18.jpg",
    "https://telegra.ph/file/3628db51a1c3e0876d302.jpg",
    "https://telegra.ph/file/199c2029f227eab9654f2.jpg",
    "https://telegra.ph/file/ccd1d7272082434cc643d.jpg",
    "https://telegra.ph/file/f6dbede265f6a6f909560.jpg",
    "https://telegra.ph/file/edd72efc60ce1cccdc203.jpg",
    "https://telegra.ph/file/d72cc07a0fa56d787fc5a.jpg",
    "https://telegra.ph/file/64d69c69f03372d18a5a9.jpg",
    "https://telegra.ph/file/1b2928c73612cf856c32b.jpg",
    "https://telegra.ph/file/e07a24aaa229b0c51471b.jpg",
    "https://telegra.ph/file/7bbb6813da08d5bccbb56.jpg",
]


@borg.on(admin_cmd(pattern="cpp ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./ravana/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            pass

        shutil.copy(downloaded_file_name, photo)
        Image.open(photo)
        current_time = datetime.now().strftime(
            "\n \n \n \n \n \n \n Owner: @kirito6969 . It's Her Choice (- Lawdi) \n \n \n \n \n \n \n \n \n                   Nikal Lawde \n                   Time: %H:%M:%S \n                   Date: %d/%m/%y "
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 35)
        drawn_text.text((200, 250), current_time, font=fnt, fill=(230, 230, 250))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)

            await asyncio.sleep(15)
        except BaseException:
            return
