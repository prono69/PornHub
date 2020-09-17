"""
Carbon Scraper Plugin for Userbot. //text in creative way.
usage: .carbon //as a reply to any text message

Thanks to @NeoMatrix90 for vars

Type : .kar00

"""
import asyncio
import os
from urllib.parse import quote_plus

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from uniborg.util import admin_cmd

CARBONLANG = "auto"


@borg.on(admin_cmd(pattern="crblang ?(.*)"))
async def setlang(prog):
    global CARBONLANG
    CARBONLANG = prog.pattern_match.group(1)
    await prog.edit(f"Language for carbon.now.sh set to {CARBONLANG}")


@borg.on(admin_cmd(pattern="kar00 ?(.*)"))
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    await e.edit("`Processing..`")
    CARBON = "https://carbon.now.sh/?l={lang}&code={code}"
    global CARBONLANG
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    await e.edit("`Processing..\n25%`")
    if os.path.isfile("./carbon.png"):
        os.remove("./carbon.png")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = Config.CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "./"}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        executable_path=Config.CHROME_DRIVER, options=chrome_options
    )
    driver.get(url)
    await e.edit("`Processing..\n50%`")
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
    driver.find_element_by_xpath(
        '//*[@id="__next"]/main/div[3]/div[2]/div[1]/div[1]/div/span[2]'
    ).click()
    driver.find_element_by_id("export-menu").click()
    # driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
    driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
    driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await e.edit("`Processing..\n75%`")
    # Waiting for downloading
    while not os.path.isfile("./carbon.png"):
        await asyncio.sleep(0.5)
    await e.edit("`Processing..\n100%`")
    file = "./carbon.png"
    await e.edit("`Uploading..`")
    await e.client.send_file(
        e.chat_id,
        file,
        caption="Made using [Carbon](https://carbon.now.sh/about/),\
        \na project by [Dawn Labs](https://dawnlabs.io/)",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )

    os.remove("./carbon.png")
    driver.quit()
    # Removing carbon.png after uploading
    await e.delete()  # Deleting msg
