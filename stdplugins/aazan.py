import json

import requests

from uniborg.util import admin_cmd

TEMPAT = ""

""" aazan: .aazan <city> or .aazan <country>
        \nUsage: Gets the prayer time for muslims.
 """


@borg.on(admin_cmd(pattern="aazan (.*)"))
async def get_adzan(adzan):
    if not adzan.text.startswith("."):
        return ""

    if not adzan.pattern_match.group(1):
        LOCATION = TEMPAT
        if not LOCATION:
            await adzan.edit("`Please specify a City or a State.`")
            return
    else:
        LOCATION = adzan.pattern_match.group(1)

    url = f"http://muslimsalat.com/{LOCATION}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    result = json.loads(request.text)

    if request.status_code != 200:
        await adzan.edit(f"{result['status_description']}")
        return

    date = result["items"][0]["date_for"]
    location = result["query"]
    location2 = result["country"]
    location3 = result["address"]
    location4 = result["state"]

    subuh = result["items"][0]["fajr"]
    #### syuruk = result["items"][0]["shurooq"]
    zuhur = result["items"][0]["dhuhr"]
    ashar = result["items"][0]["asr"]
    maghrib = result["items"][0]["maghrib"]
    isya = result["items"][0]["isha"]

    textkirim = (
        f"⏱  **Namaz Schedule** `{date}`:\n"
        + f"`{location} | {location3} | {location4} | {location2}`\n\n"
        + f"**Subuh :** `{subuh}`\n"
        +
        # f"**Syuruk :** `{syuruk}`\n" +
        f"**Zuhur :** `{zuhur}`\n"
        + f"**Ashar :** `{ashar}`\n"
        + f"**Maghrib :** `{maghrib}`\n"
        + f"**Isya :** `{isya}`\n"
    )

    await adzan.edit(textkirim)
