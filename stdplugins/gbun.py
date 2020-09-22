# This is a troll indeed ffs *facepalm*
import asyncio

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="gbun ?(.*)"))
async def gbun(event):
    if event.fwd_from:
        return
    ### kek = "986755683" , "790841356"
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = "`Warning!! User Gbanned By Admin...\n`"
    await event.edit("**Calling some LOLIS 🌚☠️**")
    await asyncio.sleep(3)
    chat = await event.get_input_chat()
    async for _ in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 986755683:
            await reply_message.reply(
                "`Wait a Second, This is My Master!`\n**How dare you threaten to Gban My Master Nigger!**\n\n__Your account has been hacked! Pay 69$ to my master__ [Kirito](tg://user?id=986755683) __to Release your Account__😏"
            )
        else:
            jnl = (
                "`Warning!! `"
                "[{}](tg://user?id={})"
                "` RIPPED By Admin...\n\n`"
                "**Rendi's Name: ** __{}__\n"
                "**ID : ** `{}`\n"
            ).format(firstname, idd, firstname, idd)
            if usname is None:
                jnl += "**Victim Nigga's username: ** `Doesn't own a username!`\n"
            elif usname != "None":
                jnl += "**Victim Nigga's username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Reason: **" + gbunm
                jnl += gbunr
            else:
                no_reason = "__Reason: Potential Porn Addict. __"
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = (
            "`Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\nReason: Potential Porn Addict. `"
        )
        await event.reply(mention)
    await event.delete()
