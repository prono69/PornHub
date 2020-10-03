""" Userbot initialization. """

import json
import os
import re
import time
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger

import aiohttp
import requests
from pySmartDL import SmartDL
from telethon import TelegramClient
from telethon.sessions import StringSession

from sample_config import Config
from userbot.fonts import *
from userbot.functions import *

StartTime = time.time()
pepe = "3.0.0"

if Config.HU_STRING_SESSION:
    session_name = str(Config.HU_STRING_SESSION)
    if session_name.endswith("="):
        bot = TelegramClient(
            StringSession(session_name), Config.APP_ID, Config.API_HASH
        )
    else:
        bot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
        ).start(bot_token=Config.HU_STRING_SESSION)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Config.APP_ID, Config.API_HASH)

CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
    )
LOGS = getLogger(__name__)

PEPE_ID = ["790841356", "986755683", "880678601"]


class AioHttp:
    @staticmethod
    async def get_json(link):
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                return await resp.json()

    @staticmethod
    async def get_text(link):
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                return await resp.text()

    @staticmethod
    async def get_json_from_text(link):
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                text = await resp.text()
                return json.loads(text)

    @staticmethod
    async def get_raw(link):
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                return await resp.read()

    @staticmethod
    async def get_url(link):
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                return resp.url


EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+"
)


def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, "", inputString)


if not os.path.exists("bin"):
    os.mkdir("bin")
binaries = {
    "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown": "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py": "bin/cmrudl",
    "https://raw.githubusercontent.com/adekmaulana/python-scripts/master/shell/megadirect": "bin/megadirect",
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "min", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time


if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "thumb_image.jpg"
# thumb image
with open(thumb_image_path, "wb") as f:
    f.write(requests.get(Config.THUMB_IMG).content)
