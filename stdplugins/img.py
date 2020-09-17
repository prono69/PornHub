# Adapted from OpenUserBot for Uniborg

"""Download & Upload Images on Telegram\n
Syntax: `.img <number> <Name>` or `.img <number> (replied message)`
\n Upgraded and Google Image Error Fixed by @kirito6969
"""

import os
import shutil
from re import findall

from uniborg.util import admin_cmd
from userbot.utils.google_images_download import googleimagesdownload


@borg.on(admin_cmd(pattern=r"img ?(\d+)? ?(.*)?"))
async def img_sampler(event):
    await event.edit("`Processing Bsdk..`")
    reply = await event.get_reply_message()
    if event.pattern_match.group(2):
        query = event.pattern_match.group(2)
    elif reply:
        query = reply.message
    else:
        await event.edit("`What I am Supposed to Search u Dumb Ass(Donkey)`")
        return

    lim = findall(r"lim=\d+", query)
    lim = event.pattern_match.group(1)
    try:
        lim = lim[0]
        lim = lim.replace("lim=", "")
        query = query.replace("lim=" + lim[0], "")
    except IndexError:
        lim = 5
    response = googleimagesdownload()

    # creating list of arguments
    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory",
    }

    # passing the arguments to the function
    paths = response.download(arguments)
    lst = paths[0][query]
    await event.client.send_file(
        await event.client.get_input_entity(event.chat_id), lst
    )
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await event.delete()
