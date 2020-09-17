"""COMMAND : .dns , .link, .unshort , .myip , .myisp , .myhead , .mywho , .myup , .iifast"""
import requests

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="dns (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/dns/{}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit("DNS Records of {} are \n{}".format(input_str, response_api))
    else:
        await event.edit("I can't seem to Find {} on the internet".format(input_str))


@borg.on(admin_cmd(pattern="link (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit("Generated {} for {}.".format(response_api, input_str))
    else:
        await event.edit("Something is Wrong. Please try Again Later.")


@borg.on(admin_cmd(pattern="unshort (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not input_str.startswith("http"):
        input_str = "http://" + input_str
    r = requests.get(input_str, allow_redirects=False)
    if str(r.status_code).startswith("3"):
        await event.edit(
            "Input URL: {}\nReDirected URL: {}".format(input_str, r.headers["Location"])
        )
    else:
        await event.edit(
            "Input URL {} returned status_code {}".format(input_str, r.status_code)
        )


@borg.on(admin_cmd(pattern="myip(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/ip".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit("**Ip Of My Userbot:**{}\n{}".format(input_str, response_api))
    else:
        await event.edit("I can't seem to find {} on the internet".format(input_str))


@borg.on(admin_cmd(pattern="myisp(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/isp".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit("**My Current ISP:**{}\n{}".format(input_str, response_api))
    else:
        await event.edit("I can't seem to find {} on the internet".format(input_str))


@borg.on(admin_cmd(pattern="mywho (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/w/{}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit("**Whois:**\n{}\n{}".format(input_str, response_api))
    else:
        await event.edit("I can't seem to find {} on the internet".format(input_str))


@borg.on(admin_cmd(pattern="myhead (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/headers/{}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit("**Header:**\n{}\n{}".format(input_str, response_api))
    else:
        await event.edit("i can't seem to find {} on the internet".format(input_str))


@borg.on(admin_cmd(pattern="myup (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/up/{}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit(
            "`Is Website Up????`\n ☞ {}\n\n\nAns: `{}`".format(input_str, response_api)
        )
    else:
        await event.edit("I can't seem to find {} on the internet".format(input_str))


@borg.on(admin_cmd(pattern="iifast(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://tools.keycdn.com/geo".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit(
            "`Here's What I Found:`\n{}\n{}".format(input_str, response_api)
        )
    else:
        await event.edit("I can't seem to find {} on the internet".format(input_str))
