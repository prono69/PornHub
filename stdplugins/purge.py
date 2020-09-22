"""Purge your messages without the admins seeing it in Recent Actions"""

import asyncio
import logging
from asyncio import sleep

from telethon import events

from uniborg.util import admin_cmd

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

level = logging.INFO
print(level)
_YEETPURGES = {0: dict(), 1: dict()}  # Dont even try to kang this


@borg.on(admin_cmd(pattern="purge ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`I Need a Mesasge to Start Purging From. U Dumb..`")
        return
    else:
        i = 1
        msgs = []
        from_user = None
        input_str = event.pattern_match.group(1)
        if input_str:
            from_user = await borg.get_entity(input_str)
            logger.info(from_user)
        async for message in borg.iter_messages(
            event.chat_id, min_id=event.reply_to_msg_id, from_user=from_user
        ):
            i += 1
            msgs.append(message)
            if len(msgs) == 100:
                await borg.delete_messages(event.chat_id, msgs, revoke=True)
                msgs = []
            if len(msgs) <= 100:
                await borg.delete_messages(event.chat_id, msgs, revoke=True)
            msgs = []
            await event.delete()
        else:
            await event.edit("**PURGE** Failed!")


@borg.on(admin_cmd(pattern="purgme ?(.*)"))
async def purgeme(delme):
    """ For .purgeme, delete x count of your latest message."""
    message = delme.text
    count = int(message[8:])
    i = 1

    async for message in delme.client.iter_messages(delme.chat_id, from_user="me"):
        if i > count + 1:
            break
        i += 1
        await message.delete()

    smsg = await delme.client.send_message(
        delme.chat_id,
        "`Purge complete!` Purged " + str(count) + " messages.",
    )
    await asyncio.sleep(3)
    await smsg.delete()


@borg.on(admin_cmd(pattern="isd ?(.*)"))
async def selfdestruct(destroy):
    """ For .sd command, make seflf-destructable messages. """
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await smsg.delete()
    if Config.BOTLOG:
        await destroy.client.send_message(
            Config.PRIVATE_GROUP_BOT_API_ID, "`Sd query done successfully`"
        )


@borg.on(admin_cmd(pattern="ipurg ?(.*)"))
async def fastpurger(purg):
    """ For .purge command, purge all messages starting from the reply. """
    chat = await purg.get_input_chat()
    msgs = []
    count = purg.pattern_match.group(1)
    itermsg = purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id)
    count = 0

    if purg.reply_to_msg_id is not None:
        async for msg in itermsg:
            msgs.append(msg)
            count += 1
            msgs.append(purg.reply_to_msg_id)
            if len(msgs) == 100:
                await purg.client.delete_messages(chat, msgs)
                msgs = []
    else:
        await purg.edit("`I Need a Mesasge to Start Purging From.`")
        return

    if msgs:
        await purg.client.delete_messages(chat, msgs)
        done = await purg.client.send_message(
            purg.chat_id,
            f"`Fast purge complete!`\
        \nPurged {str(count)} messages",
        )

    await sleep(1)
    await done.delete()


@borg.on(events.NewMessage(pattern=r"\.(s(?:elf)?)?y(?:eet)?p(?:urge)?", outgoing=True))
async def yeetpurge(e):
    global _YEETPURGES
    selfonly = 1 if e.pattern_match.group(1) else 0
    if not e.is_reply:
        await e.edit("err \\\nNo reply")
        return
    if e.from_id not in _YEETPURGES[selfonly]:
        _YEETPURGES[selfonly][e.from_id] = {}
    cond = e.chat_id not in _YEETPURGES[selfonly][e.from_id]
    if cond:
        _YEETPURGES[selfonly][e.from_id][e.chat_id] = e
        await e.edit("`Yeetpurge from destination set! Reply to end destination`")
        return
    ype = _YEETPURGES[selfonly][e.from_id].pop(e.chat_id)
    minmax = sorted([ype.reply_to_msg_id, e.reply_to_msg_id])
    messages = [e.message, ype.message]
    kw = {"min_id": minmax[0] - 1, "max_id": minmax[1] + 1}
    if selfonly:
        kw["from_user"] = "me"
    async for m in e.client.iter_messages(e.chat_id, **kw):
        messages.append(m)
    await e.client.delete_messages(e.chat_id, messages)
    # Maa ki chut kang mat karna
