# created by @KeselekPermen69
"""Type - `.nhentai` (link/code)
To view hentai manga in telegra.ph format. xD:)"""

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="nhentai(?: |$)(.*)"))
async def _(event):
    # Prevent Channel Bug to run nhentai commad
    if event.is_channel and not event.is_group:
        await event.edit("`Bish! nhentai Command isn't permitted on channels`")
        return
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    if not link:
        await event.edit("`Bish! Put a nHentai code or link`")
        return
    chat = "@nHentaiBot"
    await event.edit("```Processing...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=424466890)
            )
            await event.client.send_message(chat, link)
            response = await response
            # Now bot can't send Notification :)
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.reply("```Please unblock @nHentaiBot and try again```")
            return
        if response.text.startswith("**Sorry I couldn't get manga from**"):
            await event.edit("```Bish! I think this is not the right link/code```")
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)
            await event.client.send_read_acknowledge(event.chat_id)
