# Thanks to @AvinashReddy3108 for this plugin

"""
Audio and video downloader using Youtube-dl
.yta To Download in mp3 format
.ytv To Download in mp4 format
"""
import asyncio
import logging
import math
import os
import re
import time

from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)

from uniborg.util import admin_cmd

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)


DELETE_TIMEOUT = 5


async def progress(current, total, event, start, type_of_ps, file_name=None):
    """Generic progress_callback for uploads and downloads."""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join(["█" for i in range(math.floor(percentage / 10))]),
            "".join(["░" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            await event.edit(
                "{}\nFile Name: `{}`\n{}".format(type_of_ps, file_name, tmp)
            )
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


def humanbytes(size):
    """Input size in bytes,
    outputs in a human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " day(s), ") if days else "")
        + ((str(hours) + " hour(s), ") if hours else "")
        + ((str(minutes) + " minute(s), ") if minutes else "")
        + ((str(seconds) + " second(s), ") if seconds else "")
        + ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    )
    return tmp[:-2]


@borg.on(admin_cmd(pattern="yt(a|v) ?(.*)"))
async def download_video(v_url):
    """ For .ytdl command, download media from YouTube and many other sites. """
    reply = await v_url.get_reply_message()
    if v_url.pattern_match.group(2) != "":
        url = v_url.pattern_match.group(2)
    elif reply is not None:
        url = reply.message
        url = re.findall(r"\bhttps?://.*\.\S+", reply.message)[0]
    else:
        return
    type = (
        v_url.pattern_match.group(1).lower()
        if v_url.pattern_match.group(1) is not None
        else "a"
    )
    out_folder = Config.TMP_DOWNLOAD_DIRECTORY + "youtubedl/"
    Config.TMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"
    if not os.path.isdir(out_folder):
        os.makedirs(out_folder)
    await v_url.edit("`Preparing to download...`")

    if type == "a":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "embedthumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": out_folder + "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
        video = False
        song = True

    elif type == "v":
        opts = {
            "format": "best",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "getthumbnail": True,
            "embedthumbnail": True,
            "writethumbnail": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}
            ],
            "outtmpl": out_folder + "%(id)s.mp4",
            "logtostderr": False,
            "quiet": True,
        }
        song = False
        video = True

    try:
        await v_url.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url)
        filename = sorted(get_lst_of_files(out_folder, []))
    except DownloadError as DE:
        await v_url.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await v_url.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await v_url.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await v_url.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await v_url.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await v_url.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await v_url.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await v_url.edit("`There was an error during info extraction.`")
        return
    except Exception as e:
        await v_url.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    if song:
        # raster_size = os.path.getsize(f"{out_folder + ytdl_data['id']}.mp3")
        # song_size = size(raster_size)
        thumb = (
            f"{out_folder + ytdl_data['id']}.mp3"[
                : (len(f"{out_folder + ytdl_data['id']}.mp3") - 4)
            ]
            + ".jpg"
        )
        file_path = f"{out_folder + ytdl_data['id']}.mp3"
        song_size = file_size(file_path)
        await v_url.edit(
            f"`Preparing to upload song:`\
        \n**{ytdl_data['title']}**\
        \nby *{ytdl_data['uploader']}*"
        )
        await v_url.client.send_file(
            v_url.chat_id,
            f"{out_folder + ytdl_data['id']}.mp3",
            caption=ytdl_data["title"] + "\n" + f"`{song_size}`",
            supports_streaming=True,
            thumb=thumb,
            attributes=[
                DocumentAttributeAudio(
                    duration=int(ytdl_data["duration"]),
                    title=str(ytdl_data["title"]),
                    performer=str(ytdl_data["uploader"]),
                )
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, v_url, c_time, "Uploading..", f"{ytdl_data['title']}.mp3"
                )
            ),
        )
        os.remove(f"{out_folder + ytdl_data['id']}.mp3")
        await asyncio.sleep(DELETE_TIMEOUT)
        await v_url.delete()
        os.removedirs(out_folder)
    elif video:
        for single_file in filename:
            # image_link = ytdl_data['thumbnail']
            # downloaded_image = wget.download(image_link,out_folder)
            # thumb = downloaded_image
            # raster_size = os.path.getsize(f"{out_folder + ytdl_data['id']}.mp4")
            file_path = f"{out_folder + ytdl_data['id']}.mp4"
            video_size = file_size(file_path)
            f"{ytdl_data['id']}.jpg"
            thumb = f"{out_folder + ytdl_data['id']}.jpg"
            await v_url.edit(
                f"`Preparing to upload video:`\
            \n**{ytdl_data['title']}**\
            \nby *{ytdl_data['uploader']}*"
            )
            await v_url.client.send_file(
                v_url.chat_id,
                f"{out_folder + ytdl_data['id']}.mp4",
                supports_streaming=True,
                caption=ytdl_data["title"] + "\n" + f"`{video_size}`",
                thumb=thumb,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(
                        d, t, v_url, c_time, "Uploading..", f"{ytdl_data['title']}.mp4"
                    )
                ),
            )
            os.remove(f"{out_folder + ytdl_data['id']}.mp4")
            await asyncio.sleep(DELETE_TIMEOUT)
            await v_url.delete()
        os.removedirs(out_folder)


def get_lst_of_files(input_directory, output_lst):
    filesinfolder = os.listdir(input_directory)
    for file_name in filesinfolder:
        current_file_name = os.path.join(input_directory, file_name)
        if os.path.isdir(current_file_name):
            return get_lst_of_files(current_file_name, output_lst)
        output_lst.append(current_file_name)
    return output_lst


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ["bytes", "KB", "MB", "GB", "TB"]:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)
