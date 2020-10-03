""" 
created by @mrconfused
syntax :- `.song {song name}`
`.vsong {song name}`
     
"""
import glob
import os

from uniborg.util import admin_cmd
from userbot import catmusic, catmusicvideo

DEFAULTUSER = "𠘨 工 长 工 丅 卂"


@borg.on(admin_cmd(pattern="song( (.*)|$)", allow_sudo=True))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    repl = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif repl:
        if repl.message:
            query = repl.message
    else:
        await event.reply("`What I am Supposed to find `")
        return
    await event.delete()
    a = await event.reply("`wi8..! I am finding your song....`")
    await catmusic(str(query), "320k", event)
    l = glob.glob("./temp/*.mp3")
    if l:
        await a.edit("`yeah..! i found something wi8..🥰`")
    else:
        await a.edit(f"Sorry..! i can't find anything with `{query}`")
        return
    thumbcat = glob.glob("./temp/*.jpg") + glob.glob("./temp/*.webp")
    if thumbcat:
        catthumb = thumbcat[0]
    else:
        catthumb = None
    loa = l[0]
    await event.client.send_file(
        event.chat_id,
        loa,
        force_document=False,
        allow_cache=False,
        caption=f"➥ __**Song :- {query}**__\n__**➥ Uploaded by :-**__ {DEFAULTUSER}",
        thumb=catthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await a.delete()
    os.system("rm -rf ./temp/*.mp3")
    os.system("rm -rf ./temp/*.jpg")
    os.system("rm -rf ./temp/*.webp")


@borg.on(admin_cmd(pattern="vsong( (.*)|$)", allow_sudo=True))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply:
        if reply.message:
            query = reply.messag
    else:
        event = await edit_or_reply(event, "What I am Supposed to find")
        return
    event = await edit_or_reply(event, "`wi8..! I am finding your videosong....`")
    await catmusicvideo(query, event)
    l = glob.glob(("./temp/*.mp4"))
    if l:
        await event.edit("yeah..! i found something wi8..🥰")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`")
        return
    thumbcat = glob.glob("./temp/*.jpg") + glob.glob("./temp/*.webp")
    if thumbcat:
        catthumb = thumbcat[0]
    else:
        catthumb = None
    loa = l[0]
    await borg.send_file(
        event.chat_id,
        loa,
        thumb=catthumb,
        caption=query,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await event.delete()
    os.system("rm -rf ./temp/*.mp4")
    os.system("rm -rf ./temp/*.jpg")
    os.system("rm -rf ./temp/*.webp")
