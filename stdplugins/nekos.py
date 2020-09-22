# #LazyAF_Geng 🔥

"""NEKOS MODULE FOR PEPEBOT
\nPlugin Made by [NIKITA](https://t.me/kirito6969)
Cmds = `.nk <argument from POSSIBLE list>`
\nPOSSIBLE = [
        'feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo',
        'solog', 'feetg', 'cum', 'erokemo', 'les', 'wallpaper', 'lewdk',
        'ngif', 'tickle', 'lewd', 'feed', 'gecg', 'eroyuri', 'eron',
        'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'nsfw_avatar',
        'gasm', 'poke', 'anal', 'slap', 'hentai', 'avatar', 'erofeet', 'holo',
        'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'lizard', 'pussy_jpg',
        'pwankg', 'classic', 'kuni', 'waifu', 'pat', '8ball', 'kiss', 'femdom',
        'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs', 'random_hentai_gif',
        'smallboobs', 'hug', 'ero', 'smug', 'goose', 'baka', 'woof'
    ]
\n`.dva`\n`.nsfw`\n`.cat`\n`.lewdn`\n`.why`\n`.gasm`\n`.ifu`\n`.fact`\n`.tcat`
\n\nNSFW PLUGIN. BE AWARE 🔴
\n\n**DON'T EVEN TRY TO TO CHANGE CREDITS**'
"""

import os

import nekos
import requests
from PIL import Image

from uniborg import MODULE
from uniborg.util import admin_cmd

MODULE.append("nekos")


@borg.on(admin_cmd(pattern="nk ?(.*)"))
async def _(event):
    hmm = event.pattern_match.group(1)
    if not hmm:
        await event.edit("`Bruh.. What I am supposed to do!`")
        return
    await event.edit("`Processing...Nekos`")
    await event.delete()
    target = nekos.img(f"{hmm}")
    await event.client.send_file(event.chat_id, file=target, caption=f"{hmm}")


@borg.on(admin_cmd(pattern="dva"))
async def dva(event):
    nsfw = requests.get("https://api.computerfreaker.cf/v1/dva").json()
    url = nsfw.get("url")
    if not url:
        await event.edit("`uuuf.. No URL found from the API`")
        return
    await event.client.send_file(event.chat_id, file=url)


@borg.on(admin_cmd(pattern="nsfw"))
async def avatarlewd(event):
    with open("temp.png", "wb") as f:
        target = "nsfw_avatar"
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    await event.client.send_file(event.chat_id, file=open("temp.webp", "rb"))
    os.remove("temp.webp")


@borg.on(admin_cmd(pattern="cat"))
async def _(event):
    target = nekos.cat()
    await event.edit("Finding ur ket...🌚")
    await event.delete()
    await event.client.send_file(event.chat_id, file=target)


@borg.on(admin_cmd(pattern="lewdn"))
async def dva(event):
    nsfw = requests.get("https://nekos.life/api/lewd/neko").json()
    url = nsfw.get("neko")
    if not url:
        await event.edit("`uuuf.. No NEKO found from the API`")
        return
    await event.client.send_file(event.chat_id, file=url)


@borg.on(admin_cmd(pattern="why"))
async def _(event):
    target = nekos.why()
    await event.edit(target)


@borg.on(admin_cmd(pattern="gasm"))
async def gasm(event):
    with open("temp.png", "wb") as f:
        target = "gasm"
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    await event.client.send_file(event.chat_id, file=open("temp.webp", "rb"))
    os.remove("temp.webp")


@borg.on(admin_cmd(pattern="ifu"))
async def waifu(event):
    with open("temp.png", "wb") as f:
        target = "waifu"
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    await event.client.send_file(event.chat_id, file=open("temp.webp", "rb"))
    os.remove("temp.webp")


@borg.on(admin_cmd(pattern="fact"))
async def _(event):
    target = nekos.fact()
    await event.edit(f"`{target}`")


@borg.on(admin_cmd(pattern="tcat"))
async def _(event):
    target = nekos.textcat()
    await event.edit(target)
