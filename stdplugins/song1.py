"get music from .gaana\n.spotbot <music query>  Credits https://t.me/By_Azade"
import logging

from telethon import events

from uniborg import MODULE
from uniborg.util import admin_cmd

MODULE.append("song1")

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)
logger = logging.getLogger(__name__)


@borg.on(admin_cmd(pattern="gaana ?(.*)"))  # pylint:disable=E0602
async def music_find(event):
    if event.fwd_from:
        return

    music_name = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if music_name:
        await event.delete()
        song_result = await event.client.inline_query("deezermusicbot", music_name)

        await song_result[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )
    elif msg:
        await event.delete()
        song_result = await event.client.inline_query("deezermusicbot", msg.message)

        await song_result[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )


@borg.on(admin_cmd(pattern="spotbot ?(.*)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    msg = await event.get_reply_message()
    await event.delete()

    music_name = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if music_name:
        await event.delete()
        song_result = await event.client.inline_query("spotify_to_mp3_bot", music_name)

        for item_ in song_result:

            if "(FLAC)" in item_.title:

                j = await item_.click(
                    event.chat_id,
                    reply_to=event.reply_to_msg_id,
                    hide_via=True,
                )

                k = await event.respond(j)
                await j.delete()
                await k.edit("`Error Sar`")

            elif "(MP3_320)" in item_.title:

                j = await item_.click(
                    event.chat_id,
                    reply_to=event.reply_to_msg_id,
                    hide_via=True,
                )

                k = await event.respond(j)
                await j.delete()
                await k.edit("`Error Sar`")

            elif "(MP3_128)" in item_.title:

                j = await item_.click(
                    event.chat_id,
                    reply_to=event.reply_to_msg_id,
                    hide_via=True,
                )

                k = await event.respond(j)
                await j.delete()
                await k.edit("`Error Sar`")

    elif msg:

        await event.delete()
        song_result = await event.client.inline_query("spotify_to_mp3_bot", msg.message)
        for item in song_result:

            if "(FLAC)" in item.title:

                j = await item.click(
                    event.chat_id,
                    reply_to=event.reply_to_msg_id,
                    hide_via=True,
                )

                k = await event.respond(j)
                await j.delete()
                await k.edit("`Error Sar`")

            elif "(MP3_320)" in item.title:

                j = await item.click(
                    event.chat_id,
                    reply_to=event.reply_to_msg_id,
                    hide_via=True,
                )

                k = await event.respond(j)
                await j.delete()
                await k.edit("`Error Sar`")

            elif "(MP3_128)" in item.title:

                j = await item.click(
                    event.chat_id,
                    reply_to=event.reply_to_msg_id,
                    hide_via=True,
                )

                k = await event.respond(j)
                await j.delete()
                await k.edit("`Error Sar`")


@borg.on(admin_cmd(pattern="ad ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("```reply to media message```")
        return
    chat = "@audiotubebot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=507379365)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @AudioTubeBot and try again```")
            return
        await event.delete()
        await event.client.send_file(event.chat_id, response.message.media)
