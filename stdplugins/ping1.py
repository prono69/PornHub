from datetime import datetime

from uniborg.util import admin_cmd, edit_or_reply


@borg.on(admin_cmd(pattern="ping", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    e = await edit_or_reply(event, "Poooong!")
    start = datetime.now()
    await e.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await e.edit("**Pong!**\n`{}` `ms`".format(ms))
