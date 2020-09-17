# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""
    .chat [options]
    \n`.id: Return only the id.`
    \n`.general: Show general information related to the chat.`
    \n`.admins: Show chat admins (does not mention them).`
    \n`.all: Show everything.`
     """


from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import Channel, ChatInviteExported, User
from telethon.tl.types.messages import ChatFull

from uniborg.util import admin_cmd, parse_arguments
from userbot.tgdoc import *
from userbot.utils import get_chat_from_event, inline_mention, list_admins, list_bots


@borg.on(admin_cmd(pattern=r"c(?:hat)?(\s+[\S\s]+|$)"))
async def chat_info(e):
    params = e.pattern_match.group(1) or ""
    args, chat = parse_arguments(params, ["id", "general", "admins", "bots", "all"])
    args["chat"] = chat

    if isinstance(e.chat, User):
        from .userinfo import fetch_info as fetch_user_info

        replied_user = await e.client(GetFullUserRequest(e.chat.id))
        response = await fetch_user_info(replied_user, **args)
    else:
        full_chat: ChatFull = await get_chat_from_event(e, **args)

        await e.edit("`Fetching chat info...`")
        response = await fetch_info(e, full_chat, **args)

    await e.edit(str(response))


async def fetch_info(event, full_chat, **kwargs):
    chat = full_chat.chats[0]
    show_all = kwargs.get("all", False)
    id_only = kwargs.get("id", False)
    show_general = kwargs.get("general", True)
    show_admins = kwargs.get("admins", False)
    show_bots = kwargs.get("bots", False)

    is_private = False
    if isinstance(chat, Channel) and chat.username:
        chat.title if chat.title else chat.username
        title = Bold("〽 Chat Informations:")
    elif chat.title:
        is_private = True
        title = Bold("〽️ Chat Informations:")
    else:
        is_private = True
        title = Bold(f"Chat {chat.id}")

    if show_all:
        show_general = True
        show_admins = True
        show_bots = True
    elif id_only:
        return KeyValueItem(title, Code(str(chat.id)))

    admin_list = await list_admins(event)

    if show_general:
        exported_invite = full_chat.full_chat.exported_invite
        invite_link = (
            exported_invite.link
            if isinstance(exported_invite, ChatInviteExported)
            else None
        )
        admin_count = full_chat.full_chat.admins_count or len(admin_list)

        general = SubSection(
            KeyValueItem("   \t**Chat Id**", Code(str(f"-100{chat.id}"))),
            KeyValueItem("**Title**", f"[{chat.title}](t.me/{chat.username})"),
            KeyValueItem("**Private**", Code(str(is_private))),
            KeyValueItem(
                "**Invite Link**", Link(invite_link.split("/")[-1], invite_link)
            )
            if invite_link
            else None,
            KeyValueItem("**Admins**", Code(str(admin_count))),
            KeyValueItem("**Online**", Code(str(full_chat.full_chat.online_count))),
            KeyValueItem(
                "**Total**", Code(str(full_chat.full_chat.participants_count))
            ),
        )
    else:
        general = None

    if show_admins:
        admins = SubSection(Bold("🧍Admins🧍"))
        for admin in admin_list:
            admins.items.append(String(inline_mention(admin)))
        if not admins:
            admins.items.append(String("No Admins"))

    if show_bots:
        bots_list = await list_bots(event)
        bots = SubSection(Bold("🤖Bots🤖"))
        for bot in bots_list:
            bots.items.append(String(inline_mention(bot)))
        if not bots:
            bots.items.append(String("No Bots"))

    return TGDoc(
        Section(
            title,
            general if show_general else None,
            admins if show_admins else None,
            bots if show_bots else None,
        )
    )
