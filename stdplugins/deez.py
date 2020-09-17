import requests

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="deez (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = (
        "https://song.link/redirect?url="
        + event.pattern_match.group(1)
        + "&to=deezer&web=true"
    )
    if not input_str.startswith("http"):
        input_str = "http://" + input_str
    r = requests.get(input_str, allow_redirects=False)
    if str(r.status_code).startswith("3"):
        await event.edit("{}".format(r.headers["Location"]))
    else:
        await event.edit(
            "Input URL {} returned status_code {}".format(input_str, r.status_code)
        )
