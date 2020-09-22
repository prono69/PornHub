# For UniBorg
# By Priyam Kalra
# Syntax (.spam <number of msgs> <text>)

from time import sleep

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="spam ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input = str(event.pattern_match.group(1))
    input_split = input.split()
    chat = event.chat_id
    try:
        count = str(input_split[0])
    except ValueError:
        await event.edit("Invalid Syntax!\nTip: Use ```.nigga spam``` for help.")
        return
    if input.startswith(count):
        strip = len(count)
        text = input[strip:]
    else:
        await event.edit(
            "Fatal Error!\nPlease contact the developer of this module [@A_FRICKING_GAMER] for support."
        )
        return
    if text and count is not None:
        for _ in range(int(count)):
            await event.reply(text)
        msg = await event.reply(f"Task complete, spammed input text {count} times!")
        sleep(5)
        await msg.delete()
        status = f"SPAMMED\n```{text}```\n in {chat} ```{count}``` times."
        await log(status)
    else:
        await event.edit("Unexpected Error! Aborting..")
        return


async def log(text):
    LOGGER = Config.PRIVATE_GROUP_BOT_API_ID
    await borg.send_message(LOGGER, text)
