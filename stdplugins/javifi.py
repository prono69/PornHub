from telethon.errors.rpcerrorlist import YouBlockedUserError

from uniborg import MODULE, SYNTAX
from uniborg.util import admin_cmd

naam = "NIKITA"
nom = " You"

bot = "@indianaibot"
bluebot = "@EASY12DEVIL_BOT"
freebot = "@freeusersbot"

MODULE.append("javifi")


@borg.on(admin_cmd(pattern="jav ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)

    if sysarg == "h":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/hello")
                audio = await conv.get_response()
                await borg.send_file(
                    event.chat_id,
                    audio,
                    caption="➡️**TO BOSS : **"
                    + naam
                    + "\n`Check out` [PEPEBOT](https://github.com/prono69/PepeBot)",
                )
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @indianaibot `and retry!")
    elif sysarg == "ss":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/ss")
                audio = await conv.get_response()
                await borg.send_file(
                    event.chat_id,
                    audio,
                    caption="**CREDITS : Dr.jr Genesis**\n`Check out` [PEPEBOT](https://github.com/prono69/PepeBot)",
                )
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @Mariodevs `and retry!`")
    elif sysarg == "--h":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/help")
                audio = await conv.get_response()
                await borg.send_file(
                    event.chat_id,
                    audio,
                    caption="**Dr.Bot Is Here To Help**\n`Check out` [PEPEBOT](https://github.com/prono69/PepeBot)",
                )
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @Mariodevs `and retry!`")
    elif sysarg == "npic":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/nudepic")
                audio = await conv.get_response()
                await borg.send_file(
                    event.chat_id,
                    audio,
                    caption="**For"
                    + nom
                    + " **\n`Check out` [PEPEBOT](https://github.com/prono69/PepeBot)",
                )
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @indianaibot `and retry!`")
    elif sysarg == "rs":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/rs")
                audio = await conv.get_response()
                await borg.send_file(
                    event.chat_id,
                    audio,
                    caption="**CREDITS : Dr.Pure Indian Lover**\n`Check out` [PEPEBOT](https://github.com/prono69/PepeBot)",
                )
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @Mariodevs `and retry!`")
    elif sysarg == "ib":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/ib")
                audio = await conv.get_response()
                await borg.send_file(
                    event.chat_id,
                    audio,
                    caption="**CREDITS : Dr.BlueDevil**\n`Check out` [PEPEBOT](https://github.com/prono69/PepeBot)",
                )
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @mariodevs `and retry!`")
    elif sysarg == "acc":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/acc")
                audio = await conv.get_response()
                await borg.send_file(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @mariodevs `and retry!`")
    elif sysarg == "ccn":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/lcc")
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @indianaibot `and retry!`")
    else:
        await brog.send_message(
            event.chat_id, "**INVALID** -- FOR HELP COMMAND IS **.jav --h**"
        )
        await event.delete()
        await event.client.send_read_acknowledge(event.chat_id)


SYNTAX.update(
    {
        "javifi": "Usage: Various Bot Commands\
\n\n`.jav h` For Hello\
\n\n`.jav --h` For Help\
\n\n`.jav npic` For a Random Nude Pic\
\n\n`.jav ss` \
\n\n`.jav rs` \
\n\n`.jav ib` \
\n\n`.jav acc` \
\n\n`.jav ccn`"
    }
)
