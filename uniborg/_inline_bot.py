#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
import asyncio
import json
import re
from math import ceil

from telethon import custom, events

from uniborg.util import admin_cmd, humanbytes


@borg.on(admin_cmd(pattern="ib (.[^ ]*) (.*)"))
async def _(event):
    # https://stackoverflow.com/a/35524254/4723940
    if event.fwd_from:
        return
    bot_username = event.pattern_match.group(1)
    search_query = event.pattern_match.group(2)
    try:
        output_message = ""
        bot_results = await event.client.inline_query(bot_username, search_query)
        for i, result in enumerate(bot_results):
            output_message += "{} {} `{}`\n\n".format(
                result.title,
                result.description,
                ".icb " + bot_username + " " + str(i + 1) + " " + search_query,
            )
        await event.edit(output_message)
    except Exception as e:
        await event.edit(
            "{} did not respond correctly, for **{}**!\n\
            `{}`".format(
                bot_username, search_query, str(e)
            )
        )


@borg.on(admin_cmd(pattern="icb (.[^ ]*) (.[^ ]*) (.*)"))
async def _(event):
    if event.fwd_from:
        return
    bot_username = event.pattern_match.group(1)
    i_plus_oneth_result = event.pattern_match.group(2)
    search_query = event.pattern_match.group(3)
    try:
        bot_results = await event.client.inline_query(bot_username, search_query)
        message = await bot_results[int(i_plus_oneth_result) - 1].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )
        await event.delete()
    except Exception as e:
        await event.edit(str(e))


if Config.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.sender_id == borg.uid and query.startswith("@UniBorg "):
            try:
                _, ko, pno = query.split(" ")
                actual_text = borg._iiqsixfourstore[ko][pno]
                del borg._iiqsixfourstore[ko]
            except IndexError:
                actual_text = query
            buttons = paginate_help(0, borg._plugins, "helpme")
            result = builder.article(
                "© @UniBorg",
                text="{}\nCurrently Loaded Plugins: {}".format(
                    actual_text, len(borg._plugins)
                ),
                buttons=buttons,
                link_preview=True,
                parse_mode="html",
            )
        elif query.startswith("tb_btn"):
            result = builder.article(
                "Button Parser © @UniBorg",
                text="powered by @LazyAF_Pepe",
                buttons=[],
                link_preview=True,
                parse_mode="html",
            )
        elif query.startswith("ytdl"):
            # input format should be ytdl URL
            p = re.compile("ytdl (.*)")
            r = p.search(query)
            ytdl_url = r.group(1).strip()
            if ytdl_url.startswith("http"):
                command_to_exec = [
                    "youtube-dl",
                    "--no-warnings",
                    "--youtube-skip-dash-manifest",
                    "-j",
                    ytdl_url,
                ]
                logger.info(command_to_exec)
                process = await asyncio.create_subprocess_exec(
                    *command_to_exec,
                    # stdout must a pipe to be accessible as process.stdout
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                )
                # Wait for the subprocess to finish
                stdout, stderr = await process.communicate()
                e_response = stderr.decode().strip()
                # logger.info(e_response)
                t_response = stdout.decode().strip()
                logger.info(command_to_exec)
                if e_response:
                    error_message = e_response.replace(
                        "please report this issue on https://yt-dl.org/bug . Make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. Be sure to call youtube-dl with the --verbose flag and include its complete output.",
                        "",
                    )
                    # throw error
                    result = builder.article(
                        "YTDL Errors © @UniBorg",
                        text=f"{error_message} Powered by @LazyAF_Pepe",
                        link_preview=False,
                    )
                elif t_response:
                    x_reponse = t_response
                    if "\n" in x_reponse:
                        x_reponse, _ = x_reponse.split("\n")
                    response_json = json.loads(x_reponse)
                    save_ytdl_json_path = (
                        Config.TMP_DOWNLOAD_DIRECTORY + "/" + "YouTubeDL" + ".json"
                    )
                    with open(save_ytdl_json_path, "w", encoding="utf8") as outfile:
                        json.dump(response_json, outfile, ensure_ascii=False)
                    # logger.info(response_json)
                    inline_keyboard = []
                    duration = None
                    if "duration" in response_json:
                        duration = response_json["duration"]
                    if "formats" in response_json:
                        for formats in response_json["formats"]:
                            format_id = formats.get("format_id")
                            format_string = formats.get("format_note")
                            if format_string is None:
                                format_string = formats.get("format")
                            format_ext = formats.get("ext")
                            approx_file_size = ""
                            if "filesize" in formats:
                                approx_file_size = humanbytes(formats["filesize"])
                            cb_string_video = "ytdl|{}|{}|{}".format(
                                "video", format_id, format_ext
                            )
                            if format_string is not None:
                                ikeyboard = [
                                    custom.Button.inline(
                                        " "
                                        + format_ext
                                        + " video ["
                                        + format_string
                                        + "] ( "
                                        + approx_file_size
                                        + " )",
                                        data=(cb_string_video),
                                    )
                                ]
                            else:
                                # special weird case :\
                                ikeyboard = [
                                    custom.Button.inline(
                                        " " + approx_file_size + " ",
                                        data=cb_string_video,
                                    )
                                ]
                            inline_keyboard.append(ikeyboard)
                        if duration is not None:
                            cb_string_64 = "ytdl|{}|{}|{}".format("audio", "64k", "mp3")
                            cb_string_128 = "ytdl|{}|{}|{}".format(
                                "audio", "128k", "mp3"
                            )
                            cb_string = "ytdl|{}|{}|{}".format("audio", "320k", "mp3")
                            inline_keyboard.append(
                                [
                                    custom.Button.inline(
                                        "MP3 " + "(" + "64 kbps" + ")",
                                        data=cb_string_64,
                                    ),
                                    custom.Button.inline(
                                        "MP3 " + "(" + "128 kbps" + ")",
                                        data=cb_string_128,
                                    ),
                                ]
                            )
                            inline_keyboard.append(
                                [
                                    custom.Button.inline(
                                        "MP3 " + "(" + "320 kbps" + ")", data=cb_string
                                    )
                                ]
                            )
                    else:
                        format_id = response_json["format_id"]
                        format_ext = response_json["ext"]
                        cb_string_video = "ytdl|{}|{}|{}".format(
                            "video", format_id, format_ext
                        )
                        inline_keyboard.append(
                            [custom.Button.inline("video", data=cb_string_video)]
                        )
                    result = builder.article(
                        "YouTube © @UniBorg",
                        text=f"{ytdl_url} powered by @LazyAF_Pepe",
                        buttons=inline_keyboard,
                        link_preview=True,
                    )
        else:
            result = builder.article(
                "© @UniBorg",
                text="""@PepeB0t **( Custom Built By** @kirito6969 **)
**Verified Account:** ✅
**Official Website:** https://prono69.github.io/PepeBot/

**Pithun 3.8.5 (default, Apr 29 2020, 09:19:52)**
**[GCC 7.4.0]**
**Talethrun 1.15.0**

**Custom Built Fork:** https://github.com/prono69/PepeBot""",
                buttons=[
                    [
                        custom.Button.url(
                            "👤Contact Creator👤", "https://telegram.dog/kirito6969"
                        ),
                        custom.Button.url(
                            "📼Ravana Audio Memes📼", "https://t.me/tgaudiomemes"
                        ),
                    ],
                    [
                        custom.Button.url(
                            "👨‍💻Source Code👨‍💻", "https://github.com/prono69/PepeBot"
                        ),
                        custom.Button.url(
                            "❕❗Deploy Me❗❕",
                            "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fravana69%2FPornHub%2F&template=https%3A%2F%2Fgithub.com%2Fravana69%2FPornHub%2F",
                        ),
                    ],
                    [
                        custom.Button.url(
                            "🔰Update Fork🔰", "tg://need_update_for_some_feature"
                        ),
                        custom.Button.url(
                            "✳️Fork Boost✳️", "tg://some_unsupported_feature"
                        ),
                        custom.Button.url("♻️Refresh Heroku♻️", "tg://chutiya"),
                    ],
                ],
                link_preview=True,
            )
        await event.answer([result] if result else None)

    @tgbot.on(
        events.callbackquery.CallbackQuery(data=re.compile(rb"helpme_next\((.+?)\)"))
    )
    async def on_plug_in_callback_query_handler(event):
        if event.sender_id == borg.uid:
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, borg._plugins, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "⚠️ Warning: Don't Press Any Buttons ⚠️\n\n\nNote: Bas kar BetiChod, Maa Ke Laude, Madarchod"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(data=re.compile(rb"helpme_prev\((.+?)\)"))
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == borg.uid:
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number - 1, borg._plugins, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = (
                "Please get your own @PepeBot. Don't edit my messages plox!"
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ub_plugin_(.*)")))
    async def on_plug_in_callback_query_handler(event):
        plugin_name = event.data_match.group(1).decode("UTF-8")
        try:
            help_string = borg._plugins[plugin_name].__doc__[
                0:125
            ]  # pylint:disable=E0602
        except (ValueError, TypeError):
            help_string = None
        reply_pop_up_alert = (
            help_string
            if help_string is not None
            else "No DOCSTRING has been setup for {} plugin".format(plugin_name)
        )
        reply_pop_up_alert += "\n\n Use .unload {} to remove this plugin\n\n\
            © @LazyAF_Pepe".format(
            plugin_name
        )
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = Config.NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD
    number_of_cols = 2
    helpable_plugins = [p for p in loaded_plugins if not p.startswith("_")]
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        custom.Button.inline("{} {}".format("🐈", x), data="ub_plugin_{}".format(x))
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⏮️ Previous", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "⏭️ Next", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs
