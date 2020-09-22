"""Command: .repo"""
from telethon.tl.types import ChannelParticipantsAdmins

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="repo"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Link To The Custom Forked Repo:** https://github.com/prono69/PepeBot "
    chat = await event.get_input_chat()
    async for _ in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
