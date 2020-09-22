# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

import asyncio
from asyncio import sleep

from uniborg import SYNTAX
from uniborg.util import admin_cmd

BOTLOG = Config.BOTLOG


@borg.on(admin_cmd(pattern="tspam (.*)"))
async def tmeme(e):
    cspam = str(e.pattern_match.group(1))
    message = cspam.replace(" ", "")
    await e.delete()
    for letter in message:
        await e.respond(letter)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG, "#CSPAM\n" "TSpam was executed successfully"
        )


@borg.on(admin_cmd(pattern="wspam (.*)"))
async def tmeme(e):
    wspam = str(e.pattern_match.group(1))
    message = wspam.split()
    await e.delete()
    for word in message:
        await e.respond(word)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG, "#WSPAM\n" "WSpam was executed successfully"
        )


@borg.on(admin_cmd(pattern="ispam (.*)"))
async def spammer(e):
    counter = int(e.pattern_match.group(1).split(" ", 1)[0])
    spam_message = str(e.pattern_match.group(1).split(" ", 1)[1])
    await e.delete()
    await asyncio.wait([e.respond(spam_message) for i in range(counter)])
    if BOTLOG:
        await e.client.send_message(BOTLOG, "#SPAM\n" "Spam was executed successfully")


@borg.on(admin_cmd(pattern="picspam"))
async def tiny_pic_spam(e):
    message = e.text
    text = message.split()
    counter = int(text[1])
    link = str(text[2])
    await e.delete()
    for _ in range(1, counter):
        await e.client.send_file(e.chat_id, link)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG, "#PICSPAM\n" "PicSpam was executed successfully"
        )


@borg.on(admin_cmd(pattern="delayspam (.*)"))
async def spammer(e):
    spamDelay = float(e.pattern_match.group(1).split(" ", 2)[0])
    counter = int(e.pattern_match.group(1).split(" ", 2)[1])
    spam_message = str(e.pattern_match.group(1).split(" ", 2)[2])
    await e.delete()
    for _ in range(1, counter):
        await e.respond(spam_message)
        await sleep(spamDelay)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG, "#DelaySPAM\n" "DelaySpam was executed successfully"
        )


SYNTAX.update(
    {
        "Spam/Fun": "**Your spam is your death wish.**"
        """
.tspam <text>\
\nUsage: Spam the text letter by letter.\
\n\n.ispam <count> <text>\
\nUsage: Floods text in the chat !!\
\n\n.wspam <text>\
\nUsage: Spam the text word by word.\
\n\n.picspam <count> <link to image/gif>\
\nUsage: As if text spam was not enough !!\
\n\n.delayspam <delay> <count> <text>\
\nUsage: .bigspam but with custom delay.\
\n\n\nNOTE : Spam at your own risk !!
    """
    }
)
