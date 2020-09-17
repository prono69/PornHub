"""Ported by @NeoMatrix90 (***LEGEND***) cmd is .fp"""
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="fp$ ?(.*)", allow_sudo=True))  # pylint:disable=E0602
async def facepalm(e):
    """ Facepalm  🤦‍♂ """
    await e.edit("🤦‍♂")
