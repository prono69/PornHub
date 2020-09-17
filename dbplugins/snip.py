"""Snips
Available Commands:
.snips
.snipl
.snipd"""

import logging

from sample_config import Config
from sql_helpers.snips_sql import add_snip, get_all_snips, get_snips, remove_snip
from uniborg.util import admin_cmd

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)
logger = logging.getLogger(__name__)


@borg.on(admin_cmd(pattern=r"\#(\S+)", outgoing=True))
async def on_snip(event):
    name = event.pattern_match.group(1)
    snip = get_snips(name)
    if not event.is_group:
        await event.delete()
    reply_message = await event.get_reply_message()
    if snip:
        msg_o = await event.client.get_messages(
            entity=Config.PRIVATE_CHANNEL_BOT_API_ID, ids=int(snip.f_mesg_id)
        )
        if msg_o.media is not None:
            if reply_message:
                await event.client.send_file(
                    event.chat_id,
                    msg_o.media,
                    supports_streaming=True,
                    reply_to=reply_message.id,
                )
            else:
                await event.client.send_file(
                    event.chat_id, msg_o.media, supports_streaming=True
                )
        else:
            if reply_message:
                await event.client.send_message(
                    entity=event.chat_id,
                    message=msg_o.message,
                    reply_to=reply_message.id,
                )
            else:
                await event.client.send_message(
                    entity=event.chat_id, message=msg_o.message
                )


@borg.on(admin_cmd(pattern="snips (.*)"))
async def on_snip_save(event):
    name = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if not name:
        return await event.edit("`No Keyword Provided`")
    if msg:
        msg_o = await event.client.forward_messages(
            entity=Config.PRIVATE_CHANNEL_BOT_API_ID,
            messages=msg,
            from_peer=event.chat_id,
            silent=True,
        )
        add_snip(name, msg_o.id)
        await event.edit(
            "`Saved successfully`. Get it with `#{name}`".format(name=name)
        )
    else:
        await event.edit("Reply to a message with `snips keyword` to save the snip")


@borg.on(admin_cmd(pattern="snipl"))
async def on_snip_list(event):
    all_snips = get_all_snips()
    OUT_STR = "Available Snips:\n\n"
    if len(all_snips) > 0:
        for a_snip in all_snips:
            OUT_STR += f"~ `#{a_snip.snip}` \n"
    else:
        OUT_STR = "No Snips. Start Saving using `.snips`"
    if len(OUT_STR) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "snips.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Available Snips",
                reply_to=event,
            )
            await event.delete()
    else:
        await event.edit(OUT_STR)


@borg.on(admin_cmd(pattern=r"snipd (\S+)"))
async def on_snip_delete(event):
    name = event.pattern_match.group(1)
    remove_snip(name)
    await event.edit("Snip `#{}` deleted successfully".format(name))
