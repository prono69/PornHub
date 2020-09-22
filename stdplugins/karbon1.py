"""
Carbon Scraper Plugin for Userbot. //text in creative way.
usage: .karbon1 //as a reply to any text message

Thanks to @r4v4n4 for vars

"""
import os
from time import sleep
from urllib.parse import quote_plus

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from telethon import events


@borg.on(events.NewMessage(pattern=r"\.karbon1", outgoing=True))
async def carbon_api(e):
    if e.text[0].isalpha() or e.text[0] in ("/", "#", "@", "!"):
        return

    """ A Wrapper for carbon.now.sh """
    await e.edit("⬜⬜⬜⬜⬜")
    CARBON = "https://carbon.now.sh/?bg=rgba(239%2C40%2C44%2C0)&t=one-light&wt=none&l={lang}&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=2x&wm=false&code={code}"
    CARBONLANG = "en"
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = Config.GOOGLE_CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "./"}
    chrome_options.add_experimental_option("prefs", prefs)
    await e.edit("⬛⬛⬜⬜⬜")

    driver = webdriver.Chrome(
        executable_path=Config.CHROME_DRIVER, options=chrome_options
    )
    driver.get(url)
    download_path = "./"
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_path},
    }
    driver.execute("send_command", params)

    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
    sleep(5)  # this might take a bit.
    driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
    sleep(5)
    await e.edit("⬛⬛⬛⬜⬜")
    driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    sleep(5)  # Waiting for downloading

    await e.edit("⬛⬛⬛⬛⬛")
    file = "./carbon.png"
    await e.edit("✅Karbon1 Completed, Uploading Karbon✅")
    await e.client.send_file(
        e.chat_id,
        file,
        caption="Karbon1 by [@NeoMatrix90](https://www.github.com/prono69/PepeBot)",
        force_document=False,
        reply_to=e.message.reply_to_msg_id,
    )

    os.remove("./carbon.png")
    # Removing carbon.png after uploading
    await e.delete()  # Deleting msg
