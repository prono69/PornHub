# modified by @UniBorg
from telethon.tl.types import Channel, Chat, User

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="res ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to a Link.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.entities:
        await event.edit("```Reply to a Link```")
        return
    # chat = "@CheckRestrictionsBot"
    reply_entity = reply_message.entities[0]
    reply_res = reply_message.text[
        reply_entity.offset : reply_entity.offset + reply_entity.length
    ]
    rr = await event.client.get_entity(reply_res)
    await event.edit(get_restriction_string(rr))


def get_restriction_string(a) -> str:
    b = ""
    c = ""
    if isinstance(a, Channel):
        c = f"[{a.title}](https://t.me/c/{a.id}/{2})"
    elif isinstance(a, User):
        c = f"[{a.first_name}](tg://user?id={a.id})"
    elif isinstance(a, Chat):
        c = f"{a.title}"
        b = f"{c}: basic groups do not have restriction, to the best of my knowledge"
        return b
    else:
        c = "__UN-KNOWN__"
    if a.restriction_reason is None or len(a.restriction_reason) == 0:
        b = "{}: Good News! No Limitations are currently applied to this @CheckRestrictionsBot".format(
            c
        )
        # plox: do not remove -_- this credit. thx.!
    else:
        tmp_string = f"{c} has the following restriction_reason(s): \n"
        for a_r in a.restriction_reason:
            tmp_string += f"👉 {a_r.reason}-{a_r.platform}: {a_r.text}\n\n"
        b = tmp_string
    return b
