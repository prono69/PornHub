"""PepeBot Module for Finding Songs"""

import asyncio
import glob
import os
import subprocess

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from uniborg import MODULE, SYNTAX
from uniborg.util import admin_cmd

MODULE.append("song")
try:
    import subprocess
except BaseException:
    os.system("pip install instantmusic")


os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s " + name)


@borg.on(admin_cmd(pattern="song(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    await event.edit("searching song..please wait")
    bruh(str(cmd))
    l = glob.glob("*.mp3")
    loa = l[0]
    await event.edit("sending song")
    await event.client.send_file(
        event.chat_id,
        loa,
        force_document=True,
        allow_cache=False,
        caption=cmd,
        reply_to=reply_to_id,
    )
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3", shell=True)


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


SYNTAX.update(
    {
        "music": "`.song` <search title>\
            \nUsage: For searching songs.\
            \n\n`.spd`<Artist - Song Title>\
            \nUsage:For searching songs from Spotify.\
            \n\n`.netease` <Artist - Song Title>\
            \nUsage:Download music with @WooMaiBot\
            \n\n`.dzd` <Spotify/Deezer Link>\
            \nUsage:Download music from Spotify or Deezer."
    }
)
