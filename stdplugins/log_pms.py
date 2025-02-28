"""Log PMs
Check https://t.me/tgbeta/3505"""
import asyncio
import logging
import os
import sys
from asyncio import sleep

from telethon import events

from uniborg import SYNTAX
from uniborg.util import admin_cmd

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.WARN
)

NO_PM_LOG_USERS = []

BOTLOG = True
BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID


@borg.on(admin_cmd(outgoing=True, pattern=r"save(?: |$)([\s\S]*)"))
async def log(log_text):
    """For .log command, forwards a message or the command argument to the bot logs group"""
    if BOTLOG:
        if log_text.reply_to_msg_id:
            reply_msg = await log_text.get_reply_message()
            await reply_msg.forward_to(BOTLOG_CHATID)
        elif log_text.pattern_match.group(1):
            user = f"#LOG / Chat ID: {log_text.chat_id}\n\n"
            textx = user + log_text.pattern_match.group(1)
            await bot.send_message(BOTLOG_CHATID, textx)
        else:
            await log_text.edit("`What am I supposed to log?`")
            return
        await log_text.edit("`Logged Successfully`")
    else:
        await log_text.edit("`This feature requires Logging to be enabled!`")
    await sleep(2)
    await log_text.delete()


@borg.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def monito_p_m_s(event):
    sender = await event.get_sender()
    if Config.NO_LOG_P_M_S and not sender.bot:
        chat = await event.get_chat()
        if chat.id not in NO_PM_LOG_USERS and chat.id != borg.uid:
            try:
                if Config.PM_LOGGR_BOT_API_ID and event.message:
                    e = await borg.get_entity(int(Config.PM_LOGGR_BOT_API_ID))
                    fwd_message = await borg.forward_messages(
                        e, event.message, silent=True
                    )
                else:
                    return
            except Exception as e:
                # logger.warn(str(e))
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print(e)


@borg.on(admin_cmd(pattern="log(?: |$)(.*)"))
async def set_no_log_p_m(event):
    if Config.PM_LOGGR_BOT_API_ID is not None:
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private and chat.id in NO_PM_LOG_USERS:
            NO_PM_LOG_USERS.remove(chat.id)
            await event.edit("`Will Log Messages from this Chat`")
            await asyncio.sleep(2)
            await event.delete()


@borg.on(admin_cmd(pattern="nolog(?: |$)(.*)"))
async def set_no_log_p_m(event):
    if Config.PM_LOGGR_BOT_API_ID is not None:
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private and chat.id not in NO_PM_LOG_USERS:
            NO_PM_LOG_USERS.append(chat.id)
            await event.edit("`Won't Log Messages from this chat`")
            await asyncio.sleep(2)
            await event.delete()


SYNTAX.update(
    {
        "log_pms": "`.save` :\
      \nUSAGE: saves taged message in private group .\
      \n\n `.kickme`:\
      \nUSAGE: kicks you from the chat where you used this\
      \n\n`.log`:\
      \nUSAGE:By default will log all private chat messages if you use .nolog and want to log again then you need to use this\
      \n\n`.nolog`:\
      \nUSAGE:to stops logging from a private chat "
    }
)
