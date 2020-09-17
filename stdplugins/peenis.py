# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#


from uniborg.util import admin_cmd

PENIS_TEMPLATE = """
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆       🍆🍆
"""


@borg.on(admin_cmd(pattern=r"(?:penis|dick)\s?(.)?"))
async def emoji_penis(e):
    emoji = e.pattern_match.group(1)

    await e.edit("`Dickifying...`")
    message = PENIS_TEMPLATE
    if emoji:
        message = message.replace("🍆", emoji)

    await e.edit(message)
