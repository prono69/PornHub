import random

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="modi ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`Mitro, Main Hoon Modi. Jo is desh ki Gand Mar raha hain.`")


# ===================================================================

MODISTR = [
    "`Mitron, Mandir Wahi Banadiya`",
    "`Mitron, Ye Hindu Rastra Hain`",
    "`Mitron, Main Hoon Modi, Maine apni Gand marali`",
    "`Mitron, Farmer suicide kar rahe hain, Acchey Din Aagaya`",
    "`Mitron, Jo bhi kuch sawal puchega woh Anti-nationalist, Deshdrohi`",
    "`Mitron, Mujhe time do, main tumhe Kala Dhan dunga`",
    "`Mitron, Main Hoon MODI, maine kal Ranu ke sath sex kiya, ekdam chod dala jaise main is desh ko chod raha hu`",
]

# =======================================================================================================


@borg.on(admin_cmd(pattern="imodi", outgoing=True))
async def imodi(lul):
    """ Fuck Modi """
    if not lul.text[0].isalpha() and lul.text[0] not in ("/", "#", "@", "!"):
        await lul.edit(random.choice(MODISTR))
