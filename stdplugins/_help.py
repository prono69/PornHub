"""**Know Your UniBorg**
◇ list of all loaded plugins
◆ `.info`\n
◇ to know Data Center
◆ `.dc`\n
◇ powered by
◆ `.config`\n
◇ to know syntax
◆ `.nigga` <plugin name>
"""
import shutil
import sys
import time

from telethon import __version__, functions

from uniborg.util import admin_cmd, humanbytes, time_formatter


@borg.on(admin_cmd(pattern="info ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    splugin_name = event.pattern_match.group(1)
    if splugin_name in borg._plugins:
        s_help_string = borg._plugins[splugin_name].__doc__
    else:
        s_help_string = ""
        _, check_sgnirts = check_data_base_heal_th()

    current_run_time = time_formatter((time.time() - BOT_START_TIME))
    total, used, free = shutil.disk_usage("/")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)

    help_string = "@UniBorg\n"
    help_string += f"✅ <b>UpTime</b> <code>{current_run_time}</code>\n"
    help_string += f"✅ <b>Python</b> <code>{sys.version}</code>\n"
    help_string += f"✅ <b>Telethon</b> <code>{__version__}</code>\n"
    help_string += f"{check_sgnirts} <b>Database</b>\n"
    help_string += f"<b>Total Disk Space</b>: <code>{total}</code>\n"
    help_string += f"<b>Used Disk Space</b>: <code>{used}</code>\n"
    help_string += f"<b>Free Disk Space</b>: <code>{free}</code>\n\n"
    help_string += f"<b>Custom Repo</b>: https://github.com/udf/uniborg"
    borg._iiqsixfourstore[str(event.chat_id)] = {}
    borg._iiqsixfourstore[str(event.chat_id)][str(event.id)] = (
        help_string + "\n\n" + s_help_string
    )
    tgbotusername = Config.TG_BOT_USER_NAME_BF_HER
    if tgbotusername is not None:
        results = await borg.inline_query(
            tgbotusername, f"@UniBorg {event.chat_id} {event.id}"
        )
        await results[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )
    else:
        await event.reply(help_string + "\n\n" + s_help_string, parse_mode="html")

    await event.delete()


@borg.on(admin_cmd(pattern="dc"))
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetNearestDcRequest())  # pylint:disable=E0602
    await event.edit(
        f"**Country** : `{result.country}`\n"
        f"**Nearest DC** : `{result.nearest_dc}`\n"
        f"**This DC** : `{result.this_dc}`"
    )


@borg.on(admin_cmd(pattern="config"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetConfigRequest())
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await event.edit("""Telethon UserBot powered by @UniBorg""")


@borg.on(admin_cmd(pattern="nigga (.*)"))
async def _(event):
    if event.fwd_from:
        return
    plugin_name = event.pattern_match.group(1)
    if plugin_name in borg._plugins:
        help_string = borg._plugins[plugin_name].__doc__
        unload_string = (
            f"Use `.unload {plugin_name}` to remove this plugin.\n           © @UniBorg"
        )
        if help_string:
            plugin_syntax = f"Syntax for plugin **{plugin_name}**:\n\n{help_string}\n{unload_string}"
        else:
            plugin_syntax = f"No DOCSTRING has been setup for {plugin_name} plugin."
    else:
        plugin_syntax = "Enter valid **Plugin** name.\nDo `.exec ls stdplugins` to get list of valid plugin names."
    await event.edit(plugin_syntax)


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "❌"

    if not Config.DB_URI:
        return is_database_working, output

    from sql_helpers import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "✅"
        is_database_working = True

    return is_database_working, output
