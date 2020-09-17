import asyncio
import io
import time
from datetime import datetime

from sample_config import Config
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern=("cmrdl ?(.*)")))
async def _(event):
    url = event.pattern_match.group(1)
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    await event.edit("Processing ...")
    datetime.now()
    await event.get_reply_message()
    time.time()
    Config.TMP_DOWNLOAD_DIRECTORY
    await event.edit("Finish downloading to my local")
    command_to_exec = f"./bin/cmrudl.py {url} -d ./ravana/"
    reply_to_id = event.message.id
    PROCESS_RUN_TIME = 100
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        command_to_exec, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    logger.info(command_to_exec)
    OUTPUT = "**Files in DOWNLOADS folder:**\n"
    stdout, stderr = await process.communicate()
    stdout.decode().strip()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(stdout) as out_file:
            stdout.decode().strip()
            output = stdout.decode("utf-8").splitlines()
            file_name = output[1]
            file_name = file_name.split()
            full_file_name = file_name[2]
            out_file_name = "./ravana/" + full_file_name
            logger.info(file_name)
            await event.edit("Uploading, please wait!!")
            await borg.send_file(
                event.chat_id,
                out_file_name,
                force_document=True,
                allow_cache=False,
                caption=f"`{full_file_name}`",
                reply_to=reply_to_id,
            )
