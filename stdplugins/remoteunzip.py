import re

from remotezip import RemoteZip
from telethon import events

from sample_config import Config

filedir = f"{Config.TMP_DOWNLOAD_DIRECTORY}extracted/"


@borg.on(events.NewMessage(pattern=("runzip")))
async def _(event):
    """ remote link to unzip archive """
    await event.edit("`Processing...`")
    textx = await event.get_reply_message()
    message = event.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await event.edit("`Usage: .runzip <url>`")
        return
    reply = ""
    links = re.findall(r"\.zip", textx)
    if not links:
        reply = "`No .zip extension link found!`"
        await event.edit(reply)
    else:
        with RemoteZip(links) as zip:
            zip.extractall(filedir)
            x = zip.extractall(filedir)
            await borg.send_file(
                event.chat_id,
                x,
                caption="unzipped @By_Azade",
                # progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                #     progress(d, t, event, c_time, "trying to upload")
                # )
            )

    await event.edit(reply)
