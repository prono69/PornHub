### ⚠️Warning: // **Multiple accounts are getting banned, // Hence, Use it at your own RISK .** :( /

#click_the_pepe_photo_below_to_deploy_or_the_deploy_button

[![Build](https://github.com/prono69/PepeBot/workflows/FailedChecker/badge.svg?branch=master)](https://github.com/prono69/PepeBot/actions "Build")
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/61152ca51cc6417bb9866562f3dfbf76)](https://app.codacy.com/manual/prono69/PepeBot?utm_source=github.com&utm_medium=referral&utm_content=prono69/PepeBot&utm_campaign=Badge_Grade_Settings)
[![Deploy](https://telegra.ph/file/aab0b657924e806b0c6c8.jpg)](https://heroku.com/deploy?template=https://github.com/prono69/PepeBot/tree/master)


DIS DEPLOY BUTTON.........



[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

#### Code Quality

[![CodeFactor](https://www.codefactor.io/repository/github/prono69/pepebot/badge)](https://www.codefactor.io/repository/github/prono69/pepebot)

#### The Legacy Way
Simply clone the repository and run the main file:
```sh
git clone https://github.com/muhammedfurkan/uniborg.git
cd uniborg
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create config.py with variables as given below>
python3 -m stdborg YourSessionName
```
 
An example `config.py` file could be:
 
**Not All of the variables are mandatory**
 
__The UniBorg should work by setting only these variables__
 
```python3
from sample_config import Config
 
class Development(Config):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
  TG_BOT_TOKEN_BF_HER = ""
  TG_BOT_USER_NAME_BF_HER = ""
  UB_BLACK_LIST_CHAT = []
  # specify LOAD and NO_LOAD
  LOAD = []
  NO_LOAD = []
```
 
## internals
 
The core features offered by the custom `TelegramClient` live under the
[`uniborg/`](https://github.com/muhammedfurkan/uniborg/tree/master/uniborg)
directory, with some utilities, enhancements, the `_core` plugin, and the `_inline_bot` plugin.
 
## [#LazyAF_Geng](https://t.me/LazyAF_Geng)

We are a OP Telegram Gang. And yes I am the creator of this Gang. If you wanna join the community then message me.

## [Kirito](https://telegram.dog/kirito6969)
 
- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will work without setting the non-mandatory environment variables.
- Please report any issues to the support group: [support group](https://t.me/joinchat/AHAujEjG4FBO-TH-NrVVbg)
 
 
## design
 
The modular design of the project enhances your Telegram experience
through [plugins](https://github.com/SpEcHiDe/uniborg/tree/master/stdplugins)
which you can enable or disable on demand.
 
Each plugin gets the `borg`, `logger`, `Config`, `tgbot` magical
[variables](https://github.com/muhammedfurkan/UniBorg/blob/488eff632e65103ba7017d4f52777d22ddd52ea2/uniborg/uniborg.py#L76-L80)
to ease their use. Thus creating a plugin as easy as adding
a new file under the plugin directory to do the job:

```python
# stdplugins/myplugin.py
from telethon import events
from uniborg.util import admin_cmd
 
@borg.on(admin_cmd(pattern="hi"))
async def handler(event):
    await event.reply("hey")
```
 
 
## learning
 
Check out the already-mentioned [plugins](https://github.com/SpEcHiDe/muhammedfurkan/tree/master/stdplugins) directory, or some third-party [plugins](https://telegram.dog/UniBorg) to learn how to write your own, and consider reading [Telethon's documentation](http://telethon.readthedocs.io/).
 
 
## credits
 
 
Thanks to:
- [lonami](https://lonami.dev) for creating [Telethon](https://github.com/lonamiwebs/Telethon)
