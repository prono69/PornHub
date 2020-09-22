"""Type `.df` or `.df <1-9>` reply to a photo or sticker
"""
from telethon.errors.rpcerrorlist import YouBlockedUserError

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="df(:? |$)(.*)?"))
async def _(event):
    await event.edit("`Destroying Image...`")
    level = event.pattern_match.group(2)
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Reaply to an Image Nigga`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`I am not going to Destroy a Media :)`")
        return
    chat = "@image_deepfrybot"
    await event.edit("```Final Nuking...```")
    event.message.reply_to_msg_id
    msg_reply = None
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(reply_message)
            if level:
                m = f"/deepfry {level}"
                msg_reply = await conv.send_message(m, reply_to=msg.id)
                r = await conv.get_response()
            elif reply_message.gif:
                m = "/deepfry"
                msg_reply = await conv.send_message(m, reply_to=msg.id)
                r = await conv.get_response()
            response = await conv.get_response()
            """ Don't spam notification """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.reply("`Please unblock` @image_deepfrybot`...`")
            return
        if response.text.startswith("Couldn't"):
            await event.edit("`Send Image Plox`")
            await event.client.delete_messages(
                conv.chat_id, [msg.id, response.id, r.id, msg_reply.id]
            )
            return
        else:
            await event.client.send_file(event.chat_id, response)
