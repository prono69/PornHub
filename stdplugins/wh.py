"""Get Telegram User Information
Syntax: .ww @username/userid"""
import html
import os

from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location

from uniborg.util import admin_cmd

TMP_DOWNLOAD_DIRECTORY = "./"


@borg.on(admin_cmd(pattern="ww ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    if not os.path.isdir(TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)

    replied_user = await get_user(event)

    caption = await fetch_info(replied_user, event)

    message_id_to_reply = event.message.reply_to_msg_id

    if not message_id_to_reply:
        message_id_to_reply = None

    await event.reply(caption, parse_mode="HTML")


async def get_user(event):
    """Get the user from argument or replied message."""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
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
            await event.edit(str(err))
            return None

    return replied_user


async def fetch_info(replied_user, event):
    """Get details from the User object."""
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(
            user_id=replied_user.user.id, offset=42, max_id=0, limit=80
        )
    )
    replied_user_profile_photos_count = "None"
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
        dc_id = "Need a Profile Picture to check DC ID!"
        str(e)
    common_chat = replied_user.common_chats_count
    username = replied_user.user.username
    user_bio = replied_user.about
    replied_user.user.bot
    replied_user.user.restricted
    replied_user.user.verified
    photo = await event.client.download_profile_photo(
        user_id, TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg", download_big=True
    )
    first_name = html.escape(replied_user.user.first_name)
    first_name = first_name.replace("\u2060", "")
    last_name = last_name.replace("\u2060", "") if last_name else ("None")
    last_name = html.escape(last_name)
    username = "@{}".format(username) if username else ("None")
    user_bio = "None" if not user_bio else user_bio
    if user_id != (await event.client.get_me()).id:
        common_chat = replied_user.common_chats_count
    else:
        common_chat = "They're in all the same places I am... oh. It's me."

    caption = "<b>General Info OF:</b> \n"
    caption += f'<a href="tg://user?id={user_id}">{first_name}</a> \n'
    caption += f"<b>First Name</b>: <code>{first_name}</code> \n"
    caption += f"<b>Last Name</b>: {last_name} \n"
    caption += f"<b>Username</b>: {username} \n"
    caption += f"<b>ID</b>: <code>{user_id}</code> \n"
    caption += f"<b>DC ID</b>: <code>{dc_id}</code>\n"
    caption += (
        f"<b>Number of PPs</b>: <code>{replied_user_profile_photos_count}</code>\n"
    )
    caption += f"Common Groups: <code>{common_chat}</code> \n \n"
    caption += f"<b>Bio</b>: \n<code>{user_bio}</code> \n"

    return caption
