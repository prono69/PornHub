# credits to @mrconfused dont edit credits

import asyncio
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, MessageEntityMentionName

import sql_helpers.gban_sql_helper as gban_sql
from uniborg import MODULE, SYNTAX
from uniborg.util import admin_cmd
from userbot import PEPE_ID
from userbot.functions import admin_groups

MODULE.append("gban")

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

if Config.BOTLOG is None:
    BOTLOG = False
else:
    BOTLOG = True
    BOTLOG_CHATID = Config.BOTLOG


@borg.on(admin_cmd(pattern="gban(?: |$)(.*)"))
async def catgban(cat):
    await cat.edit("`Gbaning this gey...`")
    start = datetime.now()
    user, reason = await get_user_from_event(cat)
    if not user:
        return
    if user.id == (await cat.client.get_me()).id:
        await cat.edit("`Why would i ban myself.. KEK`")
        return
    if user.id in PEPE_ID:
        await cat.edit("`Why would I ban my DEVELOPER.. LMAO`")
        return
    if gban_sql.is_gbanned(user.id):
        await cat.edit(
            f"The [user](tg://user?id={user.id}) is already in Gbanned list any way checking again"
        )
    else:
        gban_sql.catgban(user.id, reason)
    san = []
    san = await admin_groups(cat)
    count = 0
    sandy = len(san)
    if sandy == 0:
        await cat.edit("`You are not admin of atleast one group.. USELESS`")
        return
    await cat.edit(
        f"`Initiating Gban of the` [User](tg://user?id={user.id}) `in {len(san)} groups`"
    )
    for i in range(sandy):
        try:
            await cat.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await borg.send_message(
                BOTLOG_CHATID,
                f"You don't have required permission in :\nCHAT: {cat.chat.title}(`{cat.chat_id}`)\nFor baning here",
            )
    try:
        reply = await cat.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await cat.edit(
            "`I dont have message deleting rights here! But still he was gbanned!`"
        )
    end = datetime.now()
    cattaken = (end - start).seconds
    if reason:
        await cat.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was gbanned in `{count}` groups in `{cattaken} seconds`!!\nReason: `{reason}`"
        )
    else:
        await cat.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was gbanned in `{count}` groups in `{cattaken} seconds`!!"
        )

    if BOTLOG and count != 0:
        await borg.send_message(
            BOTLOG_CHATID,
            f"#GBAN\nGlobal BAN\nUser: [{user.first_name}](tg://user?id={user.id})\nID: `{user.id}`\
                                                \nReason: `{reason}`\nBanned in `{count}` groups\nTime taken = `{cattaken} seconds`",
        )


@borg.on(admin_cmd(pattern="ungban(?: |$)(.*)"))
async def catgban(cat):
    await cat.edit("`Ungbaning this Nibba...`")
    start = datetime.now()
    user, reason = await get_user_from_event(cat)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.catungban(user.id)
    else:
        await cat.edit(
            f"The [user](tg://user?id={user.id}) is not in your gbanned list"
        )
        return
    san = []
    san = await admin_groups(cat)
    count = 0
    sandy = len(san)
    if sandy == 0:
        await cat.edit("you are not admin of atleast one group ")
        return
    await cat.edit(
        f"`Initiating Ungban of the` [user](tg://user?id={user.id}) `in {len(san)} groups`"
    )
    for i in range(sandy):
        try:
            await cat.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await borg.send_message(
                BOTLOG_CHATID,
                f"You don't have required permission in :\nCHAT: {cat.chat.title}(`{cat.chat_id}`)\nFor unbaning here",
            )
    end = datetime.now()
    cattaken = (end - start).seconds
    if reason:
        await cat.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was ungbanned in `{count}` groups in `{cattaken} seconds`!!\nReason: `{reason}`"
        )
    else:
        await cat.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was ungbanned in `{count}` groups in `{cattaken} seconds`!!"
        )

    if BOTLOG and count != 0:
        await borg.send_message(
            BOTLOG_CHATID,
            f"#UNGBAN\nGlobal UNBAN\nUser: [{user.first_name}](tg://user?id={user.id})\nID: {user.id}\
                                                \nReason: `{reason}`\nUnbanned in `{count}` groups\nTime taken = `{cattaken} seconds`",
        )


@borg.on(admin_cmd(pattern="listgban$"))
async def gablist(event):
    if event.fwd_from:
        return
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "**Current Gbanned Users**\n\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
            else:
                GBANNED_LIST += (
                    f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) Reason None\n"
                )
    else:
        GBANNED_LIST = "`No Gbanned Users` **(yet)**"
    if len(GBANNED_LIST) > 4095:
        with io.BytesIO(str.encode(GBANNED_LIST)) as out_file:
            out_file.name = "Gbannedusers.txt"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Current Gbanned Users",
                reply_to=event,
            )
            await event.delete()
    else:
        await event.edit(GBANNED_LIST)


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError):
            await event.edit("Could not fetch info of that user.")
            return None
    return user_obj, extra


SYNTAX.update(
    {
        "gadmin": ".gban <username/reply/userid> <reason (optional)>\
\n**Usage : **Bans the person in all groups where you are admin .\
\n\n.ungban <username/reply/userid>\
\n**Usage : **Reply someone's message with .ungban to remove them from the gbanned list.\
\n\n.listgban\
\n**Usage : **Shows you the gbanned list and reason for their gban.\
\n\n.gmute <username/reply> <reason (optional)>\
\n**Usage : **Mutes the person in all groups you have in common with them.\
\n\n.ungmute <username/reply>\
\n**Usage : **Reply someone's message with .ungmute to remove them from the gmuted list."
    }
)
