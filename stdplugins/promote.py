"""Reply to a user to .premote / .demote / .prankpremote them in the current chat"""
from datetime import datetime

from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="prankpremote ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    datetime.now()
    to_prankpremote_id = None
    rights = ChatAdminRights()
    input_str = event.pattern_match.group(1)
    reply_msg_id = event.message.id
    if reply_msg_id:
        r_mesg = await event.get_reply_message()
        to_prankpremote_id = r_mesg.sender_id
    elif input_str:
        to_prankpremote_id = input_str
    try:
        await borg(EditAdminRequest(event.chat_id, to_prankpremote_id, rights, ""))
    except (Exception) as exc:
        await event.edit(str(exc))
    else:
        await event.edit("`Successfully Promoted`")
