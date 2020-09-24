"""IX.IO pastebin like site
Syntax: .paste
        .getp <to get the dogbin content>"""
import logging
import os
from datetime import datetime

import requests

from uniborg.util import admin_cmd
from userbot import AioHttp

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.WARN
)


def progress(current, total):
    logger.info(
        "Downloaded {} of {}\nCompleted {}".format(
            current, total, (current / total) * 100
        )
    )


DOGBIN_URL = "https://del.dog/"
BOTLOG = Config.PM_LOGGR_BOT_API_ID


@borg.on(admin_cmd(pattern="paste ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    input_str = event.pattern_match.group(1)
    message = "SYNTAX: `.paste <long text to include>`"
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await previous_message.download_media(
                Config.TMP_DOWNLOAD_DIRECTORY,
                progress_callback=progress,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8")
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        message = "SYNTAX: `.paste <long text to include>`"
    url = "https://del.dog/documents"
    r = requests.post(url, data=message.encode("UTF-8")).json()
    url = f"https://del.dog/{r['key']}"
    raw_url = f"https://del.dog/raw/{r['key']}"
    end = datetime.now()
    ms = (end - start).seconds
    if r["isUrl"]:
        nurl = f"https://del.dog/v/{r['key']}"
        await event.edit(
            "Dogged to {} in {} seconds. GoTo Original URL: {}".format(url, ms, nurl)
        )
    else:
        await event.edit(
            "`Pasted Successfully!` \n**LINK:** [URL]({}) | **RAW:** [URL]({})\n__Link Generated In__ **{}** __seconds__".format(
                url, raw_url, ms
            )
        )


@borg.on(admin_cmd(pattern="getp ?(.*)"))
async def get_dogbin_content(dog_url):
    """For .get_dogbin_content command,
    fetches the content of a dogbin URL."""
    textx = await dog_url.get_reply_message()
    link = dog_url.pattern_match.group(1)
    await dog_url.edit("`Getting dogbin content...`")

    if textx:
        link = str(textx.message)

    format_view = f"{DOGBIN_URL}v/"

    if link.startswith(format_view):
        link = link[len(format_view) :]
        raw_link = f"https://del.dog/raw/{link}"
    elif link.startswith("https://del.dog/"):
        link = link[len("https://del.dog/") :]
        raw_link = f"https://del.dog/raw/{link}"
    elif link.startswith("del.dog/"):
        link = link[len("del.dog/") :]
        raw_link = f"https://del.dog/raw/{link}"
    elif link.startswith("https://nekobin.com/"):
        link = link[len("https://nekobin.com/") :]
        raw_link = f"https://nekobin.com/raw/{link}"
    elif link.startswith("nekobin.com/"):
        link = link[len("nekobin.com/") :]
        raw_link = f"https://nekobin.com/raw/{link}"
    else:
        await dog_url.edit("`Is that even a paste url?`")
        return
    resp = await AioHttp().get_text(raw_link)
    if len(str(resp)) > 4096:
        with io.BytesIO(str.encode(resp)) as out_file:
            out_file.name = "getp.txt"
            await dog_url.client.send_file(dog_url.chat_id, out_file)
            await dog_url.delete()
    else:
        await dog_url.edit(f"**URL content** :\n\n`{resp}`")
    if BOTLOG:
        await dog_url.client.send_message(
            BOTLOG,
            "Get dogbin content query for `"
            + link
            + "` was \
executed successfully",
        )
