# For UniBorg
# By Priyam Kalra
# Based on the note module made by RaphielGang (https://da.gd/X4Mnf)

"""Syntax:
`.seb <notename>
.get <notename>
.clear <notename>
.cleanall
.rmbotnotes`
"""

import time

from sql_helpers.global_variables_sql import LOGGER
from sql_helpers.notes_sql import add_note, get_notes, rm_all_notes, rm_note
from uniborg import MODULE, SYNTAX
from uniborg.util import admin_cmd

MODULE.append("notes")


@borg.on(admin_cmd(pattern="notes ?(.*)"))
async def _(svd):
    if svd.fwd_from:
        return
    notes = get_notes(svd.chat_id)
    message = "```There are no saved notes in this chat.```"
    if notes:
        message = "**Notes saved in this chat:** \n\n"
        for note in notes:
            message = message + "🔸 " + note.keyword + "\n"
    await svd.edit(message)


@borg.on(admin_cmd(pattern="clear ?(.*)"))
async def _(clr):
    if clr.fwd_from:
        return
    notes = get_notes(clr.chat_id)
    notelist = ""
    for note in notes:
        notelist = note.keyword
    notename = clr.pattern_match.group(1)
    status = f"**Note {notename} not found.**"
    if notename in notelist:
        rm_note(clr.chat_id, notename)
        status = f"**Note** ```{notename}``` **cleared successfully**"
    await clr.edit(status)


@borg.on(admin_cmd(pattern="seb ?(.*)"))
async def _(fltr):
    if fltr.fwd_from:
        return
    notename = fltr.pattern_match.group(1)
    rep_msg = await fltr.get_reply_message()
    if rep_msg and notename:
        string = rep_msg.text
        add_note(str(fltr.chat_id), notename, string)
        message = f"**Note saved successfully.**\n**Use** ```.get {notename}``` **to get it.**"
    else:
        message = "**Error!**\nPlease use carefully or ```Reply to a user message.```\n**You little piece of Shit!**"
    await fltr.edit(message)


@borg.on(admin_cmd(pattern="get ?(.*)"))
async def _(getnt):
    if getnt.fwd_from:
        return
    notename = getnt.pattern_match.group(1)
    notes = get_notes(getnt.chat_id)
    for note in notes:
        if notename == note.keyword:
            await getnt.reply(note.reply)
            await getnt.delete()
        else:
            await getnt.edit(f"**Note** ```{notename}``` **not found!**")


@borg.on(admin_cmd(pattern="cleanall ?(.*)"))
async def _(prg):
    if prg.fwd_from:
        return
    if not prg.text[0].isalpha():
        await prg.edit("```Purging all notes.```")
        await prg.edit(
            "**All notes have been purged successfully.**\n```This auto generated message will be deleted in a few seconds...```"
        )
        rm_all_notes(str(prg.chat_id))
        time.sleep(5)
        await prg.delete()
        if LOGGER:
            await borg.send_message(
                LOGGER, f"**Successfully purged all notes at** ```{prg.chat_id}```"
            )


@borg.on(admin_cmd(pattern="rmbotnotes ?(.*)"))
async def kick_marie_notes(kick):
    if kick.is_private:
        await event.edit("`You cant do that in DMs`")
        return
    if LOGGER:
        await kick.client.send_message(
            LOGGER, "I cleaned all Notes at " + str(kick.chat_id)
        )


SYNTAX.update(
    {
        "notes": "\
```.get <notename>```\
\nUsage: Gets the note with name <notename>\
\n\n```.seb <notename>``` (as a reply to message to save)\
\nUsage: Saves target message as a note with the name <notename>\
\n\n```.clear <notename>```\
\nUsage: Deletes the note with name <notename>.\
\n\n```.notes <notename>```\
\nUsage: Prints the list of notes saved in the current chat.\
\n\n```.cleanall```\
\nUsage: Clear all notes at Once.\
\n\n```.rmbotnotes```\
\nUsage: Clear Marie and Rose Bot notes"
    }
)
