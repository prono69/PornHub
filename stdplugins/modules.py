# For UniBorg
# By Priyam Kalra
# modified by @authoritydmc
# Syntax (.modules)
from uniborg import MODULE
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="modules ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    modules = "**List of available modules:**\n"
    MODULE.sort()
    prev = "1"
    for module in MODULE:
        if prev[0] != module[0]:
            modules += f"\n\n\t{module[0].upper()}\n\n"
        modules += f"ℹ️ ```{module}```\n"
        prev = module
    modules += "\n\n**Tip --> Use .help <module_name> for more info.**"
    await event.edit(modules)
