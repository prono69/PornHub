"""

Let me Google / YouTube / DuckDuckGo / altnews / Xvideo / Xvideos2/ Pornhub / var / log / Dyno that for you!

Syntax:

 .lmg <search query>

 .lmy <search query>

 .lmd <search query>

 .lmalt <search news>

 .lmx <search porn>

 .lmx2 <search porn> in xvideos2

 .lmp <search porn>

 .lmvar <heroku app name>

 .lmlog <heroku app name>

 .dyno <type billing>

 .lmkp


"""


import requests

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="lmg (.*)"))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    sample_url = "https://da.gd/s?url=http://google.com/search?q={}".format(
        input_str.replace(" ", "+")
    )

    response_api = requests.get(sample_url).text

    if response_api:

        await event.edit(
            "Let me **Googal** that for you:\n👉 [{}]({})\n`Le link dal de apne piche, Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )

    else:

        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="lmy (.*)"))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    sample_url = (
        "https://da.gd/s?url=https://www.youtube.com/results?search_query={}".format(
            input_str.replace(" ", "+")
        )
    )

    response_api = requests.get(sample_url).text

    if response_api:

        await event.edit(
            "Let me **UThooB** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )

    else:

        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="lmd (.*)"))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    sample_url = (
        "https://da.gd/s?url=https://duckduckgo.com/?q={}&t=h_&ia=about".format(
            input_str.replace(" ", "+")
        )
    )

    response_api = requests.get(sample_url).text

    if response_api:

        await event.edit(
            "Let me **DuckDuckGo** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )

    else:

        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="lmx (.*)"))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    sample_url = "https://da.gd/s?url=https://www.xvideos.com/?k={}".format(
        input_str.replace(" ", "+")
    )

    response_api = requests.get(sample_url).text

    if response_api:

        await event.edit(
            "Let me **xvideo** that for you:\n👉 [{}]({})\n`Maze kar Bsdk, Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )

    else:

        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="lmp (.*)"))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    sample_url = (
        "https://da.gd/s?url=https://www.pornhub.com/video/search?search={}".format(
            input_str.replace(" ", "+")
        )
    )

    response_api = requests.get(sample_url).text

    if response_api:

        await event.edit(
            "Let me **pornhub** that for you:\n👉 [{}]({})\n`Le Tharak ke pujari, Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )

    else:

        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="lmalt (.*)"))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    sample_url = "https://da.gd/s?url=https://www.altnews.in/?s={}".format(
        input_str.replace(" ", "+")
    )

    response_api = requests.get(sample_url).text

    if response_api:

        await event.edit(
            "Let me **altnews** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )

    else:

        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="lmvar (.*)"))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    sample_url = (
        "https://da.gd/s?url=https://dashboard.heroku.com/apps/{}/settings".format(
            input_str.replace(" ", "+")
        )
    )

    response_api = requests.get(sample_url).text

    if response_api:

        await event.edit(
            "Let me **var** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )

    else:

        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="lmlog (.*)"))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    sample_url = "https://da.gd/s?url=https://dashboard.heroku.com/apps/{}/logs".format(
        input_str.replace(" ", "+")
    )

    response_api = requests.get(sample_url).text

    if response_api:

        await event.edit(
            "Let me **log** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )

    else:

        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="lmx2 (.*)"))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    sample_url = "https://da.gd/s?url=https://www.xvideos2.com/?k={}".format(
        input_str.replace(" ", "+")
    )

    response_api = requests.get(sample_url).text

    if response_api:

        await event.edit(
            "Let me **xvideos** that for you:\n👉 [{}]({})\n`Katei Tharki ho raha hain launda, Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )

    else:

        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="lmkp (.*)"))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    sample_url = "https://da.gd/s?url=https://indiankanoon.org/search/?formInput={}+sortby%3Amostrecent".format(
        input_str.replace(" ", "+")
    )

    response_api = requests.get(sample_url).text

    if response_api:

        await event.edit(
            "Let me **Indiankanoon.com :** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )

    else:

        await event.edit("Something went wrong. Please try again later.")
