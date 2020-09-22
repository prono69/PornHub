"""Reply to any message (.shoot) to kill that fuking user.Created by @NeoMatrix90 .Don't fucking edit this, Otherwise u r geyyy."""

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="shoot$ ?(.*)", allow_sudo=True))  # pylint:disable=E0602
async def killing(killed):
    """ Dont Kill Too much -_-"""
    if (
        not killed.text[0].isalpha()
        and killed.text[0] not in ("/", "#", "@", "!")
        and await killed.get_reply_message()
    ):
        await killed.edit(
            "`Targeted user killed by Headshot 😈.. Bhag Bsdk`\n" "#Sad_Reacts_Onli\n"
        )
