# A Huge Thenks to @PhycoNinja13b and @Meli_odas_Bot for their Hard Work
# 👩‍❤️‍💋‍👨
import jikanpy

from uniborg.util import admin_cmd
from userbot.anime import get_anime_manga, get_poster, getBannerLink, post_to_telegraph


@borg.on(admin_cmd(pattern="sanime ?(.*)", allow_sudo=True))
async def get_anime(message):
    try:
        query = message.pattern_match.group(1)
    except IndexError:
        if message.reply_to_msg_id:
            query = await message.get_reply_message().text
        else:
            await message.reply(
                "You gave nothing to search. (｡ì _ í｡)\n `Usage: .ani <anime name>`"
            )
            return
    except Exception as err:
        await message.edit(f"**Encountered an Unknown Exception**: \n{err}")
        return

    p_rm = await message.reply("`Searching Anime...`")
    f_mal_id = ""
    try:
        jikan = jikanpy.AioJikan()
        search_res = await jikan.search("anime", query)
        f_mal_id = search_res["results"][0]["mal_id"]
    except IndexError:
        await p_rm.edit(f"No Results Found for {query}")
        return
    except Exception as err:
        await p_rm.edit(f"**Encountered an Unknown Exception**: \n{err}")
        return

    results_ = await jikan.anime(f_mal_id)
    await jikan.close()

    # Get All Info of anime
    anime_title = results_["title"]
    id = results_["mal_id"]
    jap_title = results_["title_japanese"]
    eng_title = results_["title_english"]
    type_ = results_["type"]
    results_["source"]
    episodes = results_["episodes"]
    status = results_["status"]
    results_["aired"].get("string")
    results_["duration"]
    rating = results_["rating"]
    score = results_["score"]
    synopsis = results_["synopsis"]
    results_["background"]
    producer_list = results_["producers"]
    studios_list = results_["studios"]
    genres_list = results_["genres"]

    # Info for Buttons
    mal_dir_link = results_["url"]
    trailer_link = results_["trailer_url"]

    main_poster = ""
    telegraph_poster = ""
    # Poster Links Search
    try:
        main_poster = get_poster(anime_title)
    except BaseException:
        pass
    try:
        telegraph_poster = getBannerLink(f_mal_id)
    except BaseException:
        pass
    # if not main_poster:
    main_poster = telegraph_poster
    if not telegraph_poster:
        telegraph_poster = main_poster

    genress_md = ""
    producer_md = ""
    studio_md = ""
    for i in genres_list:
        genress_md += f"{i['name']} "
    for i in producer_list:
        producer_md += f"[{i['name']}]({i['url']}) "
    for i in studios_list:
        studio_md += f"[{i['name']}]({i['url']}) "

    # Build synopsis telegraph post
    html_enc = ""
    html_enc += f"<img src = '{telegraph_poster}' title = {anime_title}/>"
    html_enc += f"<br><b>» Studios:</b> {studio_md}</br>"
    html_enc += f"<br><b>» Producers:</b> {producer_md}</br>"
    html_enc += "<br><b>» Synopsis: </b></br>"
    html_enc += f"<br><em>{synopsis}</em></br>"
    synopsis_link = post_to_telegraph(anime_title, html_enc)

    # Build captions:
    captions = f"""📺 `{anime_title}` - `{eng_title}` - `{jap_title}`

**🆎 Type:** `{type_}`
**🆔 ID:** `{id}`
**🎭 Genre:** `{genress_md}`
**🔢 Episodes:** `{episodes}`
**📡 Status:** `{status}`
**💯 Score:** `{score}/10`
**🔞 Rating:** `{rating}`

[🎬 Trailer]({trailer_link})
[📖 Synopsis]({synopsis_link})
[📚 More Info]({mal_dir_link})

©️ @LazyAF_Pepe"""

    await p_rm.delete()
    await message.client.send_file(message.chat_id, file=main_poster, caption=captions)
    await message.delete()


@borg.on(admin_cmd(pattern="imanga ?(.*)"))
async def manga(message):
    search_query = message.pattern_match.group(1)
    await message.get_reply_message()
    await message.edit("`Searching Manga..`")
    jikan = jikanpy.jikan.Jikan()
    search_result = jikan.search("manga", search_query)
    first_mal_id = search_result["results"][0]["mal_id"]
    caption, image = get_anime_manga(first_mal_id, "anime_manga", message.chat_id)
    await message.client.send_file(
        message.chat_id, file=image, caption=caption, parse_mode="HTML"
    )
    await message.delete()


@borg.on(admin_cmd(pattern="ianime ?(.*)"))
async def anime(message):
    search_query = message.pattern_match.group(1)
    await message.get_reply_message()
    await message.edit("`Searching Anime..`")
    jikan = jikanpy.jikan.Jikan()
    search_result = jikan.search("anime", search_query)
    first_mal_id = search_result["results"][0]["mal_id"]
    caption, image = get_anime_manga(first_mal_id, "anime_anime", message.chat_id)
    try:
        await message.client.send_file(
            message.chat_id, file=image, caption=caption, parse_mode="HTML"
        )
    except BaseException:
        image = getBannerLink(first_mal_id, False)
        await message.client.send_file(
            message.chat_id, file=image, caption=caption, parse_mode="HTML"
        )
    await message.delete()


def replace_text(text):
    return text.replace('"', "").replace("\\r", "").replace("\\n", "").replace("\\", "")
