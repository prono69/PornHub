# Credits @TheKneesocks

import html

from telethon import events
from telethon.tl.types import User
from telethon.utils import get_display_name


@borg.on(events.NewMessage(pattern=r"\.iid(?: (.+))?", outgoing=True))
async def get_id(e):
    custom = e.pattern_match.group(1)
    if custom:
        try:
            custom = int(custom)
        except ValueError:
            pass
        try:
            en = await e.client.get_entity(custom)
        except ValueError:
            await e.edit("err \\\nUnknown entity")
            return
        id = await e.client.get_peer_id(en)
        text = html.escape(get_display_name(en))
        if isinstance(en, User):
            text = f'<a href="tg://user?id={id}">{text}</a>'
        elif getattr(en, "username", None):
            text = f'<a href="tg://resolve?domain={en.username}">{text}</a>'
        text += f"'s ID: <code>{id}</code>"
        await e.edit(text, parse_mode="HTML")
        return
    text = f"👥 ChatID[<code>{e.chat_id}</code>]\n"
    text += f"💬 MessageID[<code>{e.id}</code>]\n"
    text += f'🙋‍♂️ YourID[<code>{e.from_id}</code>, <a href="tg://user?id={e.from_id}">link</a>]\n'
    if e.is_reply:
        text += "\n"
        r = await e.get_reply_message()
        text += f"RepliedMessageID[<code>{r.id}</code>]\n"
        text += f'RepliedSenderID[<code>{r.from_id}</code>, <a href="tg://user?id={r.from_id}">link</a>]\n'
        if getattr(r.fwd_from, "from_id", None):
            text += f'RepliedForwardSenderID[<code>{r.fwd_from.from_id}</code>, <a href="tg://user?id={r.fwd_from.from_id}">link</a>]\n'
    await e.edit(text, parse_mode="HTML")
