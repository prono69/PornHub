"""
Files Batch Uploader Plugin for userbot.
usage:- .upb
Note:- set TEMP_DIR in Your ENV Vars First.
By:-@Zero_cool7870

"""
import os

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.upb", outgoing=True))
async def batch_upload(event):
    if event.fwd_from:
        return
    temp_dir = Config.TEMP_DIR
    if os.path.exists(temp_dir):
        files = sorted(os.listdir(temp_dir))
        await event.edit("Uploading Files on Telegram...")
        for file in files:
            required_file_name = temp_dir + "/" + file
            print(required_file_name)
            await borg.send_file(event.chat_id, required_file_name, force_document=True)
    else:
        await event.edit("Directory Not Found.")
        return
    await event.edit("Successfullllll.")
