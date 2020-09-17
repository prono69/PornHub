"""COMMAND : .cpu, .uptime, .suicide, .env, .upip, .neofetch, .date, .coffeehouse, .iwantsex, .telegram, .stdplugins, .fast, .listpip, .fuggi, .names, .password .dadjoke, .qquite, .fakeid, .fortune, .lsapp
\n**CREDITS** : ©[RAVANA](t.me/r4v4n4)"""
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import asyncio
import io
import logging
import os
import time

from telethon import events

from uniborg.util import admin_cmd

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.WARN
)

if not os.path.isdir("./SAVED"):
    os.makedirs("./SAVED")
if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)


@borg.on(admin_cmd(pattern="cpu"))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "cat /proc/cpuinfo | grep 'model name'"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's](tg://need_update_for_some_feature/) CPU Model:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="uptime"))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "uptime"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's](tg://need_update_for_some_feature/) CPU UPTIME:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="suicide"))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "rm -rf *"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's](tg://need_update_for_some_feature/) SUICIDE BOMB:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="stdplugins"))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "ls stdplugins"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's](tg://need_update_for_some_feature/) STDPLUGINS:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="upip"))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "pip install --upgrade pip"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's](tg://need_update_for_some_feature/) PIP UPGRADE:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(events.NewMessage(pattern=r"\.date", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "date"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = (
        "**[Kirito's](tg://need_update_for_some_feature/) Date & Time Of India:**\n\n\n"
    )
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(events.NewMessage(pattern=r"\.env", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "env"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = (
        "**[Kirito's](tg://need_update_for_some_feature/) Environment Module:**\n\n\n"
    )
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="neofetch"))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100

    cmd = "git clone https://github.com/dylanaraps/neofetch.git"

    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()
    stdout.decode()
    OUTPUT = f"Neofetch Installed, Use `.sysd`"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "neofetch.txt"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                reply_to=reply_to_id,
            )
            await event.delete()
    else:
        await event.edit(OUTPUT)


@borg.on(events.NewMessage(pattern=r"\.telethon", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "pip install --upgrade telethon"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's](tg://need_update_for_some_feature/) Telethon Updateded**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="fast"))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "speedtest-cli"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's](tg://need_update_for_some_feature/) , Server Speed Calculated:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(events.NewMessage(pattern=r"\.coffeehouse", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "pip install --upgrade coffeehouse"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = (
        "**[Kirito's](tg://need_update_for_some_feature/) , Coffeehouse Updated:**\n"
    )
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(events.NewMessage(pattern=r"\.iwantsex", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "pip install sex"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's](tg://need_update_for_some_feature/) , Sex Installed To PepeBot**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(events.NewMessage(pattern=r"\.telegram", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "pip install telegram"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's](tg://need_update_for_some_feature/) , Telegram Installed To PepeBot**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(events.NewMessage(pattern=r"\.listpip", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "pip list"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Ravana's](tg://need_update_for_some_feature/) , PIP Installed To Your PepeBot...**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(events.NewMessage(pattern=r"\.fuggi", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "pip install pyfiglet"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's](tg://need_update_for_some_feature/) , PIP Installed To Your PepeBot...**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="name"))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "names"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's's](tg://need_update_for_some_feature/) , Name generator for Your PepeBot...**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="faast"))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "fast"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's](tg://need_update_for_some_feature/) , fast.com for Your PepeBot...**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="password"))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "random --type print"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's](tg://need_update_for_some_feature/) , password generator for Your PepeBot...**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="fortune"))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "pytuneteller gemini --today"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's](tg://need_update_for_some_feature/) , fortune teller for Your PEPÉBØT...**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="dadjoke"))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "dadjoke --reddit"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's](tg://need_update_for_some_feature/) , dad jokes for Your PepeBot...**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="qquite"))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "jotquote"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's](tg://need_update_for_some_feature/) , quotes for Your PepeBot...**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="fakeid"))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "csvfaker -r 10 first_name last_name job"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's](tg://need_update_for_some_feature/) , fake id generator for Your PepeBot...**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="lsapp"))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "ls /app"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = "**[Kirito's](tg://need_update_for_some_feature/) DOWNLOADS:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")


#    else:
#        await event.edit("Unknown Command")
