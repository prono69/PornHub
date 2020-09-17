"""Get the info your system. Using .neofetch then .sysd"""
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="sysd", outgoing=True))
async def sysdetails(sysd):
    """ a. """
    if not sysd.text[0].isalpha() and sysd.text[0] not in ("/", "#", "@", "!"):
        try:
            neo = "neofetch --off --color_blocks off --bold off --cpu_temp C \
                    --cpu_speed on --cpu_cores physical --kernel_shorthand off --stdout"
            fetch = await asyncrunapp(
                neo,
                stdout=asyncPIPE,
                stderr=asyncPIPE,
            )

            stdout, stderr = await fetch.communicate()
            result = str(stdout.decode().strip()) + str(stderr.decode().strip())

            await sysd.edit("Neofetch Result: `" + result + "`")
        except FileNotFoundError:
            await sysd.edit(
                "`On PepeBot Neofetch not installed. Install it by .neofetch, kthxbye!`"
            )
