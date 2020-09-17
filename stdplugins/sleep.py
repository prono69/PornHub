import asyncio

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="sleep( [0-9]+)?$", outgoing=True))
async def sleepybot(time):
    """ For .sleep command, let the userbot snooze for a few second. """
    time.text
    if " " not in time.pattern_match.group(1):
        await time.reply("Syntax: `.sleep [seconds]`")
    else:
        counter = int(time.pattern_match.group(1))
        await time.edit("`I am sulking and snoozing....`")
        await asyncio.sleep(2)
        if Config.PRIVATE_GROUP_BOT_API_ID is not None:
            await time.client.send_message(
                Config.PRIVATE_GROUP_BOT_API_ID,
                "You put the bot to sleep for " + str(counter) + " seconds",
            )
        await asyncio.sleep(counter)
        await time.edit("`OK, I'm awake now.`")
