"""Emoji



Available Commands:

.wupload



by @kirito6969

"""


import asyncio

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "wupload":

        await event.edit(input_str)

        animation_chars = [
            "Uploading File From Telegram To Whatsapp...",
            " User Online: True\nTelegram API Access: True\nWhatsapp API Access: True\nRead Storage: True ",
            "DOWNLOADING STARTED... \n\n0% [░░░░░░░░░░░░░░░░░░░░]\n`Connecting To WhatsApp API...`\nETA: 0m, 20s",
            "DOWNLOADING... \n\n11.07% [██░░░░░░░░░░░░░░░░░░]\n\nETA: 0m, 18s",
            "DOWNLOADING... \n\n20.63% [███░░░░░░░░░░░░░░░░░]\n\nETA: 0m, 16s",
            "FILE DOWNLOADED, UPLOADING TO ADMIN'S WHATSAPP GROUP [CHUTIYA GENG BOYS]... \n\n34.42% [█████░░░░░░░░░░░░░░░]\n\nETA: 0m, 14s",
            "UPLOADING... \n\n42.17% [███████░░░░░░░░░░░░░]\n\nETA: 0m, 12s",
            "UPLOADING... \n\n55.30% [█████████░░░░░░░░░░░]\n\nETA: 0m, 10s",
            "UPLOADING... \n\n64.86% [███████████░░░░░░░░░]\n\nETA: 0m, 08s",
            "UPLOADED TO ADMIN'S WHATSAPP GROUP SERVER ... \n\n74.02% [█████████████░░░░░░░]\n\nETA: 0m, 06s",
            "SPLITTING FILE IN WHATSAPP SUPPORTED SIZE & UPLOADING IT ... 86.21% [███████████████░░░░░]\n\nETA: 0m, 04s",
            "SPLITTING FILE IN WHATSAPP SUPPORTED SIZE & UPLOADING IT... 93.50% [█████████████████░░░]\n\nETA: 0m, 02s",
            "UPLOADING TO ADMIN'S WHATSAPP GROUP [CHUTIYA GANG BOYS]... 100% [████████████████████]\n`Scanning file...`\nETA: 0m, 00s",
            "UPLOADING FILE TO WHATSAPP GROUP COMPLETED!\nFILE VERIFIED: ✅",
            "API TERMINATED UNTIL FURTHER USAGE...",
        ]

        animation_interval = 9

        animation_ttl = range(15)

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 15])
