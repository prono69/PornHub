# Made By @DragSama with help of @TheRealPhoenix
# Uses PokeApi.co
"""pokedex for pokemon info .berry for berry info .move for move info"""

import requests

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="pokedex ?(.*)", allow_sudo=True))
async def pokedex(event):
    string = event.pattern_match.group(1)
    url = "http://pokeapi.co/api/v2/pokemon/{}/".format(string)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        msg = ""
        name = data.get("name")
        (data.get("abilities")[0].get("ability"))
        height = data.get("height")
        pokeid = data.get("id")
        (data.get("held_items"))
        sprites = data.get("sprites")
        sprites_front = sprites.get("front_default")
        weight = data.get("weight")
        types = data.get("types")[0].get("type")
        typesa = types.get("name")
        msg += "\n**Name** = {}".format(name)
        typecount = data.get("types")
        msg += "\n**ID** = {}".format(pokeid)
        msg += "\n**Type** = {}".format(typesa)
        x = len(typecount)
        if x > 1:
            typeg = data.get("types")[1].get("type")
            typesb = typeg.get("name")
            msg += "\n**Type 2** = {}".format(typesb)
        msg += "\n**Height** = {}".format(height)
        msg += "\n**Weight** = {}".format(weight)
        msg += f"[\u200c]({sprites_front})"
        try:
            urlb = "http://pokeapi.co/api/v2/characteristic/{}".format(pokeid)
            responseb = requests.get(urlb)
            datab = responseb.json()
            desc = datab.get("descriptions")[1]
            descsub = desc.get("description")
            msg += "\n**Description** = {}".format(descsub)
        except BaseException:
            pass
        await event.edit(msg, link_preview=True)


@borg.on(admin_cmd(pattern="berry ?(.*)", allow_sudo=True))
async def berry(event):
    berryname = event.pattern_match.group(1)
    base = "https://pokeapi.co/api/v2/berry/{}".format(berryname)
    response = requests.get(base)
    if response.status_code == 200:
        data = response.json()
        ev = ""
        (data.get("firmness").get("name"))
        name = data.get("item").get("name")
        gp = data.get("natural_gift_power")
        gt = data.get("natural_gift_type").get("name")
        size = data.get("size")
        smooth = data.get("smoothness")
        dry = data.get("soil_dryness")
        ev += "\n**Name** = {}".format(name)
        ev += "\n**Natural Gift Power** = {}".format(gp)
        ev += "\n**Natural Gift Type** = {}".format(gt)
        ev += "\n**Size** = {}".format(size)
        ev += "\n**Smoothness** = {}".format(smooth)
        ev += "\n**Soil Dryness** = {}".format(dry)
        await event.edit(ev)
    else:
        await event.edit("Berry Not Found.")


@borg.on(admin_cmd(pattern="move ?(.*)", allow_sudo=True))
async def moves(event):
    move = event.pattern_match.group(1)
    base = "https://pokeapi.co/api/v2/move/{}".format(move)
    response = requests.get(base)
    if response.status_code == 200:
        data = response.json()
        ev = ""
        targ = data.get("target").get("name")
        typem = data.get("type").get("name")
        idw = data.get("id")
        name = data.get("name")
        acc = data.get("accuracy")
        pp = data.get("pp")
        prior = data.get("priority")
        power = data.get("power")
        ev += "\n**Name** = {}".format(name)
        ev += "\n**ID** = {}".format(idw)
        ev += "\n**Accuracy** = {}".format(acc)
        ev += "\n**PP** = {}".format(pp)
        ev += "\n**Priority** = {}".format(prior)
        ev += "\n**Power** = {}".format(power)
        ev += "\n**Type** = {}".format(typem)
        ev += "\n**Target** = {}".format(targ)
        try:
            effect = data.get("effect_entries")[0].get("short_effect")
            ev += "\n**Effect** = {}".format(effect)
        except BaseException:
            pass
        await event.edit(ev)
    else:
        await event.edit("Uh is that even a move")
