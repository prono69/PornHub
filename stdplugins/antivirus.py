# Lots of lub to @r4v4n4 for gibing the base <3
# copied from @A_Dark_Prince3

"""Type .scan
\nReply to a file/media."""
import logging

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from uniborg.util import admin_cmd

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.WARN
)


@borg.on(admin_cmd(pattern="scan ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to a file to Scan !```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("```Reply to a media message```")
        return
    chat = "@DrWebBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit(" `Sliding my tip, of fingers over it`")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=161163358)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @DrWebBot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            if response.text.startswith("Select"):
                await event.edit("`Please go to` @DrWebBot `and select your language.`")
            else:
                await event.edit(
                    f"**Antivirus scan was completed. I got dem final results.**\n {response.message.message}"
                )
