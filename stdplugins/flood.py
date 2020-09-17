"""COMMAND : .floodwarn
\nThis is the Most dangours plugin. This can RIPPED ur UserBot.
"""

import asyncio
from collections import deque

from telethon import events


@borg.on(events.NewMessage(pattern=r".floodwarn", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("💙💛💓💔💘💕💜💚💝💞💟"))
    for _ in range(100000000):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)
