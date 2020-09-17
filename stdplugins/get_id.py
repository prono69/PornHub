"""Get ID of any Telegram media, or any user
Syntax: .g_id"""
from telethon.utils import pack_bot_file_id

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="g_id"))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await event.edit(
                "👥 **Chat ID**: `{}`\n🙋‍♂️ **From User ID**: `{}`\n📄 **File ID**: `{}`".format(
                    str(event.chat_id), str(r_msg.from_id), bot_api_file_id
                )
            )
        else:
            await event.edit(
                "👥 **Chat ID**: `{}`\n🙋‍♂️ **From User ID**: `{}`".format(
                    str(event.chat_id), str(r_msg.from_id)
                )
            )
    else:
        await event.edit("👥 **Chat ID**: `{}`".format(str(event.chat_id)))
