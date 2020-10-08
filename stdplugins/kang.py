"""Make / Download Telegram Sticker Packs without installing Third Party applications
Available Commands:
.kang [Optional Emoji]
.packinfo
.loda {for get stickers in a zip file}"""
import asyncio
import datetime
import math
import os
import random
import zipfile
from collections import defaultdict
from io import BytesIO

from PIL import Image
from telethon.errors import MessageNotModifiedError
from telethon.errors.rpcerrorlist import StickersetInvalidError
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import (
    DocumentAttributeSticker,
    InputStickerSetID,
    InputStickerSetShortName,
    MessageMediaPhoto,
)

from uniborg.util import admin_cmd

KANGING_STR = [
    "`Using Witchery to kang this sticker...`",
    "`Plagiarising hehe...`",
    "`Aaham Brahmassami................`",
    "`Inviting this sticker over to my pack...`",
    "`Kanging this sticker...`",
    "`Hey that's a nice sticker!\nMind if I kang?!..`",
    "`hehe me stel ur stikér\nhehe.`",
    "`Ay look over there (☉｡☉)!→\nWhile I kang this...`",
    "`Roses are red violets are blue, kanging this sticker so my pacc looks cool`",
    "`Imprisoning this sticker...`",
    "`Mr.Steal Your Sticker is stealing this sticker...`",
    "`I am Stealing your Sticker.....\nGand Marao...`",
    "Why u bullin me.....\nರ╭╮ರ`",
    "`BOOM.... HEADSHOT...\n(ノಠ益ಠ)ノ...\n(⌐■-■)`",
    "`Me is having sux with ur GF....\nU can't du nthing...Hehe..\nಠ∀ಠ...(≧▽≦)`",
    "`Aise tukur tukur kahe Dekh raha hain`",
]


@borg.on(admin_cmd(pattern="kang ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.is_reply:
        await event.edit("Reply to a photo to add to my personal sticker pack.")
        return
    reply_message = await event.get_reply_message()
    sticker_emoji = "🍆"
    input_str = event.pattern_match.group(1)
    if input_str:
        sticker_emoji = input_str

    me = borg.me
    name = me.username
    userid = event.from_id
    packname = f"@{name}'s lawde Part3"
    packshortname = f"puretaboo_gengbeng{userid}"  # format: Uni_Borg_userid

    is_a_s = is_it_animated_sticker(reply_message)
    file_ext_ns_ion = "chutiya_Sticker.png"
    file = await borg.download_file(reply_message.media)
    uploaded_sticker = None
    if is_a_s:
        file_ext_ns_ion = "AnimatedSticker.tgs"
        uploaded_sticker = await borg.upload_file(file, file_name=file_ext_ns_ion)
        packname = "nikal_lawde_AnimatedStickers"
        packshortname = "kirito6969_Animated"  # format: Uni_Borg_userid_as
    elif not is_message_image(reply_message):
        await event.edit("Invalid message type")
        return
    else:
        with BytesIO(file) as mem_file, BytesIO() as sticker:
            resize_image(mem_file, sticker)
            sticker.seek(0)
            uploaded_sticker = await borg.upload_file(
                sticker, file_name=file_ext_ns_ion
            )

    await event.edit(random.choice(KANGING_STR))

    async with borg.conversation("@Stickers") as bot_conv:
        now = datetime.datetime.now()
        dt = now + datetime.timedelta(minutes=1)
        if not await stickerset_exists(bot_conv, packshortname):
            await silently_send_message(bot_conv, "/cancel")
            if is_a_s:
                response = await silently_send_message(bot_conv, "/newanimated")
            else:
                response = await silently_send_message(bot_conv, "/newpack")
            if "Yay!" not in response.text:
                await event.edit(f"**FAILED**! @Stickers replied: {response.text}")
                return
            response = await silently_send_message(bot_conv, packname)
            if not response.text.startswith("Alright!"):
                await event.edit(f"**FAILED**! @Stickers replied: {response.text}")
                return
            await bot_conv.send_file(
                file=uploaded_sticker, allow_cache=False, force_document=True
            )
            response = await bot_conv.get_response()
            if "Sorry" in response.text:
                await event.edit(f"**FAILED**! @Stickers replied: {response.text}")
                return
            await silently_send_message(bot_conv, sticker_emoji)
            await silently_send_message(bot_conv, "/publish")
            response = await silently_send_message(bot_conv, f"<{packname}>")
            await silently_send_message(bot_conv, "/skip")
            response = await silently_send_message(bot_conv, packshortname)
            if response.text == "Sorry, this short name is already taken.":
                await event.edit(f"**FAILED**! @Stickers replied: {response.text}")
                return
        else:
            await silently_send_message(bot_conv, "/cancel")
            await silently_send_message(bot_conv, "/addsticker")
            esnopre = await silently_send_message(bot_conv, packshortname)
            if "Alright!" not in esnopre.text:
                await event.edit(f"**FAILED**! @Stickers replied: {esnopre.text}")
                return
            await bot_conv.send_file(
                file=uploaded_sticker, allow_cache=False, force_document=True
            )
            response = await bot_conv.get_response()
            if "Sorry" in response.text:
                await event.edit(f"**FAILED**! @Stickers replied: {response.text}")
                return
            await silently_send_message(bot_conv, sticker_emoji)
            await silently_send_message(bot_conv, "/done")

    await event.edit(
        f"`This Sticker Is Raped! Plox Help this Sticker by Clicking` [HERE](t.me/addstickers/{packshortname})"
    )
    
    
# Helpers


def is_it_animated_sticker(message):
    try:
        if message.media and message.media.document:
            mime_type = message.media.document.mime_type
            return "tgsticker" in mime_type
        else:
            return False
    except BaseException:
        return False


def is_message_image(message):
    if message.media:
        if isinstance(message.media, MessageMediaPhoto):
            return True
        return bool(
            message.media.document
            and message.media.document.mime_type.split("/")[0] == "image"
        )

    return False


async def silently_send_message(conv, text):
    await conv.send_message(text)
    response = await conv.get_response()
    await conv.mark_read(message=response)
    return response


async def stickerset_exists(conv, setname):
    try:
        await borg(GetStickerSetRequest(InputStickerSetShortName(setname)))
        response = await silently_send_message(conv, "/addsticker")
        if response.text == "Invalid pack selected.":
            await silently_send_message(conv, "/cancel")
            return False
        await silently_send_message(conv, "/cancel")
        return True
    except StickersetInvalidError:
        return False


def resize_image(image, save_locaton):
    """Copyright Rhyse Simpson:
    https://github.com/skittles9823/SkittBot/blob/master/tg_bot/modules/stickers.py
    """
    im = Image.open(image)
    if (im.width and im.height) < 512:
        size1 = im.width
        size2 = im.height
        if size1 > size2:
            scale = 512 / size1
            size1new = 512
            size2new = size2 * scale
        else:
            scale = 512 / size2
            size1new = size1 * scale
            size2new = 512
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        im = im.resize(sizenew)
    else:
        maxsize = (512, 512)
        im.thumbnail(maxsize)
    im.save(save_locaton, "PNG")


def progress(current, total):
    logger.info(
        "Uploaded: {} of {}\nCompleted {}".format(
            current, total, (current / total) * 100
        )
    )


def find_instance(items, class_or_tuple):
    for item in items:
        if isinstance(item, class_or_tuple):
            return item
    return None


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            os.remove(os.path.join(root, file))
