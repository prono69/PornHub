"""Carbon Scraper Plugin for Userbot. //text in creative way.
usage: .kar1 //as a reply to any text message

Thanks to @r4v4n4 for vars"""
import os
from time import sleep
from urllib.parse import quote_plus

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="kar1 ?(.*)", allow_sudo=True))
async def carbon_api(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        """ A Wrapper for carbon.now.sh """
        hmm = await e.reply("🔲🔲🔲🔲🔲")
        CARBON = "https://carbon.now.sh/?bg=rgba(249%2C237%2C212%2C0)&t=synthwave-84&wt=none&l=application%2Fjson&ds=true&dsyoff=20px&dsblur=0px&wc=true&wa=true&pv=56px&ph=0px&ln=false&fl=1&fm=IBM%20Plex%20Mono&fs=14.5px&lh=153%25&si=false&es=4x&wm=false&code={code}"
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
        await hmm.edit("🔳🔳🔲🔲🔲")

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

        driver.find_element_by_xpath(
            '//*[@id="__next"]/main/div[3]/div[2]/div[1]/div[1]/div/span[2]'
        ).click()
        driver.find_element_by_id("export-menu").click()

        # removing below line coz seems no use now
        # driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()

        sleep(5)  # this might take a bit.
        driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
        sleep(5)
        await hmm.edit("🔳🔳🔳🔲🔲")
        driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
        sleep(5)  # Waiting for downloading

        await hmm.edit("🔳🔳🔳🔳🔳")
        file = "./carbon.png"
        await hmm.edit("☣️Karbon1 Completed, Uploading Karbon☣️")
        await e.client.send_file(
            e.chat_id,
            file,
            caption="Karbon1 by [@PhycoNinja13b](https://github.com/Phyco-Ninja/UniNinja)",
            force_document=True,
            reply_to=e.message.reply_to_msg_id,
        )

        os.remove("./carbon.png")
        # Removing carbon.png after uploading
        await hmm.delete()  # Deleting msg
