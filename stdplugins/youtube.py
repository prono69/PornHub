# kanged from AbhiNash Reddy's PPE (THX)

"""It will search youtube videos using Api
\n`Type .yts (anynumber(maximum 50)) {ur query}`
\nAll thanks goes to **SNAPDRAGON** . Thnaks a lot Bruh..
\nPorted by © [EYEPATCH](t.me/neomatrix90)
\n`Don't Copy Without Credits.`"""
from html import unescape

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern=r"yts ?(\d+)? ?(.*)?"))
async def yt_search(video_q):
    """For .yt command, do a YouTube search from Telegram."""
    reply = await video_q.get_reply_message()
    if video_q.pattern_match.group(2):
        query = video_q.pattern_match.group(2)
    elif reply:
        query = reply.message
    else:
        return await video_q.edit("Invalid syntax")
    resultamt = (
        int(video_q.pattern_match.group(1))
        if video_q.pattern_match.group(1) is not None
        else 10
    )
    result = ""
    if Config.YOUTUBE_API_KEY is None:
        await video_q.edit(
            "`Error: YouTube API key missing!\
            Add it to environment vars or config.env.`"
        )
        return

    await video_q.edit("```Processing...```")

    full_response = youtube_search(query, resultamt=resultamt)
    videos_json = full_response[1]

    for i, video in enumerate(videos_json, start=1):
        result += f"{i}. [{unescape(video['snippet']['title'])}]\
(https://www.youtube.com/watch?v={video['id']['videoId']})\n\n"

    reply_text = f"**Search Query:**\n`{query}`\n\n**Result:**\n{result}"

    await video_q.edit(reply_text)


def youtube_search(
    query,
    order="relevance",
    token=None,
    location=None,
    location_radius=None,
    resultamt=10,
):
    """Do a YouTube search."""
    youtube = build(
        "youtube", "v3", developerKey=Config.YOUTUBE_API_KEY, cache_discovery=False
    )
    search_response = (
        youtube.search()
        .list(
            q=query,
            type="video",
            pageToken=token,
            order=order,
            part="id,snippet",
            maxResults=resultamt,
            location=location,
            locationRadius=location_radius,
        )
        .execute()
    )

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append(search_result)
    try:
        nexttok = search_response["nextPageToken"]
        return (nexttok, videos)
    except HttpError:
        nexttok = "last_page"
        return (nexttok, videos)
    except KeyError:
        nexttok = "KeyError, try again."
        return (nexttok, videos)
