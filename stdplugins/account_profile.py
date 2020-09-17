"""Profile Updation Commands
.cbio <Bio>
.cname <Name>
.cpic
.delpfp <number or all>
to delete ur profile pic.
.username <name>
to change ur username.
.photo <number>"""

import datetime
import logging
import os
from datetime import datetime

from telethon.errors.rpcerrorlist import UsernameInvalidError, UsernameOccupiedError
from telethon.tl import functions
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from telethon.tl.types import InputPhoto

from uniborg.util import admin_cmd

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)


@borg.on(admin_cmd(pattern="cbio (.*)"))
async def _(event):
    if event.fwd_from:
        return
    bio = event.pattern_match.group(1)
    try:
        await borg(functions.account.UpdateProfileRequest(about=bio))
        await event.edit("`Succesfully changed My Profile bio`")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


@borg.on(admin_cmd(pattern="cname ((.|\n)*)"))
async def _(event):
    if event.fwd_from:
        return
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if "\\n" in names:
        first_name, last_name = names.split("\\n", 1)
    try:
        await borg(
            functions.account.UpdateProfileRequest(
                first_name=first_name, last_name=last_name
            )
        )
        await event.edit("`My name was changed successfully`")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


@borg.on(admin_cmd(pattern="cpic"))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if reply_message.text:
        await event.edit("`Hey Pro! Are You sure it's a Photo ?`")
        return
    await event.edit("`Downloading Profile Picture/vdo to my local...`")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    photo = None
    try:
        photo = await borg.download_media(reply_message, Config.TMP_DOWNLOAD_DIRECTORY)
    except Exception as e:
        await event.edit(str(e))
    else:
        if photo:
            await event.edit("`Making Profile pic/vdo for U, Nibba...`")
            if photo.endswith((".mp4", ".MP4", ".gif")):
                # https://t.me/tgbetachat/324694
                size = os.stat(photo).st_size
                if size > 2097152:
                    await event.edit("`Size must be less than 2 mb`")
                    os.remove(photo)
                    return
                catpic = None
                catvideo = await borg.upload_file(photo)
            else:
                catpic = await borg.upload_file(photo)
                catvideo = None
            try:
                await borg(
                    functions.photos.UploadProfilePhotoRequest(
                        file=catpic, video=catvideo, video_start_ts=0.01
                    )
                )
            except Exception as e:  # pylint:disable=C0103,W0703
                await event.edit(str(e))
            else:
                await event.edit("`My profile picture was succesfully changed... KEK`")
    try:
        os.remove(photo)
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))


@borg.on(admin_cmd(pattern="delpfp ?(.*)"))
async def remove_profilepic(delpfp):
    """ For .delpfp command, delete your current profile picture in Telegram. """
    group = delpfp.text[8:]
    if group == "all":
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1

    pfplist = await delpfp.client(
        GetUserPhotosRequest(user_id=delpfp.from_id, offset=0, max_id=0, limit=lim)
    )
    input_photos = []
    for sep in pfplist.photos:
        input_photos.append(
            InputPhoto(
                id=sep.id,
                access_hash=sep.access_hash,
                file_reference=sep.file_reference,
            )
        )
    await delpfp.client(DeletePhotosRequest(id=input_photos))
    await delpfp.edit(f"`Successfully deleted {len(input_photos)} profile picture(s).`")


@borg.on(admin_cmd(pattern="username ?(.*)"))
async def update_username(username):
    """ For .username command, set a new username in Telegram. """
    newusername = username.pattern_match.group(1)
    try:
        await username.client(UpdateUsernameRequest(newusername))
        await username.edit("```Your username was succesfully changed.```")
    except UsernameOccupiedError:
        await username.edit("```This username is already taken by a Faking Nibba.```")
    except UsernameInvalidError:
        await username.edit("```This Username is Invalid, U Brainless Creature```")


@borg.on(admin_cmd(pattern="photo ?(.*)"))
async def _(event):
    """getting user profile photo last changed time"""
    if event.fwd_from:
        return
    p_number = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    if event.is_group:
        entity = await event.client.get_entity(reply_message.from_id)
        try:
            a = await event.edit("`Getting profile pic changed or added date`")
            photos = await event.client.get_profile_photos(entity)
            if photos.total == 0:
                await event.edit("`This user has no profile photos.`")
            else:
                msg = photos[int(p_number)].date
                print(msg)
                d = datetime.datetime.strptime(str(msg), "%Y-%m-%d %H:%M:%S%z")
                d = d.replace(tzinfo=datetime.timezone.utc)
                d = d.astimezone()
                msg_utc = d.strftime("%d %m %Y %H:%M:%S")
                msg = "Last profile photo changed: \n👉 `{}` `UTC+5:30`".format(
                    str(msg_utc)
                )
                await a.edit(msg)
        except BaseException:
            pass

    else:
        entity = await event.client.get_entity(event.chat_id)
        try:
            a = await event.edit("`Getting profile pic changed or added date`")
            photos = await borg.get_profile_photos(entity)
            if photos.total == 0:
                await event.edit("`This user has no profile photos.`")
            else:
                msg = photos[int(p_number)].date
                d = datetime.datetime.strptime(str(msg), "%Y-%m-%d %H:%M:%S%z")
                d = d.replace(tzinfo=datetime.timezone.utc)
                d = d.astimezone()
                msg_utc = d.strftime("%d %m %Y %H:%M:%S")
                msg = "Last profile photo changed: \n👉 `{}` `UTC+5:30`".format(
                    str(msg_utc)
                )
                await a.edit(msg)
        except BaseException:
            pass
