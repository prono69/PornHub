# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import asyncio
import importlib.util
import logging
import os
import time
from pathlib import Path

import telethon.events
import telethon.utils
from pymongo import MongoClient
from telethon import TelegramClient


class ReverseList(list):
    def __iter__(self):
        return reversed(self)


class Uniborg(TelegramClient):
    def __init__(
        self,
        session,
        *,
        n_plugin_path="plugins",
        db_plugin_path="plugins",
        bot_token=None,
        api_config=None,
        **kwargs,
    ):
        self._name = "LoggedIn"
        self._logger = logging.getLogger("PepeBot")
        self._plugins = {}
        self._iiqsixfourstore = {}
        self.n_plugin_path = n_plugin_path
        self.db_plugin_path = db_plugin_path
        self.config = api_config
        self.mongo = MongoClient(os.environ.get("MONGO_URI", None))

        kwargs = {
            "api_id": 6,
            "api_hash": "eb06d4abfb49dc3eeb1aeb98ae0f581e",
            "device_model": "Kali Linux nonUI",
            "app_version": "@PepeBot 7.0",
            "lang_code": "en",
            **kwargs,
        }

        self.tgbot = None
        if api_config.TG_BOT_USER_NAME_BF_HER is not None:
            self._logger.info("Initiating Inline Bot")
            # ForTheGreatrerGood of beautification
            self.tgbot = TelegramClient(
                "TG_BOT_TOKEN", api_id=api_config.APP_ID, api_hash=api_config.API_HASH
            ).start(bot_token=api_config.TG_BOT_TOKEN_BF_HER)
            self._logger.info("Initialisation finished with no errors")

        super().__init__(session, **kwargs)

        # This is a hack, please avert your eyes
        # We want this in order for the most recently added handler to take
        # precedence
        self._event_builders = ReverseList()

        self.loop.run_until_complete(self._async_init(bot_token=bot_token))

        core_plugin = Path(__file__).parent / "_core.py"
        self.load_plugin_from_file(core_plugin)

        inline_bot_plugin = Path(__file__).parent / "_inline_bot.py"
        self.load_plugin_from_file(inline_bot_plugin)

        for a_plugin_path in Path().glob(f"{self.n_plugin_path}/*.py"):
            self.load_plugin_from_file(a_plugin_path)

        if api_config.DB_URI is not None:
            for a_plugin_path in Path().glob(f"{self.db_plugin_path}/*.py"):
                self.load_plugin_from_file(a_plugin_path)

        LOAD = self.config.LOAD
        NO_LOAD = self.config.NO_LOAD
        if LOAD or NO_LOAD:
            to_load = LOAD
            if to_load:
                self._logger.info("Modules to LOAD: ")
                self._logger.info(to_load)
        if NO_LOAD:
            for plugin_name in NO_LOAD:
                if plugin_name in self._plugins:
                    self.remove_plugin(plugin_name)

    async def _async_init(self, **kwargs):
        await self.start(**kwargs)

        self.me = await self.get_me()
        self.uid = telethon.utils.get_peer_id(self.me)

        self._logger.info(
            f"Logged in as {self.uid} "
            f"Try {self.config.COMMAND_HAND_LER}info in any chat..!"
        )

    def load_plugin(self, shortname):
        self.load_plugin_from_file(f"{self.n_plugin_path}/{shortname}.py")

    def load_plugin_from_file(self, path):
        path = Path(path)
        shortname = path.stem
        name = f"{self._name}.{shortname}"

        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.mongo_client = self.mongo

        mod.borg = self
        mod.bot = self
        mod.logger = logging.getLogger(shortname)
        # declare Config and tgbot to be accessible by all modules
        mod.Config = self.config
        if self.config.TG_BOT_USER_NAME_BF_HER is not None:
            mod.tgbot = self.tgbot
        mod.BOT_START_TIME = time.time()

        spec.loader.exec_module(mod)
        self._plugins[shortname] = mod
        self._logger.info(f"Successfully loaded plugin {shortname}")

    def remove_plugin(self, shortname):
        name = self._plugins[shortname].__name__

        for i in reversed(range(len(self._event_builders))):
            ev, cb = self._event_builders[i]
            if cb.__module__ == name:
                del self._event_builders[i]

        del self._plugins[shortname]
        self._logger.info(f"Removed plugin {shortname}")
        self._logger.info("Userbot Startup Completed")

    def await_event(self, event_matcher, filter=None):
        fut = asyncio.Future()

        @self.on(event_matcher)
        async def cb(event):
            try:
                if filter is None or await filter(event):
                    fut.set_result(event)
            except telethon.events.StopPropagation:
                fut.set_result(event)
                raise

        fut.add_done_callback(lambda _: self.remove_event_handler(cb, event_matcher))

        return fut
