"""COMMAND : .fu, .sux, .kess"""

import asyncio

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "fu":
        await event.edit(input_str)
        animation_chars = ["👉       ✊️", "👉     ✊️", "👉  ✊️", "👉✊️💦"]

        animation_interval = 0.1
        animation_ttl = range(101)
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "sux":
        await event.edit(input_str)
        animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵👼👰"]

        animation_interval = 0.2
        animation_ttl = range(101)
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "kess":
        await event.edit(input_str)
        animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵💋👰"]

        animation_interval = 0.2
        animation_ttl = range(101)
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])
