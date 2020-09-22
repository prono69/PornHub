"""Emoji
Available Commands:
.admem"""

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "admem":
        await event.edit(input_str)
        animation_chars = [
            "@aaaaaaaaaaaaadddddddddddddmmmmmmmmmmmmmiiiiiiiiiiiiinnnnnnnnnnnnn",
            "@aaaaaaaaaaaaddddddddddddmmmmmmmmmmmmiiiiiiiiiiiinnnnnnnnnnnn",
            "@aaaaaaaaaaadddddddddddmmmmmmmmmmmiiiiiiiiiiinnnnnnnnnnn",
            "@aaaaaaaaaaddddddddddmmmmmmmmmmiiiiiiiiiinnnnnnnnnn",
            "@aaaaaaaaadddddddddmmmmmmmmmiiiiiiiiinnnnnnnnn",
            "@aaaaaaaaddddddddmmmmmmmmiiiiiiiinnnnnnnn",
            "@aaaaaaadddddddmmmmmmmiiiiiiinnnnnnn",
            "@aaaaaaddddddmmmmmmiiiiiinnnnnn",
            "@aaaaadddddmmmmmiiiiinnnnn",
            "@aaaaddddmmmmiiiinnnn",
            "@aaadddmmmiiinnn",
            "@aaddmmiinn",
            "@admin",
        ]

        animation_ttl = range(96)
        for i in animation_ttl:
            await event.edit(animation_chars[i % 96])
