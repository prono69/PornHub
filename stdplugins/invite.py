"""Invite the user(s) to the current chat
Syntax: `.invite <User(s)>`"""

from telethon import functions

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="invite ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    ed = await event.edit("`Hold On! Inviting...`")
    if event.is_private:
        await event.edit("`Are u sure u gonna do that in DMs ?`")
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
            # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.messages.AddChatUserRequest(
                            chat_id=event.chat_id, user_id=user_id, fwd_limit=1000000
                        )
                    )
                    await ed.edit("`Invited Successfully`")
                except Exception as e:
                    await ed.edit(str(e))
        else:
            # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.channels.InviteToChannelRequest(
                            channel=event.chat_id, users=[user_id]
                        )
                    )
                    await ed.edit("`Invited Successfully`")
                except Exception as e:
                    await ed.edit(str(e))
