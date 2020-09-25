"""FFMpeg for @UniBorg
"""
import asyncio
import os
import time
from datetime import datetime

from uniborg.util import admin_cmd, cult_small_video, progress, take_screen_shot


@borg.on(admin_cmd(pattern="ftrim"))
async def ff_mpeg_trim_cmd(event):
    if event.fwd_from:
        return

    FF_MPEG_DOWN_LOAD_MEDIA_PATH = await bleck_megic(event)
    logger.info(FF_MPEG_DOWN_LOAD_MEDIA_PATH)

    if FF_MPEG_DOWN_LOAD_MEDIA_PATH is None:
        await event.edit("please set the required ENVironment VARiables")
        return

    current_message_text = event.raw_text
    cmt = current_message_text.split(" ")
    logger.info(cmt)
    start = datetime.now()
    if len(cmt) == 3:
        # output should be video
        cmd, start_time, end_time = cmt
        o = await cult_small_video(
            FF_MPEG_DOWN_LOAD_MEDIA_PATH,
            Config.TMP_DOWNLOAD_DIRECTORY,
            start_time,
            end_time,
        )
        logger.info(o)
        try:
            c_time = time.time()
            await borg.send_file(
                event.chat_id,
                o,
                caption=" ".join(cmt[1:]),
                force_document=False,
                supports_streaming=True,
                allow_cache=False,
                # reply_to=event.message.id,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, event, c_time, "trying to upload")
                ),
            )
            os.remove(o)
        except Exception as e:
            logger.info(str(e))
    elif len(cmt) == 2:
        # output should be image
        cmd, start_time = cmt
        o = await take_screen_shot(
            FF_MPEG_DOWN_LOAD_MEDIA_PATH, Config.TMP_DOWNLOAD_DIRECTORY, start_time
        )
        logger.info(o)
        try:
            c_time = time.time()
            await borg.send_file(
                event.chat_id,
                o,
                caption=" ".join(cmt[1:]),
                force_document=True,
                # supports_streaming=True,
                allow_cache=False,
                # reply_to=event.message.id,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, event, c_time, "trying to upload")
                ),
            )
            os.remove(o)
        except Exception as e:
            logger.info(str(e))
    else:
        await event.edit("RTFM")
        return
    end = datetime.now()
    ms = (end - start).seconds
    await event.edit(f"Completed Process in {ms} seconds")


async def bleck_megic(evt_message) -> str:
    if Config.LT_QOAN_NOE_FF_MPEG_URL is None or Config.LT_QOAN_NOE_FF_MPEG_CTD is None:
        return None
    r_m_y = await evt_message.get_reply_message()
    fwd_mesg = await r_m_y.forward_to(Config.LT_QOAN_NOE_FF_MPEG_CTD)
    return Config.LT_QOAN_NOE_FF_MPEG_URL.format(message_id=fwd_mesg.id)
