# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import asyncio
import logging
import os
import traceback
from datetime import datetime

from uniborg import util

thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)
logger = logging.getLogger(__name__)
DELETE_TIMEOUT = 5


@borg.on(util.admin_cmd(pattern=r"load (?P<shortname>\w+)$"))
async def load_reload(event):
    await event.delete()
    shortname = event.pattern_match["shortname"]
    try:
        if shortname in borg._plugins:
            borg.remove_plugin(shortname)
        borg.load_plugin(shortname)
        msg = await event.respond(f"Successfully (re)loaded plugin `{shortname}`")
        await asyncio.sleep(DELETE_TIMEOUT)
        await msg.delete()
    except Exception as e:  # pylint:disable=C0103,W0703
        trace_back = traceback.format_exc()

        logger.warn(f"Failed to (re)load plugin {shortname}: {trace_back}")
        await event.respond(f"Failed to (re)load plugin {shortname}: {e}")


@borg.on(util.admin_cmd(pattern=r"(?:unload|remove) (?P<shortname>\w+)$"))
async def remove(event):
    await event.delete()
    shortname = event.pattern_match["shortname"]
    if shortname == "_core":
        msg = await event.respond(f"Not removing {shortname}")
    elif shortname in borg._plugins:
        borg.remove_plugin(shortname)
        msg = await event.respond(f"`Removed plugin {shortname}`")
    else:
        msg = await event.respond(f"Plugin {shortname} is not loaded")
    await asyncio.sleep(DELETE_TIMEOUT)
    await msg.delete()


@borg.on(util.admin_cmd(pattern=r"send (?P<shortname>\w+)$"))
async def send_plug_in(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    input_str = event.pattern_match["shortname"]
    the_plugin_file = "./stdplugins/{}.py".format(input_str)
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    if os.path.exists(the_plugin_file):
        start = datetime.now()
        await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            caption="©️ @LazyAF_Pepe",
            reply_to=message_id,
            thumb=thumb,
        )
        end = datetime.now()
        time_taken_in_ms = (end - start).seconds
        await event.edit(
            "Ok, BTC Uploaded {} in {} seconds".format(input_str, time_taken_in_ms)
        )
        await asyncio.sleep(DELETE_TIMEOUT)
        await event.delete()
    else:
        await event.edit("**404:** `File Not Found`")


@borg.on(util.admin_cmd(pattern="install"))
async def install_plug_in(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(
                await event.get_reply_message(), borg.n_plugin_path
            )
            if "(" not in downloaded_file_name:
                borg.load_plugin_from_file(downloaded_file_name)
                await event.edit(
                    "Installed temp Plugin `{}`".format(
                        os.path.basename(downloaded_file_name)
                    )
                )
            else:
                os.remove(downloaded_file_name)
                await event.edit("`Abe Sale ! Plugin already exists, Can't instll`")
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()
