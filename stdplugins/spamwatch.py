"""spamwatch for uniborg users. Credits : @By_Azade"""

import spamwatch
from telethon import events
from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from sample_config import Config

ENABLE_LOG = True
LOGGING_CHATID = Config.PRIVATE_CHANNEL_BOT_API_ID
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


@borg.on(events.ChatAction(func=lambda e: e.is_group))
async def spam_watch_(event):
    chat = await event.get_chat()
    if Config.SPAM_WATCHAPI:
        client = spamwatch.Client(Config.SPAM_WATCH_API)
        user = await event.get_user()
        try:
            if (chat.admin_rights or chat.creator) and (
                event.user_joined or event.user_added
            ):
                try:
                    ban = client.get_ban(event.action_message.from_id)
                    if ban:
                        await borg(
                            EditBannedRequest(
                                event.chat_id,
                                event.action_message.from_id,
                                BANNED_RIGHTS,
                            )
                        )
                    else:
                        return
                except AttributeError:
                    return
                except BadRequestError:
                    return
                except ValueError:
                    return
                if ENABLE_LOG:
                    await event.client.send_message(
                        LOGGING_CHATID,
                        "#SPAMWATCH_BAN\n"
                        f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                        f"CHAT: {event.chat.title}(`{event.chat_id}`)",
                    )
            else:
                return ""
        except AttributeError:
            return
