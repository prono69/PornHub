"""AnimeList Plugin For PEPEBOT
\nPlugin Made By - © [NIKITA](https://t.me/kirito6969)
\nThanks [MeliOdas](https://t.me/Meli_odas_Bot) for fixing some Bugs
\nDo `.help animelist` if you are using **My Repo**
\n\n**DON'T EDIT CREDITS**
\n\n#LazyAF_Geng rocks.. 🔥
"""
import asyncio
import datetime
import html
import textwrap

import bs4
import requests
from jikanpy import Jikan
from jikanpy.exceptions import APIException

from uniborg import MODULE, SYNTAX
from uniborg.util import admin_cmd

MODULE.append("animelist")

jikan = Jikan()


@borg.on(admin_cmd(pattern="anime ?(.*)"))
async def anime(event):
    query = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    await event.edit("`Searching Anime...`")
    if query:
        pass
    elif reply:
        query = reply.text
    else:
        await event.edit("`Brah.. What I am supposed to search ?`")
        await asyncio.sleep(6)
        await event.delete()
        return
    # res = ""
    try:
        res = jikan.search("anime", query)
    except Exception as err:
        await event.edit(f"**Error:** \n`{err}`")
        return
    try:
        res = res.get("results")[0].get("mal_id")  # Grab first result
    except APIException:
        await event.edit("Error connecting to the API. Please try again!")
        return
    if res:
        anime = jikan.anime(res)
        title = anime.get("title")
        japanese = anime.get("title_japanese")
        anime.get("title_english")
        type = anime.get("type")
        duration = anime.get("duration")
        synopsis = anime.get("synopsis")
        source = anime.get("source")
        status = anime.get("status")
        episodes = anime.get("episodes")
        score = anime.get("score")
        rating = anime.get("rating")
        genre_lst = anime.get("genres")
        genres = ""
        for genre in genre_lst:
            genres += genre.get("name") + ", "
        genres = genres[:-2]
        studios = ""
        studio_lst = anime.get("studios")
        for studio in studio_lst:
            studios += studio.get("name") + ", "
        studios = studios[:-2]
        duration = anime.get("duration")
        premiered = anime.get("premiered")
        image_url = anime.get("image_url")
        trailer = anime.get("trailer_url")
        if trailer:
            bru = f"<a href='{trailer}'>Trailer</a>"
        url = anime.get("url")
    else:
        await event.edit("`No results Found!`")
        return
    rep = f"<b>{title}</b> - ({japanese})\n"
    rep += f"<b>Type:</b> <code>{type}</code>\n"
    rep += f"<b>Source:</b> <code>{source}</code>\n"
    rep += f"<b>Status:</b> <code>{status}</code>\n"
    rep += f"<b>Genres:</b> <code>{genres}</code>\n"
    rep += f"<b>Episodes:</b> <code>{episodes}</code>\n"
    rep += f"<b>Duration:</b> <code>{duration}</code>\n"
    rep += f"<b>Score:</b> <code>{score}</code>\n"
    rep += f"<b>Studio(s):</b> <code>{studios}</code>\n"
    rep += f"<b>Premiered:</b> <code>{premiered}</code>\n"
    rep += f"<b>Rating:</b> <code>{rating}</code>\n\n"
    ##rep += f"<b>Trailer:</b> {bru}\n\n"
    rep += f"<a href='{image_url}'>\u200c</a>"
    rep += f"📖 <b>Synopsis</b>: <i>{synopsis}</i>\n"
    rep += f'<b>Read More:</b> <a href="{url}">MyAnimeList</a>'
    await event.edit(rep, parse_mode="HTML", link_preview=True)


@borg.on(admin_cmd(pattern="manga ?(.*)"))
async def manga(event):
    query = event.pattern_match.group(1)
    await event.edit("`Searching Manga...`")
    if not query:
        await event.edit("`Bruh.. Gib me Something to Search`")
        return
    res = ""
    manga = ""
    try:
        res = jikan.search("manga", query).get("results")[0].get("mal_id")
    except APIException:
        await event.edit("Error connecting to the API. Please try again!")
        return ""
    if res:
        try:
            manga = jikan.manga(res)
        except APIException:
            await event.edit("Error connecting to the API. Please try again!")
            return ""
        title = manga.get("title")
        japanese = manga.get("title_japanese")
        type = manga.get("type")
        status = manga.get("status")
        score = manga.get("score")
        volumes = manga.get("volumes")
        chapters = manga.get("chapters")
        genre_lst = manga.get("genres")
        genres = ""
        for genre in genre_lst:
            genres += genre.get("name") + ", "
        genres = genres[:-2]
        synopsis = manga.get("synopsis")
        image = manga.get("image_url")
        url = manga.get("url")
        rep = f"<b>{title} ({japanese})</b>\n"
        rep += f"<b>Type:</b> <code>{type}</code>\n"
        rep += f"<b>Status:</b> <code>{status}</code>\n"
        rep += f"<b>Genres:</b> <code>{genres}</code>\n"
        rep += f"<b>Score:</b> <code>{score}</code>\n"
        rep += f"<b>Volumes:</b> <code>{volumes}</code>\n"
        rep += f"<b>Chapters:</b> <code>{chapters}</code>\n\n"
        rep += f"<a href='{image}'>\u200c</a>"
        rep += f"📖 <b>Synopsis</b>: <i>{synopsis}</i>\n"
        rep += f'<b>Read More:</b> <a href="{url}">MyAnimeList</a>'
        await event.edit(rep, parse_mode="HTML", link_preview=True)


@borg.on(admin_cmd(pattern="user ?(.*)"))
async def user(event):
    search_query = event.pattern_match.group(1)
    message = await event.get_reply_message()
    if search_query:
        pass
    elif message:
        search_query = message.text
    else:
        await event.edit("`Format : .user <username>`")
        return

    try:
        user = jikan.user(search_query)
    except APIException:
        await event.edit("`Username not Found Nibba`")
        return

    date_format = "%Y-%m-%d"
    if user["image_url"] is None:
        img = "https://telegra.ph//file/9b4205e1b1cc68a4ffd5e.jpg"
    else:
        img = user["image_url"]

    try:
        user_birthday = datetime.datetime.fromisoformat(user["birthday"])
        user_birthday_formatted = user_birthday.strftime(date_format)
    except BaseException:
        user_birthday_formatted = "Unknown"

    user_joined_date = datetime.datetime.fromisoformat(user["joined"])
    user_joined_date_formatted = user_joined_date.strftime(date_format)
    user_last_online = datetime.datetime.fromisoformat(user["last_online"])
    user_last_online_formatted = user_last_online.strftime(date_format)

    for entity in user:
        if user[entity] is None:
            user[entity] = "Unknown"

    about = user["about"].split(" ", 60)

    try:
        about.pop(60)
    except IndexError:
        pass

    about_string = " ".join(about)
    about_string = about_string.replace("<br>", "").strip().replace("\r\n", "\n")

    caption = ""

    caption += textwrap.dedent(
        f"""
    **Username**: [{user['username']}]({user['url']})

    **Gender**: `{user['gender']}`
    **MAL ID**: `{user['user_id']}`
    **Birthday**: `{user_birthday_formatted}`
    **Joined**: `{user_joined_date_formatted}`
    **Last Online**: `{user_last_online_formatted}`
    **Days wasted watching Anime**: `{user['anime_stats']['days_watched']}`
    **Days wasted reading Manga**: `{user['manga_stats']['days_read']}`

    """
    )

    caption += f"**About**: {about_string}"
    await event.client.send_file(event.chat_id, file=img, caption=caption)


@borg.on(admin_cmd(pattern="sh (kaizoku|kayo) ?(.*)"))
async def site_search(event):
    message = await event.get_reply_message()
    search_query = event.pattern_match.group(2)
    site = event.pattern_match.group(1)
    if search_query:
        pass
    elif message:
        search_query = message.text
    else:
        await event.edit("`Uuf Bro.. Gib something to Search`")
        return

    if site == "kaizoku":
        search_url = f"https://animekaizoku.com/?s={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {"class": "post-title"})

        if search_result:
            result = f"<a href='{search_url}'>Click Here For More Results</a> <b>of</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>AnimeKaizoku</code>: \n\n"
            for entry in search_result:
                post_link = entry.a["href"]
                post_name = html.escape(entry.text.strip())
                result += f"• <a href='{post_link}'>{post_name}</a>\n"
                await event.edit(result, parse_mode="HTML")
        else:
            result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>AnimeKaizoku</code>"
            await event.edit(result, parse_mode="HTML")

    elif site == "kayo":
        search_url = f"https://animekayo.com/?s={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {"class": "title"})

        result = f"<a href='{search_url}'>Click Here For More Results</a> <b>of</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>AnimeKayo</code>: \n\n"
        for entry in search_result:

            if entry.text.strip() == "Nothing Found":
                result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>AnimeKayo</code>"
                break

            post_link = entry.a["href"]
            post_name = html.escape(entry.text.strip())
            result += f"• <a href='{post_link}'>{post_name}</a>\n"
            await event.edit(result, parse_mode="HTML")


@borg.on(admin_cmd(pattern="char ?(.*)"))
async def character(event):
    message = await event.get_reply_message()
    search_query = event.pattern_match.group(1)
    if search_query:
        pass
    elif message:
        search_query = message.text
    else:
        await event.edit("Format: `.character <character name>`")
        return

    try:
        search_result = jikan.search("character", search_query)
    except APIException:
        await event.edit("`Character not found.`")
        return
    first_mal_id = search_result["results"][0]["mal_id"]
    character = jikan.character(first_mal_id)
    caption = f"[{character['name']}]({character['url']})"
    if character["name_kanji"] != "Japanese":
        caption += f" (`{character['name_kanji']}`)\n"
    else:
        caption += "\n"

    if character["nicknames"]:
        nicknames_string = ", ".join(character["nicknames"])
        caption += f"\n**Nicknames** : `{nicknames_string}`"
    about = character["about"].split(" ", 60)
    try:
        about.pop(60)
    except IndexError:
        pass
    about_string = " ".join(about)
    mal_url = search_result["results"][0]["url"]
    for entity in character:
        if character[entity] is None:
            character[entity] = "Unknown"
    caption += f"\n🔰**Extracted Character Data**🔰\n\n__{about_string}...__"
    caption += f"\n[READ MORE]({mal_url})"
    await event.client.send_file(
        event.chat_id,
        file=character["image_url"],
        caption=replace_text(caption),
        reply_to=event,
    )


@borg.on(admin_cmd(pattern="upcoming ?(.*)"))
async def upcoming(message):
    rep = "<b>Upcoming anime</b>\n"
    later = jikan.season_later()
    anime = later.get("anime")
    for new in anime:
        name = new.get("title")
        url = new.get("url")
        rep += f"• <a href='{url}'>{name}</a>\n"
        if len(rep) > 1000:
            break
        await message.edit(rep, parse_mode="html")


def replace_text(text):
    return text.replace('"', "").replace("\\r", "").replace("\\n", "").replace("\\", "")


SYNTAX.update(
    {
        "animelist": "Usage: Anime Information\
\n\n`.anime <anime>` Returns with Anime information.\
\n\n`.character <name>` Returns with Character information.\
\n\n`.manga <manga name>` Returns with the Manga information.\
\n\n`.user <MAL username>` Returns with MAL information.\
\n\n`.sh <kaizoku or kayo> <anime name>` Returns with the Anime Downlaod link.\
\n\n`.upcoming` Returns with Upcoming Anime information."
    }
)
