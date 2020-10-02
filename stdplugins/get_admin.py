"""Get Administrators of any Chat*
Syntax: .g_admin, .ids, .g_bot"""
from telethon.tl.types import (
    ChannelParticipantAdmin,
    ChannelParticipantCreator,
    ChannelParticipantsAdmins,
    ChannelParticipantsBots,
)
from telethon.utils import pack_bot_file_id

from uniborg.util import admin_cmd, edit_or_reply


@borg.on(admin_cmd(pattern="g_ad?(m)in ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Admins in this Group**: \n"
    should_mention_admins = False
    reply_message = None
    pattern_match_str = event.pattern_match.group(1)
    if "m" in pattern_match_str:
        should_mention_admins = True
        if event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
    input_str = event.pattern_match.group(2)
    to_write_chat = await event.get_input_chat()
    chat = None
    if input_str:
        mentions_heading = "**Admins in {} :** \n".format(input_str)
        mentions = mentions_heading
        try:
            chat = await borg.get_entity(input_str)
        except Exception as e:
            await event.edit(str(e))
            return None
    else:
        chat = to_write_chat
    try:
        async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
            if not x.deleted and isinstance(x.participant, ChannelParticipantCreator):
                mentions += "\n 👑 [{}](tg://user?id={}) `{}`".format(
                    x.first_name, x.id, x.id
                )
        mentions += "\n"
        async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
            if x.deleted:
                mentions += "\n ☠️ `{}`".format(x.id)
            else:
                if isinstance(x.participant, ChannelParticipantAdmin):
                    mentions += "\n ⚜️ [{}](tg://user?id={}) `{}`".format(
                        x.first_name, x.id, x.id
                    )
    except Exception as e:
        mentions += " " + str(e) + "\n"
    if should_mention_admins:
        if reply_message:
            await reply_message.reply(mentions)
        else:
            await edit_or_reply(event, mentions)
        await event.delete()
    else:
        await edit_or_reply(event, mentions)


@borg.on(admin_cmd(pattern="g_bot ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Bots in this Channel**: \n"
    input_str = event.pattern_match.group(1)
    to_write_chat = await event.get_input_chat()
    chat = None
    if not input_str:
        chat = to_write_chat
    else:
        mentions = "**Bots in {}:** \n\n".format(input_str)
        try:
            chat = await borg.get_entity(input_str)
        except Exception as e:
            await event.edit(str(e))
            return None
    try:
        async for x in borg.iter_participants(chat, filter=ChannelParticipantsBots):
            if isinstance(x.participant, ChannelParticipantAdmin):
                mentions += "\n ⚜️ [{}](tg://user?id={}) `{}`".format(
                    x.first_name, x.id, x.id
                )
            else:
                mentions += "\n [{}](tg://user?id={}) `{}`".format(
                    x.first_name, x.id, x.id
                )
    except Exception as e:
        mentions += " " + str(e) + "\n"
    await event.edit(mentions)


@borg.on(admin_cmd(pattern="ids"))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await event.edit(
                "👥 **Chat ID**: `{}`\n💬 **Message Id**: `{}`\n🙋‍♂️ **From User ID**: `{}`\n📄 **File ID**: `{}`".format(
                    str(event.chat_id),
                    str(r_msg.id),
                    str(r_msg.from_id),
                    bot_api_file_id,
                )
            )
        else:
            await event.edit(
                "👥 **Chat ID**: `{}`\n💬 **Message Id**: `{}`\n🙋‍♂️ **From User ID**: `{}`".format(
                    str(event.chat_id), str(r_msg.id), str(r_msg.from_id)
                )
            )
    else:
        await event.edit("👥 **Chat ID**: `{}`".format(str(event.chat_id)))
