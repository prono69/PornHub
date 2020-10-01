from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from os import remove
from platform import python_version

from telethon import events, version
from telethon.tl.types import MessageEntityMentionName

from uniborg.util import admin_cmd, edit_or_reply

"""Type:
\n`.permalink`
`.userid`
`.pip`
`.on`
`.pm`
"""
plugs = len(borg._plugins)


@borg.on(admin_cmd(pattern="permalink ?(.*)"))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await mention.edit(f"[{custom}](tg://user?id={user.id})")
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await mention.edit(f"[{tag}](tg://user?id={user.id})")


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]

        if user.isnumeric():
            user = int(user)

        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None

    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)

    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None

    return user_obj


@borg.on(admin_cmd(pattern="userid"))
async def useridgetter(target):
    """ For .userid command, returns the ID of the target user. """
    message = await target.get_reply_message()
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
        await target.edit("**Name:** {} \n**User ID:** `{}`".format(name, user_id))


@borg.on(admin_cmd(pattern="pip(?: |$)(.*)"))
async def pipcheck(pip):
    """ For .pip command, do a pip search. """
    pipmodule = pip.pattern_match.group(1)
    if pipmodule:
        await pip.edit("`Searching . . .`")
        invokepip = f"pip3 search {pipmodule}"
        pipc = await asyncrunapp(
            invokepip,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )

        stdout, stderr = await pipc.communicate()
        pipout = str(stdout.decode().strip()) + str(stderr.decode().strip())

        if pipout:
            if len(pipout) > 4096:
                await pip.edit("`Output too large, sending as file`")
                file = open("output.txt", "w+")
                file.write(pipout)
                file.close()
                await pip.client.send_file(
                    pip.chat_id,
                    "output.txt",
                    reply_to=pip.id,
                )
                remove("output.txt")
                return
            await pip.edit(
                "**Query: **\n`" f"{invokepip}" "`\n**Result: **\n`" f"{pipout}" "`"
            )
        else:
            await pip.edit(
                "**Query: **\n`"
                f"{invokepip}"
                "`\n**Result: **\n`No Result Returned/False`"
            )
    else:
        await pip.edit("`Use .help pip to see an example`")


@borg.on(admin_cmd(pattern="on"))
async def amireallyalive(alive):
    """ For .on command, check if the bot is running.  """
    await alive.edit(
        "`"
        "My bot is running \n\n"
        f"Telethon version: {version.__version__} \n"
        f"Python: {python_version()} \n"
        f"User: Kirito \n"
        f"Plugins: {plugs}"
        "`"
    )


@borg.on(admin_cmd(pattern="pm ?(.*)"))
async def _(cat):
    kk = cat.pattern_match.group(1)
    await edit_or_reply(cat, "`Sending Message...`")
    replied = await cat.get_reply_message()
    query = kk
    if replied:
        text = replied.message
        username = query
    elif "|" in query:
        text, username = query.split("|")

    await borg.send_message(f"{username}", f"{text}")
    await cat.delete()


@borg.on(admin_cmd(pattern=r"reveal", allow_sudo=True))
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    c = a.read()
    a.close()
    a = await event.reply("**Reading file...**")
    if len(c) > 4095:
        await a.edit("`The Total words in this file is more than telegram limits.`")
    else:
        await event.client.send_message(event.chat_id, f"```{c}```")
        await a.delete()
    remove(b)


@borg.on(events.NewMessage(pattern=r"\.gstat ", outgoing=True))
async def get_stats(event):
    chat = event.text.split(" ", 1)[1]
    try:
        stats = await borg.get_stats(chat)
    except:
        await event.reply(
            "Failed to get stats for the current chat, Make sure you are admin and chat has more than 500 members."
        )
        return
    min_time = stats.period.min_date.strftime("From %d/%m/%Y, %H:%M:%S")
    max_time = stats.period.max_date.strftime("To %d/%m/%Y, %H:%M:%S")
    member_count = int(stats.members.current) - int(stats.members.previous)
    message_count = int(stats.messages.current) - int(stats.messages.previous)
    msg = f"Group stats:\n{min_time} {max_time}\nMembers count increased by {member_count}\nMessage count increased by {message_count}"
    await event.reply(msg)
