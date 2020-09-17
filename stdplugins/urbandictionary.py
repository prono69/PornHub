# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Urban Dictionary
Syntax: .ud Query"""
import urbandict

from uniborg.util import admin_cmd, edit_or_reply


@borg.on(admin_cmd(pattern="ud (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    hmm = await edit_or_reply(event, "Searching...🔎")
    query = event.pattern_match.group(1)
    if not query:
        get = await event.get_reply_message()
        query = get.text

    if not query and not event.reply_to_msg_id:
        await hmm.edit("`Gibe some keywords Nigga`")
        return

    try:
        mean = urbandict.define(query)

    except BaseException:
        await hmm.edit(
            text=f"Sorry, couldn't find any results fer: `{query}``\nSed vary sed \n**TIP**: \n`Now head towerd Googal u nibba`"
        )
        return

    output = ""
    for i, mean_ in enumerate(mean, start=1):
        output += (
            f"{i}- **{mean_['def']}**\n"
            + f" Examples:\n » `{mean_['example'] or 'not found'}`\n\n"
        )
        if i == 8:
            break

    if not output:
        await hmm.edit(text=f"No result found for **{query}**")
        return

    output = f"**Query Text:** `{query}`\n\n{output}\n**Source:** __Urban Dictionary__"

    await hmm.edit(output)
