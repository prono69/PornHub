"""
Torrent Search Plugin for Userbot.
CMD:
`.tt` <query>\n
`.ts` <query or reply>\n
`.movie torrentz2.eu|idop.se` <query>

"""
import asyncio
from datetime import datetime

import cfscrape  # https://github.com/Anorov/cloudflare-scrape
import requests
from bs4 import BeautifulSoup as bs

from uniborg import MODULE
from uniborg.util import admin_cmd, humanbytes

MODULE.append("torrents")


def dogbin(magnets):
    counter = 0
    urls = []
    while counter != len(magnets):
        message = magnets[counter]
        url = "https://del.dog/documents"
        r = requests.post(url, data=message.encode("UTF-8")).json()
        url = f"https://del.dog/{r['key']}"
        urls.append(url)
        counter += 1
    return urls


@borg.on(admin_cmd(pattern="tt ?(.*)", allow_sudo=True))
async def tor_search(event):
    if event.fwd_from:
        return
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }

    search_str = event.pattern_match.group(1)

    print(search_str)
    await event.edit("Searching for " + search_str + ".....")
    if " " in search_str:
        search_str = search_str.replace(" ", "+")
        print(search_str)
        res = requests.get(
            "https://www.torrentdownloads.me/search/?new=1&s_cat=0&search="
            + search_str,
            headers,
        )

    else:
        res = requests.get(
            "https://www.torrentdownloads.me/search/?search=" + search_str, headers
        )

    source = bs(res.text, "lxml")
    urls = []
    magnets = []
    titles = []
    counter = 0
    for div in source.find_all("div", {"class": "grey_bar3 back_none"}):
        # print("https://www.torrentdownloads.me"+a['href'])
        try:
            title = div.p.a["title"]
            title = title[20:]
            titles.append(title)
            urls.append("https://www.torrentdownloads.me" + div.p.a["href"])
        except KeyError:
            pass
        except TypeError:
            pass
        except AttributeError:
            pass
        if counter == 11:
            break
        counter += 1
    if not urls:
        await event.edit("Either the Keyword was restricted or not found..")
        return

    print("Found URLS...")
    for url in urls:
        res = requests.get(url, headers)
        # print("URl: "+url)
        source = bs(res.text, "lxml")
        for div in source.find_all("div", {"class": "grey_bar1 back_none"}):
            try:
                mg = div.p.a["href"]
                magnets.append(mg)
            except Exception:
                pass
    print("Found Magnets...")
    shorted_links = dogbin(magnets)
    print("Dogged Magnets to del.dog...")
    msg = ""
    try:
        search_str = search_str.replace("+", " ")
    except BaseException:
        pass
    msg = "**Torrent Search Query**\n`{}`".format(search_str) + "\n**Results**\n"
    counter = 0
    while counter != len(titles):
        msg = (
            msg
            + "⁍ [{}]".format(titles[counter])
            + "({})".format(shorted_links[counter])
            + "\n\n"
        )
        counter += 1

    await event.edit(msg, link_preview=False)


@borg.on(admin_cmd(pattern="ts ?(.*)"))
async def ts_message_f(message):
    i_m_sefg = await message.edit("`Searching For Torrent...`")
    query = message.pattern_match.group(1)
    replied = await message.get_reply_message()
    if replied:
        query = replied.text
    if not query and not replied:
        await message.edit("`Can't search void`")
        return
    r = requests.get("https://sjprojectsapi.herokuapp.com/torrent/?query=" + query)
    try:
        torrents = r.json()
        reply_ = ""
        for torrent in torrents:
            if len(reply_) < 4096:
                try:
                    reply_ = (
                        reply_ + f"\n\n<b>{torrent['name']}</b>\n"
                        f"<b>Size:</b> {torrent['size']}\n"
                        f"<b>Seeders:</b> {torrent['seeder']}\n"
                        f"<b>Leechers:</b> {torrent['leecher']}\n"
                        f"<code>{torrent['magnet']}</code>"
                    )
                    await asyncio.sleep(3)
                    await i_m_sefg.edit(reply_, parse_mode="html")
                except Exception:
                    pass

        if reply_ == "":
            await i_m_sefg.edit(f"`No torrents found for {query}!`")
            return
    except Exception:
        await i_m_sefg.edit("`Torrent Search API is Down!\nTry again later`")


@borg.on(
    admin_cmd(pattern=r"movie (torrentz2\.eu|idop\.se) (.*)")  # pylint:disable=E0602
)
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("`Processing...`")
    input_type = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    search_results = []
    if input_type == "torrentz2.eu":
        search_results = search_torrentz_eu(input_str)
    elif input_type == "idop.se":
        search_results = search_idop_se(input_str)
    logger.info(search_results)  # pylint:disable=E0602
    output_str = ""
    i = 0
    for result in search_results:
        if i > 10:
            break
        message_text = (
            "👉 <a href=https://t.me/TorrentSearchRoBot?start="
            + result["hash"]
            + ">"
            + result["title"]
            + ": "
            + "</a>"
            + " \r\n"
        )
        message_text += " FILE SIZE: " + result["size"] + "\r\n"
        # message_text += " Uploaded " + result["date"] + "\r\n"
        message_text += (
            " SEEDS: " + result["seeds"] + " PEERS: " + result["peers"] + " \r\n"
        )
        message_text += "===\r\n"
        output_str += message_text
        i += 1
    end = datetime.now()
    ms = (end - start).seconds
    await event.edit(
        f"Scrapped {input_type} for {input_str} in {ms} seconds. Obtained Results: \n {output_str}",
        link_preview=False,
        parse_mode="html",
    )


def search_idop_se(search_query):
    r = []
    url = "https://idope.se/search/{}/".format(search_query)
    raw_json = requests.get(url).json()
    results = raw_json["result"]["items"]
    for item in results:
        """The content scrapped on 24.09.2018 22:56:45"""
        title = item["name"]
        hash = item["info_hash"]
        age = item["create_time"]
        size = item["length"]
        seeds = str(item["seeds"])
        r.append(
            {
                "title": title,
                "hash": hash,
                "age": age,
                "size": humanbytes(size),
                "seeds": seeds,
                "peers": "NA",
            }
        )
    return r


def search_torrentz_eu(search_query):
    r = []
    url = "https://torrentz2.eu/searchA?safe=1&f=" + search_query + ""
    scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
    raw_html = scraper.get(url).content
    # print(raw_html)
    soup = bs(raw_html, "html.parser")
    results = soup.find_all("div", {"class": "results"})
    # print(results)
    if len(results) > 0:
        results = results[0]
        for item in results.find_all("dl"):
            # print(item)
            """The content scrapped on 23.06.2018 15:40:35"""
            dt = item.find_all("dt")[0]
            dd = item.find_all("dd")[0]
            #
            try:
                link_and_text = dt.find_all("a")[0]
                link = link_and_text.get("href")[1:]
                title = link_and_text.get_text()
                span_elements = dd.find_all("span")
                date = span_elements[1].get_text()
                size = span_elements[2].get_text()
                seeds = span_elements[3].get_text()
                peers = span_elements[4].get_text()
                #
                r.append(
                    {
                        "title": title,
                        "hash": link,
                        "date": date,
                        "size": size,
                        "seeds": seeds,
                        "peers": peers,
                    }
                )
            except BaseException:
                pass
    return r
