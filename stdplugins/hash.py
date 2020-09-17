# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing hash and encode/decode commands.
\nPorted By- [NIKITA](https://t.me/kirito6969) #LazyAF_Geng 🔥
"""

from subprocess import PIPE
from subprocess import run as runapp

import pybase64

from uniborg import MODULE, SYNTAX
from uniborg.util import admin_cmd

MODULE.append("hash")


@borg.on(admin_cmd(pattern="hash ?(.*)"))
async def gethash(hash_q):
    """ For .hash command, find the md5, sha1, sha256, sha512 of the string. """
    hashtxt_ = hash_q.pattern_match.group(1)
    if not hashtxt_:
        get = await hash_q.get_reply_message()
        hashtxt_ = get.text
    else:
        await hash_q.edit("Brah.. Gib me Something")
        return

    hashtxt = open("hashdis.txt", "w+")
    hashtxt.write(hashtxt_)
    hashtxt.close()
    md5 = runapp(["md5sum", "hashdis.txt"], stdout=PIPE)
    md5 = md5.stdout.decode()
    sha1 = runapp(["sha1sum", "hashdis.txt"], stdout=PIPE)
    sha1 = sha1.stdout.decode()
    sha256 = runapp(["sha256sum", "hashdis.txt"], stdout=PIPE)
    sha256 = sha256.stdout.decode()
    sha512 = runapp(["sha512sum", "hashdis.txt"], stdout=PIPE)
    runapp(["rm", "hashdis.txt"], stdout=PIPE)
    sha512 = sha512.stdout.decode()
    ans = (
        "Text: `"
        + hashtxt_
        + "`\nMD5: `"
        + md5
        + "`SHA1: `"
        + sha1
        + "`SHA256: `"
        + sha256
        + "`SHA512: `"
        + sha512[:-1]
        + "`"
    )
    if len(ans) > 4096:
        hashfile = open("hashes.txt", "w+")
        hashfile.write(ans)
        hashfile.close()
        await hash_q.client.send_file(
            hash_q.chat_id,
            "hashes.txt",
            reply_to=hash_q.id,
            caption="`It's too big, sending a text file instead. `",
        )
        runapp(["rm", "hashes.txt"], stdout=PIPE)
    else:
        await hash_q.reply(ans)


@borg.on(admin_cmd(pattern="base (en|de) ?(.*)"))
async def endecrypt(query):
    """ For .base64 command, find the base64 encoding of the given string. """
    input_str = query.pattern_match.group(2)
    if not input_str:
        get = await query.get_reply_message()
        input_str = get.text
    else:
        await query.edit("Uffff.. Sar Gib me something")
        return
    if query.pattern_match.group(1) == "en":
        lething = str(pybase64.b64encode(bytes(input_str, "utf-8")))[2:]
        await query.reply("Encoded: `" + lething[:-1] + "`")
    else:
        lething = str(pybase64.b64decode(bytes(input_str, "utf-8"), validate=True))[2:]
        await query.reply("Decoded: `" + lething[:-1] + "`")


SYNTAX.update(
    {
        "hash": "`.base <en or de>`\
    \n`Usage: Find the base64 encoding of the given string.`\
    \n\n`.hash`\
    \n`Usage: Find the md5, sha1, sha256, sha512 of the string when written into a txt file.`"
    }
)
