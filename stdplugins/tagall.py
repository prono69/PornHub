"""Command: .tag optional_text_to_tag_in
You can use it in reply to a message or directly in a new message."""
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="tag ?(.*)"))
async def tag(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        mentions = event.pattern_match.group(1)
    else:
        mentions = "`Helo, How do u do!`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, 50000):
        mentions += f"[\u2063](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        await previous_message.reply(mentions)
    else:
        await event.reply(mentions)
        await event.delete()
