# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing various sites direct links generators"""
import asyncio
import json
import logging
import re
import urllib.parse
from os import popen
from random import choice

import aiohttp
import requests
from bs4 import BeautifulSoup
from humanize import naturalsize
from telethon import events

from uniborg.util import time_formatter

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.WARN
)

USR_TOKEN = Config.USR_TOKEN


@borg.on(events.NewMessage(pattern=r"^.direct(?: |$)([\s\S]*)", outgoing=True))
async def direct_link_generator(request):
    """direct links generator"""
    await request.edit("`Processing...`")
    textx = await request.get_reply_message()
    message = request.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await request.edit("`Usage: .direct <url>`")
        return
    reply = ""
    links = re.findall(r"\bhttps?://.*\.\S+", message)
    if not links:
        reply = "`No links found!`"
        await request.edit(reply)
    for link in links:
        if "drive.google.com" in link:
            reply += gdrive(link)
        elif "zippyshare.com" in link:
            reply += zippy_share(link)
        elif "mega." in link:
            reply += mega_dl(link)
        elif "yadi.sk" in link:
            reply += yandex_disk(link)
        elif "cloud.mail.ru" in link:
            reply += cm_ru(link)
        elif "mediafire.com" in link:
            reply += mediafire(link)
        elif "sourceforge.net" in link:
            reply += sourceforge(link)
        elif "osdn.net" in link:
            reply += osdn(link)
        elif "github.com" in link:
            reply += github(link)
        elif "androidfilehost.com" in link:
            reply += androidfilehost(link)
        elif "uptobox.com" in link:
            reply += await uptobox(request, link)
        else:
            reply += (
                "`"
                + re.findall(r"\bhttps?://(.*?[^/]+)", link)[0]
                + "is not supported`\n"
            )
    await request.edit(reply)


def gdrive(url: str) -> str:
    """GDrive direct links generator"""
    drive = "https://drive.google.com"
    try:
        link = re.findall(r"\bhttps?://drive\.google\.com\S+", url)[0]
    except IndexError:
        reply = "`No Google drive links found`\n"
        return reply
    file_id = ""
    reply = ""
    if link.find("view") != -1:
        file_id = link.split("/")[-2]
    elif link.find("open?id=") != -1:
        file_id = link.split("open?id=")[1].strip()
    elif link.find("uc?id=") != -1:
        file_id = link.split("uc?id=")[1].strip()
    url = f"{drive}/uc?export=download&id={file_id}"
    download = requests.get(url, stream=True, allow_redirects=False)
    cookies = download.cookies
    try:
        # In case of small file size, Google downloads directly
        dl_url = download.headers["location"]
        if "accounts.google.com" in dl_url:  # non-public file
            reply += "`Link is not public!`\n"
            return reply
        name = "Direct Download Link"
    except KeyError:
        # In case of download warning page
        page = BeautifulSoup(download.content, "lxml")
        export = drive + page.find("a", {"id": "uc-download-link"}).get("href")
        name = page.find("span", {"class": "uc-name-size"}).text
        response = requests.get(
            export, stream=True, allow_redirects=False, cookies=cookies
        )
        dl_url = response.headers["location"]
        if "accounts.google.com" in dl_url:
            reply += "`Link is not public!`\n"
            return reply
    reply += f"[{name}]({dl_url})\n"
    return reply


def zippy_share(url: str) -> str:
    """ZippyShare direct links generator
    Based on https://github.com/LameLemon/ziggy"""
    reply = ""
    dl_url = ""
    try:
        link = re.findall(r"\bhttps?://.*zippyshare\.com\S+", url)[0]
    except IndexError:
        reply = "`No ZippyShare links found`\n"
        return reply
    session = requests.Session()
    base_url = re.search("http.+.com", link).group()
    response = session.get(link)
    page_soup = BeautifulSoup(response.content, "lxml")
    scripts = page_soup.find_all("script", {"type": "text/javascript"})
    for script in scripts:
        if "getElementById('dlbutton')" in script.text:
            url_raw = re.search(
                r"= (?P<url>\".+\" \+ (?P<math>\(.+\)) .+);", script.text
            ).group("url")
            math = re.search(
                r"= (?P<url>\".+\" \+ (?P<math>\(.+\)) .+);", script.text
            ).group("math")
            dl_url = url_raw.replace(math, '"' + str(eval(math)) + '"')
            break
    dl_url = base_url + eval(dl_url)
    name = urllib.parse.unquote(dl_url.split("/")[-1])
    reply += f"[{name}]({dl_url})\n"
    return reply


def yandex_disk(url: str) -> str:
    """Yandex.Disk direct links generator
    Based on https://github.com/wldhx/yadisk-direct"""
    reply = ""
    try:
        link = re.findall(r"\bhttps?://.*yadi\.sk\S+", url)[0]
    except IndexError:
        reply = "`No Yandex.Disk links found`\n"
        return reply
    api = "https://cloud-api.yandex.net/v1/disk/"
    api += "public/resources/download?public_key={}"
    try:
        dl_url = requests.get(api.format(link)).json()["href"]
        name = dl_url.split("filename=")[1].split("&disposition")[0]
        reply += f"[{name}]({dl_url})\n"
    except KeyError:
        reply += "`Error: File not found / Download limit reached`\n"
        return reply
    return reply


def mega_dl(url: str) -> str:
    """MEGA.nz direct links generator
    Using https://github.com/tonikelope/megadown"""
    reply = ""
    try:
        link = re.findall(r"\bhttps?://.*mega.*\.nz\S+", url)[0]
    except IndexError:
        reply = "`No MEGA.nz links found`\n"
        return reply
    command = f"bin/megadown -q -m {link}"
    result = popen(command).read()
    try:
        data = json.loads(result)
    except json.JSONDecodeError:
        reply += "`Error: Can't extract the link`\n"
        return reply
    dl_url = data["url"]
    name = data["file_name"]
    size = naturalsize(int(data["file_size"]))
    reply += f"[{name} ({size})]({dl_url})\n"
    return reply


def cm_ru(url: str) -> str:
    """cloud.mail.ru direct links generator
    Using https://github.com/JrMasterModelBuilder/cmrudl.py"""
    reply = ""
    try:
        link = re.findall(r"\bhttps?://.*cloud\.mail\.ru\S+", url)[0]
    except IndexError:
        reply = "`No cloud.mail.ru links found`\n"
        return reply
    command = f"bin/cmrudl -s {link}"
    result = popen(command).read()
    result = result.splitlines()[-1]
    try:
        data = json.loads(result)
    except json.decoder.JSONDecodeError:
        reply += "`Error: Can't extract the link`\n"
        return reply
    dl_url = data["download"]
    name = data["file_name"]
    size = naturalsize(int(data["file_size"]))
    reply += f"[{name} ({size})]({dl_url})\n"
    return reply


def mediafire(url: str) -> str:
    """MediaFire direct links generator"""
    try:
        link = re.findall(r"\bhttps?://.*mediafire\.com\S+", url)[0]
    except IndexError:
        reply = "`No MediaFire links found`\n"
        return reply
    reply = ""
    page = BeautifulSoup(requests.get(link).content, "lxml")
    info = page.find("a", {"aria-label": "Download file"})
    dl_url = info.get("href")
    size = re.findall(r"\(.*\)", info.text)[0]
    name = page.find("div", {"class": "filename"}).text
    reply += f"[{name} {size}]({dl_url})\n"
    return reply


def sourceforge(url: str) -> str:
    """SourceForge direct links generator"""
    try:
        link = re.findall(r"\bhttps?://.*sourceforge\.net\S+", url)[0]
    except IndexError:
        reply = "`No SourceForge links found`\n"
        return reply
    file_path = re.findall(r"files(.*)/download", link)[0]
    reply = f"Mirrors for __{file_path.split('/')[-1]}__\n\n"
    project = re.findall(r"projects?/(.*?)/files", link)[0]
    mirrors = (
        f"https://sourceforge.net/settings/mirror_choices?"
        f"projectname={project}&filename={file_path}"
    )
    page = BeautifulSoup(requests.get(mirrors).content, "html.parser")
    info = page.find("ul", {"id": "mirrorList"}).findAll("li")
    for mirror in info[1:]:
        name = re.findall(r"\((.*)\)", mirror.text.strip())[0]
        dl_url = (
            f'https://{mirror["id"]}.dl.sourceforge.net/project/{project}/{file_path}'
        )
        reply += f"[{name}]({dl_url}) "
    return reply


def osdn(url: str) -> str:
    """OSDN direct links generator"""
    osdn_link = "https://osdn.net"
    try:
        link = re.findall(r"\bhttps?://.*osdn\.net\S+", url)[0]
    except IndexError:
        reply = "`No OSDN links found`\n"
        return reply
    page = BeautifulSoup(requests.get(link, allow_redirects=True).content, "lxml")
    info = page.find("a", {"class": "mirror_link"})
    link = urllib.parse.unquote(osdn_link + info["href"])
    reply = f"Mirrors for __{link.split('/')[-1]}__\n\n"
    mirrors = page.find("form", {"id": "mirror-select-form"}).findAll("tr")
    for data in mirrors[1:]:
        mirror = data.find("input")["value"]
        name = re.findall(r"\((.*)\)", data.findAll("td")[-1].text.strip())[0]
        dl_url = re.sub(r"m=(.*)&f", f"m={mirror}&f", link)
        reply += f"[{name}]({dl_url}) "
    return reply


def github(url: str) -> str:
    """GitHub direct links generator"""
    try:
        link = re.findall(r"\bhttps?://.*github\.com.*releases\S+", url)[0]
    except IndexError:
        reply = "`No GitHub Releases links found`\n"
        return reply
    reply = ""
    dl_url = ""
    download = requests.get(url, stream=True, allow_redirects=False)
    try:
        dl_url = download.headers["location"]
    except KeyError:
        reply += "`Error: Can't extract the link`\n"
    name = link.split("/")[-1]
    reply += f"[{name}]({dl_url}) "
    return reply


def androidfilehost(url: str) -> str:
    """AFH direct links generator"""

    try:
        link = re.findall(r"\bhttps?://.*androidfilehost.*fid.*\S+", url)[0]
    except IndexError:
        reply = "`No AFH links found`\n"
        return reply

    fid = re.findall(r"\?fid=(.*)", link)[0]
    session = requests.Session()
    user_agent = useragent()

    headers = {"user-agent": user_agent}
    res = session.get(link, headers=headers, allow_redirects=True)
    headers = {
        "origin": "https://androidfilehost.com",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "user-agent": user_agent,
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "x-mod-sbb-ctype": "xhr",
        "accept": "*/*",
        "referer": f"https://androidfilehost.com/?fid={fid}",
        "authority": "androidfilehost.com",
        "x-requested-with": "XMLHttpRequest",
    }

    data = {"submit": "submit", "action": "getdownloadmirrors", "fid": f"{fid}"}

    mirrors = None
    reply = ""
    error = "`Error: Can't find Mirrors for the link`\n"

    try:
        req = session.post(
            "https://androidfilehost.com/libs/otf/mirrors.otf.php",
            headers=headers,
            data=data,
            cookies=res.cookies,
        )
        mirrors = req.json()["MIRRORS"]
    except (json.decoder.JSONDecodeError, TypeError):
        reply += error

    if not mirrors:
        reply += error
        return reply

    for item in mirrors:
        name = item["name"]
        dl_url = item["url"]
        reply += f"[{name}]({dl_url}) "

    return reply


def useragent():
    """useragent random setter"""

    useragents = BeautifulSoup(
        requests.get(
            "https://developers.whatismybrowser.com/"
            "useragents/explore/operating_system_name/android/"
        ).content,
        "lxml",
    ).findAll("td", {"class": "useragent"})

    user_agent = choice(useragents)

    return user_agent.text


async def uptobox(request, url: str) -> str:
    """Uptobox direct links generator"""
    try:
        link = re.findall(r"\bhttps?://.*uptobox\.com\S+", url)[0]
    except IndexError:
        await request.edit("`No uptobox links found.`")
        return
    if USR_TOKEN is None:
        await request.edit("`Set USR_TOKEN_UPTOBOX first!`")
        return
    index = -2 if link.endswith("/") else -1
    FILE_CODE = link.split("/")[index]
    origin = "https://uptobox.com/api/link"
    """ Retrieve file informations """
    uri = f"{origin}/info?fileCodes={FILE_CODE}"
    await request.edit("`Retrieving file informations...`")
    async with aiohttp.ClientSession() as session:
        async with session.get(uri) as response:
            result = json.loads(await response.text())
            data = result.get("data").get("list")[0]
            if "error" in data:
                await request.edit(
                    "`[ERROR]`\n"
                    f"`statusCode`: **{data.get('error').get('code')}**\n"
                    f"`reason`: **{data.get('error').get('message')}**"
                )
                return
            file_name = data.get("file_name")
            file_size = naturalsize(data.get("file_size"))
    """ Get waiting token and direct download link """
    uri = f"{origin}?token={USR_TOKEN}&file_code={FILE_CODE}"
    async with aiohttp.ClientSession() as session:
        async with session.get(uri) as response:
            result = json.loads(await response.text())
            status = result.get("message")
            if status == "Waiting needed":
                wait = result.get("data").get("waiting")
                waitingToken = result.get("data").get("waitingToken")
                await request.edit(f"`Waiting for about {time_formatter(wait)}.`")
                # for some reason it doesn't go as i planned
                # so make it 1 minute just to be save enough
                await asyncio.sleep(wait + 60)
                uri += f"&waitingToken={waitingToken}"
                async with session.get(uri) as response:
                    await request.edit("`Generating direct download link...`")
                    result = json.loads(await response.text())
                    status = result.get("message")
                    if status == "Success":
                        webLink = result.get("data").get("dlLink")
                        await request.edit(f"[{file_name} ({file_size})]({webLink})")
                    else:
                        await request.edit(
                            "`[ERROR]`\n"
                            f"`statusCode`: **{result.get('statusCode')}**\n"
                            f"`reason`: **{result.get('data')}**\n"
                            f"`status`: **{status}**"
                        )
                    return
            elif status == "Success":
                webLink = result.get("data").get("dlLink")
                await request.edit(f"[{file_name} ({file_size})]({webLink})")
                return
            else:
                await request.edit(
                    "`[ERROR]`\n"
                    f"`statusCode`: **{result.get('statusCode')}**\n"
                    f"`reason`: **{result.get('data')}**\n"
                    f"`status`: **{status}**"
                )
                return
