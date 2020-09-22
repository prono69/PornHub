from telethon import events

"""Command: .bigspam <number> DO NOT TRY THIS WITH YOUR ACCOUNT

telethon.errors.rpcerrorlist.FloodWaitError: A wait of 280 seconds is required"""


@borg.on(events.NewMessage(pattern=r"\.bigspam (.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    for _ in range(int(input_str)):
        m = await event.respond("https://github.com/prono69/PepeBot")
        await m.delete()
    """if "|" in input_str:
        counter, spam_text = input_str.split("|")
        shiiinabot = "\u2060"
        for i in range(4000):
            shiiinabot += "\u2060"
        message_text = shiiinabot + spam_text
        await event.edit(message_text)
        for i in range(int(counter)):
            time.sleep(0.3)
            await event.respond(message_text)
        await event.delete()
    else:
        await event.edit("send me a message in the format `.bigspam count | spam message` and admins won't see it in recent actions" +
                         " \n Courtesy: @shiiinabot")"""
