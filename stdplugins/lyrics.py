"""
Lyrics Plugin Syntax:
	.lyrics <aritst name - song nane>

"""
import os
import random

import lyricsgenius

from uniborg import SYNTAX
from uniborg.util import admin_cmd

GENIUS = Config.GENIUS


@borg.on(admin_cmd(pattern="lyrics ?(.*)"))
async def lyrics(lyric):
    if r"-" not in lyric.text:
        await lyric.edit(
            "Please use '-' as divider for <artist> and <song>\n"
            "eg: `.lyrics Alan Walker - Lily`"
        )
        return

    if GENIUS is None:
        await lyric.edit(
            "`Provide genius access token to config.py or Heroku Var first kthxbye!`"
        )
    else:
        genius = lyricsgenius.Genius(GENIUS)
        try:
            args = lyric.text.split(".lyrics")[1].split("-")
            artist = args[0].strip(" ")
            song = args[1].strip(" ")
        except Exception:
            await lyric.edit("`LMAO please provide artist and song names`")
            return

    if len(args) < 1:
        await lyric.edit("`Kek.. Please provide artist and song names`")
        return

    await lyric.edit(f"`Searching lyrics for {artist} - {song}...`")

    try:
        songs = genius.search_song(song, artist)
    except TypeError:
        songs = None

    if songs is None:
        await lyric.edit(f"Song **{artist} - {song}** not found!")
        return
    if len(songs.lyrics) > 4096:
        await lyric.edit("`Lyrics is too big, view the file to see it.`")
        with open("lyrics.txt", "w+") as f:
            f.write(f"Search query: \n{artist} - {song}\n\n{songs.lyrics}")
        await lyric.client.send_file(
            lyric.chat_id,
            "lyrics.txt",
            reply_to=lyric.id,
        )
        os.remove("lyrics.txt")
    else:
        await lyric.edit(
            f"**Search query**: \n`{artist} - {song}`\n\n```{songs.lyrics}```"
        )
    return


@borg.on(admin_cmd(pattern="iff(?: |$)(.*)"))
async def pressf(f):
    """Pays respects"""
    args = f.text.split()
    arg = (f.text.split(" ", 1))[1] if len(args) > 1 else None
    if len(args) == 1:
        r = random.randint(0, 3)
        logger.info(r)
        if r == 0:
            await f.edit("┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
        elif r == 1:
            await f.edit("╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯")
        else:
            arg = "F"
    if arg is not None:
        out = ""
        F_LENGTHS = [5, 1, 1, 4, 1, 1, 1]
        for line in F_LENGTHS:
            c = max(round(line / len(arg)), 1)
            out += (arg * c) + "\n"
        await f.edit("`" + out + "`")


SYNTAX.update(
    {
        "lyrics": "**Usage:** `provide artist and song name to find lyrics`\n\n"
        "For multiple-word artist name use * (Exmpl: `.lyrics Валентин-Стрыкало Все решено`)"
    }
)
