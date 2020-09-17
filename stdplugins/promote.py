"""Reply to a user to .premote / .demote / .prankpremote them in the current chat"""
from datetime import datetime

from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="premote ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    datetime.now()
    to_premote_id = None
    rights = ChatAdminRights(
        add_admins=False,
        invite_users=True,
        change_info=False,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
    )
    input_str = event.pattern_match.group(1)
    reply_msg_id = event.message.id
    if reply_msg_id:
        r_mesg = await event.get_reply_message()
        to_premote_id = r_mesg.sender_id
    elif input_str:
        to_premote_id = input_str
    try:
        await borg(EditAdminRequest(event.chat_id, to_premote_id, rights, ""))
    except (Exception) as exc:
        await event.edit(str(exc))
    else:
        await event.edit("OwO , `You are Successfully premoted`")


@borg.on(admin_cmd(pattern="demote ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    datetime.now()
    to_demote_id = None
    rights = ChatAdminRights(
        add_admins=None,
        invite_users=None,
        change_info=None,
        ban_users=None,
        delete_messages=None,
        pin_messages=None,
    )
    input_str = event.pattern_match.group(1)
    reply_msg_id = event.message.id
    if reply_msg_id:
        r_mesg = await event.get_reply_message()
        to_demote_id = r_mesg.sender_id
    elif input_str:
        to_demote_id = input_str
    try:
        await borg(EditAdminRequest(event.chat_id, to_demote_id, rights, ""))
    except (Exception) as exc:
        await event.edit(str(exc))
    else:
        await event.edit("｡:ﾟ(;´∩`;)ﾟ:｡ , `Successfully Demoted`")


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
