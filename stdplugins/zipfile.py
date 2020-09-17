""" command: .zip, .unzip
coded by @By_Azade
"""
import asyncio
import logging
import os
import time
import zipfile
from datetime import datetime

from uniborg.util import admin_cmd, progress

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)
logger = logging.getLogger(__name__)


@borg.on(admin_cmd(pattern=("zip ?(.*)")))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    mone = await event.edit("Zipping in progress....")
    if event.reply_to_msg_id:
        if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
            os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
        reply_message = await event.get_reply_message()
        try:
            c_time = time.time()
            downloaded_file_name = await borg.download_media(
                reply_message,
                Config.TMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "trying to download")
                ),
            )
            directory_name = downloaded_file_name
            await event.edit("Finish downloading to my local")
            zipfile.ZipFile(directory_name + ".zip", "w", zipfile.ZIP_DEFLATED).write(
                directory_name
            )
            os.remove(directory_name)
            cat = directory_name + ".zip"
            await event.edit(f"compressed successfully into `{cat}`")
        except Exception as e:  # pylint:disable=C0103,W0703
            await mone.edit(str(e))
    elif input_str:
        if not os.path.exists(input_str):
            await event.edit(
                f"There is no such directory or file with the name `{input_str}` check again"
            )
            return
        filePaths = zipdir(input_str)
        zip_file = zipfile.ZipFile(input_str + ".zip", "w")
        with zip_file:
            for file in filePaths:
                zip_file.write(file)
        await event.edit("Local file compressed to `{}`".format(input_str + ".zip"))


@borg.on(admin_cmd(pattern="unzip ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    mone = await event.edit("`Unzipping...`")
    input_str = event.pattern_match.group(1)
    if input_str:
        if os.path.exists(input_str):
            downloaded_file_name = input_str
            start = datetime.now()
            with zipfile.ZipFile(downloaded_file_name, "r") as zip_ref:
                zip_ref.extractall(Config.TMP_DOWNLOAD_DIRECTORY)
            end = datetime.now()
            ms = (end - start).seconds
            await event.edit(
                f"unzipped and stored to `{downloaded_file_name[:-4]}` \n**Time Taken :** `{ms} seconds`"
            )
        else:
            await event.edit(f"I can't find that path `{input_str}`")
    else:
        if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
            os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
        if event.reply_to_msg_id:
            start = datetime.now()
            reply_message = await event.get_reply_message()
            try:
                c_time = time.time()
                downloaded_file_name = await borg.download_media(
                    reply_message,
                    Config.TMP_DOWNLOAD_DIRECTORY,
                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        progress(d, t, mone, c_time, "trying to download")
                    ),
                )
            except Exception as e:  # pylint:disable=C0103,W0703
                await mone.edit(str(e))
            await event.edit("Unzipping now")
            with zipfile.ZipFile(downloaded_file_name, "r") as zip_ref:
                zip_ref.extractall(Config.TMP_DOWNLOAD_DIRECTORY)
            end = datetime.now()
            ms = (end - start).seconds
            await event.edit(
                f"unzipped and stored to `{downloaded_file_name[:-4]}` \n**Time Taken :** `{ms} seconds`"
            )
            os.remove(downloaded_file_name)


def zipdir(dirName):
    filePaths = []
    for root, directories, files in os.walk(dirName):
        for filename in files:
            filePath = os.path.join(root, filename)
            filePaths.append(filePath)
    return filePaths
