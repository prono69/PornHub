"""Cmds:
`.purl`\n`.sg`\n`.fakemail`\n`.mailid`\n`.ub`\n`.gid`\n`.urban`\n`.voicy`\n`.mashup`\n`.iascii`\n`.recognize`"""
import asyncio

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from uniborg import SYNTAX
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="purl ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("**Reply to any document.**")
        return
    reply_message = await event.get_reply_message()
    chat = "@FiletolinkTGbot"
    reply_message.sender
    await event.reply("**Making public url...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1011636686)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await a.edit("```Please unblock me (@FiletolinkTGbot) u Nigga```")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )


@borg.on(admin_cmd(pattern="sg ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```Reply to text message```")
        return
    chat = "@SangMataInfo_bot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @sangmatainfo_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.edit(f"{response.message.message}")


@borg.on(admin_cmd(pattern=("fakemail ?(.*)")))
async def _(event):
    if event.fwd_from:
        return
    chat = "@fakemailbot"
    await event.edit("```Fakemail Creating, wait```")
    async with borg.conversation(chat) as conv:
        try:
            await event.client.send_message("@fakemailbot", "/generate")
            await asyncio.sleep(5)
            k = await event.client.get_messages(
                entity="@fakemailbot", limit=1, reverse=False
            )
            mail = k[0].text
            # print(k[0].text)
        except YouBlockedUserError:
            await event.reply("```Please unblock @fakemailbot and try again```")
            return
        await event.edit(mail)


@borg.on(admin_cmd(pattern="mailid ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@fakemailbot"
    await event.edit("```Fakemail list getting```")
    async with borg.conversation(chat) as conv:
        try:
            await event.client.send_message("@fakemailbot", "/id")
            await asyncio.sleep(5)
            k = await event.client.get_messages(
                entity="@fakemailbot", limit=1, reverse=False
            )
            mail = k[0].text
            # print(k[0].text)
        except YouBlockedUserError:
            await event.reply("```Please unblock @fakemailbot and try again```")
            return
        await event.edit(mail)


@borg.on(admin_cmd(pattern="ub ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```reply to text message```")
        return
    chat = "@uploadbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=97342984)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @sangmatainfo_bot and try again```")
            return
        if response.text.startswith("Hi!,"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.edit(f"{response.message.message}")


@borg.on(admin_cmd(pattern="gid ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```reply to text message```")
        return
    chat = "@getidsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=186675376)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Nikal Gendu```")
            return
        if response.text.startswith("Hello,"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.edit(f"{response.message.message}")


@borg.on(admin_cmd(pattern="urban ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    bsdk = event.pattern_match.group(1)
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    if not bsdk:
        reply_message = await event.get_reply_message()
    bsdk = reply_message.text
    if not bsdk:
        await event.edit("```Reply to a Text message```")
        return
    chat = "@UrbanDictionaryBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=185693644)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Nikal Gendu```")
            return
        if response.text.startswith("Hello,"):
            await event.edit(
                "```Can you Kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.edit(f"{response.message.message}")


@borg.on(admin_cmd(pattern="voicy ?(.*)"))
async def voicy(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Please reply to a Message`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`Reply to a Media`")
        return
    chat = "@Voicybot"
    reply_message.sender
    await event.edit("`Haha Wait...`")
    async with event.client.conversation(chat) as conv:
        try:
            await event.client.forward_messages(chat, reply_message)
        except YouBlockedUserError:
            await event.reply(
                f"`Mmmh sanırım` {chat} `engellemişsin. Lütfen engeli aç.`"
            )
            return

        response = conv.wait_event(
            events.MessageEdited(incoming=True, from_users=259276793)
        )
        response = await response
        if response.text.startswith("__👋"):
            await event.edit("`Botu başlatıp Türkçe yapmanız gerekmektedir.`")
        elif response.text.startswith("__👮"):
            await event.edit("`Ses bozuk, ne dediğini anlamadım.`")
        else:
            await event.edit(f"`{response.text}`")


@borg.on(admin_cmd(pattern="mash ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not input_str and not event.reply_to_msg_id:
        await event.edit("`Seriously Bruh... 😑`")
        await asyncio.sleep(4)
        await event.delete()
        return
    if not input_str:
        reply_to_id = await event.get_reply_message()
        input_str = reply_to_id.text
    chat = "@vixtbot"
    await event.edit("`Checking...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=285336877)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @vixtbot")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("`Sorry i can't find it`")
        else:
            await event.delete()
            await borg.send_file(
                event.chat_id, response.message, reply_to=event.reply_to_msg_id
            )


@borg.on(admin_cmd(pattern="iascii"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Reply to any user message` **Bruh**")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`Reply to an image` **Bruh**")
        return
    start = datetime.now()
    chat = "@asciiart_bot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("Reply to actual users message.")
        return
    downloaded_file_name = await borg.download_media(
        reply_message, Var.TEMP_DOWNLOAD_DIRECTORY
    )
    end = datetime.now()
    ms = (end - start).seconds
    await event.edit(
        "Downloaded to `{}` in **{}** seconds.".format(downloaded_file_name, ms)
    )
    async with borg.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_file(downloaded_file_name)
            ascii = await conv.get_response()
            await borg.send_file(
                event.chat_id, ascii, caption="💠**Here's the requested ascii image!**💠"
            )
            await event.delete()
        except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @asciiart_bot `and retry!`")
            await event.delete()


@borg.on(admin_cmd(pattern="recognize ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply to any user's media message.")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("reply to media file")
        return
    chat = "@Rekognition_Bot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("Reply to actual users message.")
        return
    cat = await event.edit("`Recognizeing this Media...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("unblock @Rekognition_Bot and try again")
            await cat.delete()
            return
        if response.text.startswith("See next message."):
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            response = await response
            cat = response.message.message
            await event.edit(cat)

        else:
            await event.edit("sorry, I couldnt find it")


SYNTAX.update(
    {
        "mashup": "`.mash` <text> :\
      \n**USAGE:** Send you the related video message of given text . "
    }
)
