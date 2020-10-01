"""PepeBot Module for Finding Songs"""

import asyncio
import logging

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from uniborg import MODULE, SYNTAX
from uniborg.util import admin_cmd

MODULE.append("song")

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)
logger = logging.getLogger(__name__)


@borg.on(admin_cmd(pattern="spd(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    chat = "@SpotifyMusicDownloaderbot"
    await event.edit("```Getting Your Music```")
    async with event.client.conversation(chat) as conv:
        await asyncio.sleep(2)
        await event.edit("`Downloading music taking some times,  Stay Tuned.....`")
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=752979930)
            )
            await event.client.send_message(chat, name)
            respond = await response
        except YouBlockedUserError:
            await event.reply(
                "```Please unblock @SpotifyMusicDownloaderBot and try again```"
            )
            return
        await event.delete()
        await event.client.send_message(event.chat_id, respond.message)


@borg.on(admin_cmd(pattern="netease(?: |$)(.*)"))
async def WooMai(netase):
    if netase.fwd_from:
        return
    song = netase.pattern_match.group(1)
    chat = "@WooMaiBot"
    link = f"/netease {song}"
    await netase.edit("```Getting Your Music```")
    async with netase.client.conversation(chat) as conv:
        await asyncio.sleep(2)
        await netase.edit("`Downloading...Please wait`")
        try:
            msg = await conv.send_message(link)
            response = await conv.get_response()
            respond = await conv.get_response()
            """ - don't spam notif - """
            await netase.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await netase.reply("```Please unblock @WooMaiBot and try again```")
            return
        await netase.edit("`Sending Your Music...`")
        await asyncio.sleep(3)
        await netase.client.send_file(netase.chat_id, respond)
    await netase.client.delete_messages(conv.chat_id, [msg.id, response.id, respond.id])
    await netase.delete()


@borg.on(admin_cmd(pattern="dzd(?: |$)(.*)"))
async def DeezLoader(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` I need a link to download something pro.`**(._.)**")
    else:
        await event.edit("**Initiating Download!**")
    chat = "@DeezLoadBot"
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.get_response()
            await conv.send_message(d_link)
            details = await conv.get_response()
            song = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @DeezLoadBot `and retry!`")
            return
        await event.client.send_file(event.chat_id, song, caption=details.text)
        # await evwnt.client.delete_messages(conv.chat_id,
        # [msg_start.id, response.id, r.id, msg.id, details.id, song.id])
        await event.delete()


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


SYNTAX.update(
    {
        "music": "`.song` <search title>\
            \nUsage: For searching songs.\
            \n\n`.spd`<Artist - Song Title>\
            \nUsage:For searching songs from Spotify.\
            \n\n`.netease` <Artist - Song Title>\
            \nUsage:Download music with @WooMaiBot\
            \n\n`.dzd` <Spotify/Deezer Link>\
            \nUsage:Download music from Spotify or Deezer.\
            \n\n`.gaana` <Query>\
            \n\n`.spotbot` <query>\
            \n\n`.ad`"
    }
)
