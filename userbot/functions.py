import os
import time
import shlex
import asyncio
import requests
from PIL import Image
from os.path import basename
from bs4 import BeautifulSoup
from telethon.tl.types import Channel
from typing import Optional, Tuple

# gban


async def admin_groups(cat):
    catgroups = []
    async for dialog in cat.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            if entity.megagroup:
                if entity.creator or entity.admin_rights:
                    catgroups.append(entity.id)
    return catgroups

# For using gif , animated stickers and videos in some parts , this
# function takes  take a screenshot and stores ported from userge


async def take_screen_shot(video_file: str, duration: int, path: str = '') -> Optional[str]:
    print(
        '[[[Extracting a frame from %s ||| Video duration => %s]]]',
        video_file,
        duration)
    ttl = duration // 2
    thumb_image_path = path or os.path.join(
        "./temp/", f"{basename(video_file)}.jpg")
    command = f"ffmpeg -ss {ttl} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        print(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None

# executing of terminal commands


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(*args,
                                                   stdout=asyncio.subprocess.PIPE,
                                                   stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    return (stdout.decode('utf-8', 'replace').strip(),
            stderr.decode('utf-8', 'replace').strip(),
            process.returncode,
            process.pid)

# for getmusic


async def catmusic(cat, QUALITY):
    search = cat
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    html = requests.get(
        'https://www.youtube.com/results?search_query=' +
        search,
        headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        if '/watch?v=' in link.get('href'):
            # May change when Youtube Website may get updated in the future.
            video_link = link.get('href')
            break
    video_link = 'http://www.youtube.com/' + video_link
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    command = (
        'youtube-dl -o "./temp/%(title)s.%(ext)s" --extract-audio --audio-format mp3 --audio-quality ' +
        QUALITY +
        ' ' +
        video_link)
    os.system(command)
    thumb = (
        'youtube-dl -o "./temp/%(title)s.%(ext)s" --write-thumbnail --skip-download ' +
        video_link)
    os .system(thumb)


async def catmusicvideo(cat):
    search = cat
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    html = requests.get(
        'https://www.youtube.com/results?search_query=' +
        search,
        headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        if '/watch?v=' in link.get('href'):
            # May change when Youtube Website may get updated in the future.
            video_link = link.get('href')
            break
    video_link = 'http://www.youtube.com/' + video_link
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    command = (
        'youtube-dl -o "./temp/%(title)s.%(ext)s" -f "[filesize<20M]" ' +
        video_link)
    os.system(command)
    thumb = (
        'youtube-dl -o "./temp/%(title)s.%(ext)s" --write-thumbnail --skip-download ' +
        video_link)
    os .system(thumb)

# https://github.com/pokurt/LyndaRobot/blob/7556ca0efafd357008131fa88401a8bb8057006f/lynda/modules/helper_funcs/string_handling.py#L238


async def extract_time(cat, time_val):
    if any(time_val.endswith(unit) for unit in ('m', 'h', 'd', 'w')):
        unit = time_val[-1]
        time_num = time_val[:-1]  # type: str
        if not time_num.isdigit():
            cat.edit("Invalid time amount specified.")
            return ""
        if unit == 'm':
            bantime = int(time.time() + int(time_num) * 60)
        elif unit == 'h':
            bantime = int(time.time() + int(time_num) * 60 * 60)
        elif unit == 'd':
            bantime = int(time.time() + int(time_num) * 24 * 60 * 60)
        elif unit == 'w':
            bantime = int(time.time() + int(time_num) * 7 * 24 * 60 * 60)
        else:
            # how even...?
            return ""
        return bantime
    cat.edit("Invalid time type specified. Expected m , h , d or w but got: {}".format(
        time_val[-1]))
    return ""


def convert_toimage(image):
    img = Image.open(image)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save("temp.jpg", "jpeg")
    os.remove(image)
    return "temp.jpg"


async def iphonex(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=iphonex&url={text}").json()
    sandy = r.get("message")
    if not sandy:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def baguette(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=baguette&url={text}").json()
    sandy = r.get("message")
    if not sandy:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def threats(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=threats&url={text}").json()
    sandy = r.get("message")
    if not sandy:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def lolice(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=lolice&url={text}").json()
    sandy = r.get("message")
    if not sandy:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def trash(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trash&url={text}").json()
    sandy = r.get("message")
    if not sandy:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def awooify(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=awooify&url={text}").json()
    sandy = r.get("message")
    if not sandy:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def trap(text1, text2, text3):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trap&name={text1}&author={text2}&image={text3}").json()
    sandy = r.get("message")
    if not sandy:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def phcomment(text1, text2, text3):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=phcomment&image={text1}&text={text2}&username={text3}").json()
    sandy = r.get("message")
    if not sandy:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"
