"""Get Telegram User Information
Syntax: .whois @username/userid"""

import asyncio
import html
import os

from telethon.errors.rpcerrorlist import MessageTooLongError
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import Channel, MessageEntityMentionName, User
from telethon.utils import get_display_name, get_input_location

from uniborg import SYNTAX
from uniborg.util import admin_cmd

TEMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@borg.on(admin_cmd(pattern="whois ?(.*)"))
async def who(event):

    await event.edit("`Collecting info from My Private Database...`")

    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)

    replied_user = await get_user(event)

    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        return event.edit("`Could not fetch info of that user.`")

    message_id_to_reply = event.message.reply_to_msg_id

    if not message_id_to_reply:
        message_id_to_reply = None

    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )

        if not photo.startswith("http"):
            os.remove(photo)
        await event.delete()

    except TypeError:
        await event.edit(caption, parse_mode="html")


async def get_user(event):
    """ Get the user from argument or replied message. """
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            return await event.edit(str(err))

    return replied_user


async def fetch_info(replied_user, event):
    """ Get details from the User object. """
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(
            user_id=replied_user.user.id, offset=42, max_id=0, limit=80
        )
    )
    replied_user_profile_photos_count = "This gay has no Pics :("
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError:
        pass
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception as e:
        dc_id = "Need a Pic for DC ID!"
        str(e)
    if user_id != (await event.client.get_me()).id:
        common_chat = replied_user.common_chats_count
    else:
        common_chat = "It's me U gey boi"
    username = replied_user.user.username
    user_bio = replied_user.about
    is_bot = replied_user.user.bot
    restricted = replied_user.user.restricted
    verified = replied_user.user.verified
    photo = await event.client.download_profile_photo(
        user_id, TEMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg", download_big=True
    )
    first_name = first_name.replace("\u2060", "") if first_name else ("None")
    last_name = last_name.replace("\u2060", "") if last_name else ("None")
    username = "@{}".format(username) if username else ("This User has no Username")
    user_bio = "This User has no About" if not user_bio else user_bio

    caption = "<b>USER INFO:</b>\n\n"
    caption += f"<b>🗣 First Name:</b> <code>{first_name}</code>\n"
    caption += f"<b>🗣 Last Name:</b> <code>{last_name}</code>\n"
    caption += f"<b>👤 Username:</b> {username}\n"
    caption += f"<b>🏢 DC ID:</b> <code>{dc_id}</code>\n"
    caption += f"<b>🤖 Is Bot:</b> <code>{is_bot}</code>\n"
    caption += f"<b>🚫 Is Restricted:</b> <code>{restricted}</code>\n"
    caption += f"<b>✅ Is Verified by Telegram:</b> <code>{verified}</code>\n"
    caption += f"<b>🕵️‍♂️ User ID:</b> <code>{user_id}</code>\n"
    caption += (
        f"<b>🖼 Profile Photos:</b> <code>{replied_user_profile_photos_count}</code>\n"
    )
    caption += f"<b>👥 Common Chats:</b> <code>{common_chat}</code>\n"
    caption += f"<b>📝 Bio:</b> <code>{user_bio}</code>\n\n"
    caption += f"<b>🔗 Permanent Link To Profile:</b> "
    caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'

    return photo, caption


@borg.on(admin_cmd(pattern="members"))
async def _(event):
    members = []
    async for member in borg.iter_participants(event.chat_id):
        if not member.deleted and not member.bot:
            messages = await borg.get_messages(event.chat_id, from_user=member, limit=0)
            members.append(
                (messages.total, f"{messages.total} - {get_who_string(member)}\n")
            )
    members = (m[1] for m in sorted(members, key=lambda m: m[0], reverse=True))
    members = "".join(members)
    try:
        await event.reply(members, parse_mode="html")
    except MessageTooLongError:
        # print("too message")
        for m in split_message(members):
            # print(m)
            await asyncio.sleep(2)
            await event.reply(f"{m}", parse_mode="html")
    del members


def split_message(text, length=4096, offset=200):
    return [
        text[
            text.find("\n", i - offset, i + 1)
            if text.find("\n", i - offset, i + 1) != -1
            else i : text.find("\n", i + length - offset, i + length)
            if text.find("\n", i + length - offset, i + length) != -1
            else i + length
        ]
        for i in range(0, len(text), length)
    ]


def get_who_string(who):
    who_string = html.escape(get_display_name(who))
    if isinstance(who, (User, Channel)) and who.username:
        who_string += f" <i>(@{who.username})</i>"
    who_string += f", <a href='tg://user?id={who.id}'>#{who.id}</a>"
    return who_string


SYNTAX.update(
    {
        "whois": ">`.whois <username> or reply to someone's message with .whois`"
        "\nUsage: Gets info of an user."
        ">`.members`"
        "\nUsage: Show list of members in a group"
    }
)
