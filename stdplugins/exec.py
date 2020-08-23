"""Execute GNU/Linux commands inside Telegram
Syntax: .exec Code"""
import io
import asyncio
import time
from uniborg.util import admin_cmd
import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.WARN)


@borg.on(admin_cmd(pattern="exec ?(.*)"))
async def _(event):
    if event.fwd_from or event.via_bot_id:
        return
    PROCESS_RUN_TIME = 100
    await event.edit("`Processing...`")
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "No Error"
    o = stdout.decode()
    if not o:
        o = "**Tip**: \n`Nikal Lawde, Pehli Fursat Mei Nikal BSDK.`"
    else:
        _o = o.split("\n")
        o = "`\n".join(_o)
    OUTPUT = f"**QUERY:**\n__Command:__\n`{cmd}` \n__PID:__\n`{process.pid}`\n\n**stderr:** \n`{e}`\n**Output:**\n{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "exec.txt"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id
            )
            await event.delete()
    await event.edit(OUTPUT)
