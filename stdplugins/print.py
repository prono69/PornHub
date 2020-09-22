from uniborg.util import admin_cmd

deploylink = Config.HEROKU_LINK
repolink = Config.REPO_LINK
packs = Config.PACKS_CONTENT


@borg.on(admin_cmd(pattern="print ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    range(16)
    input_str = event.pattern_match.group(1)
    if input_str == "repo":
        await event.edit(
            "Click [here](" + repolink + ") to goto the custom github repo."
        )
    elif input_str == "deploy":
        await event.edit(
            "Click [here](" + deploylink + ") to goto the heroku deploy page."
        )
    elif input_str == "mf":
        await event.edit(
            """
......................................../´¯/)
......................................,/¯../
...................................../..../
..................................../´.¯/
..................................../´¯/
..................................,/¯../
................................../..../
................................./´¯./
................................/´¯./
..............................,/¯../
............................./..../
............................/´¯/
........................../´¯./
........................,/¯../
......................./..../
....................../´¯/
....................,/¯../
.................../..../
............./´¯/'...'/´¯¯·¸
........../'/.../..../......./¨¯\
........('(...´...´.... ¯~/'...')
.........\.................'...../
..........''...\.......... _.·´
............\..............(
..............\.............\...`
    """
        )
    elif input_str == "yee":
        await event.edit(
            """
ツ
"""
        )
    elif input_str == "happy":
        await event.edit(
            """
(ʘ‿ʘ)
"""
        )
    elif input_str == "happy2":
        await event.edit(
            """
=͟͟͞͞٩(๑☉ᴗ☉)੭ु⁾⁾
"""
        )
    elif input_str == "happy3":
        await event.edit(
            """
ヾ(o✪‿✪o)ｼ
"""
        )
    elif input_str == "crying":
        await event.edit(
            """
༎ຶ‿༎ຶ
"""
        )
    elif input_str == "dicc":
        await event.edit(
            """
╰U╯☜(◉ɷ◉ )
"""
        )
    elif input_str == "fek":
        await event.edit(
            """
╰U╯\n(‿ˠ‿)
"""
        )
    elif input_str == "ded":
        await event.edit(
            """
✖‿✖
"""
        )
    elif input_str == "sad":
        await event.edit(
            """
⊙︿⊙
"""
        )
    elif input_str == "lenny":
        await event.edit(
            """
( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)
"""
        )
    elif input_str == "packs":
        await event.edit(packs)
    else:
        await event.edit("variable not defined.")
