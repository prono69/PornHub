"""Available Commands:
.unoob
.menoob
.upro
.mepro
@NeoMatrix90"""

import asyncio

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="(.*)"))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "unoob":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "BiGGeSt",
            "NoOoB",
            "uNtiL",
            "YoU",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ BiGGeSt NoOoB uNtiL YoU aRriVe 😈",
        ]

        animation_interval = 0.5

        animation_ttl = range(9)

        for i in animation_ttl:

            await event.edit(animation_chars[i % 9])
            await asyncio.sleep(animation_interval)


@borg.on(admin_cmd(pattern="(.*)"))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "menoob":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "BiGGeSt",
            "NoOoB",
            "uNtiL",
            "i",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ BiGGeSt NoOoB uNtiL i aRriVe 😈",
        ]

        animation_interval = 0.5

        animation_ttl = range(9)

        for i in animation_ttl:

            await event.edit(animation_chars[i % 9])
            await asyncio.sleep(animation_interval)


@borg.on(admin_cmd(pattern="(.*)"))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "upro":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "PeRu",
            "uNtiL",
            "YoU",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ PeRu uNtiL YoU aRriVe 😈",
        ]

        animation_interval = 0.5

        animation_ttl = range(8)

        for i in animation_ttl:

            await event.edit(animation_chars[i % 8])
            await asyncio.sleep(animation_interval)


@borg.on(admin_cmd(pattern="(.*)"))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "mepro":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "PeRu",
            "uNtiL",
            "i",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ PeRu uNtiL i aRriVe 😈",
        ]

        animation_interval = 0.5

        animation_ttl = range(8)

        for i in animation_ttl:

            await event.edit(animation_chars[i % 8])
            await asyncio.sleep(animation_interval)
