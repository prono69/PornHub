# Inspired by Saitama Bot, credits - @kirito6969, @PhycoNinja13b
# Thx to @DeletedUser420


from telethon import events

from uniborg import MODULE, SYNTAX
from userbot import fonts as op

MODULE.append("weebify")


@borg.on(events.NewMessage(pattern="^.weeb(?: |$)(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = " ".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in op.normiefont:
            weebycharacter = op.weebyfont[op.normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)


boldfont = [
    "𝗮",
    "𝗯",
    "𝗰",
    "𝗱",
    "𝗲",
    "𝗳",
    "𝗴",
    "𝗵",
    "𝗶",
    "𝗷",
    "𝗸",
    "𝗹",
    "𝗺",
    "𝗻",
    "𝗼",
    "𝗽",
    "𝗾",
    "𝗿",
    "𝘀",
    "𝘁",
    "𝘂",
    "𝘃",
    "𝘄",
    "𝘅",
    "𝘆",
    "𝘇",
]


@borg.on(events.NewMessage(pattern="^.bold(?: |$)(.*)"))
async def thicc(bolded):

    args = bolded.pattern_match.group(1)
    if not args:
        get = await bolded.get_reply_message()
        args = get.text
    if not args:
        await bolded.edit("`What I am Supposed to bold for U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            boldcharacter = boldfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, boldcharacter)
    await bolded.edit(string)


medievalbold = [
    "𝖆",
    "𝖇",
    "𝖈",
    "𝖉",
    "𝖊",
    "𝖋",
    "𝖌",
    "𝖍",
    "𝖎",
    "𝖏",
    "𝖐",
    "𝖑",
    "𝖒",
    "𝖓",
    "𝖔",
    "𝖕",
    "𝖖",
    "𝖗",
    "𝖘",
    "𝖙",
    "𝖚",
    "𝖛",
    "𝖜",
    "𝖝",
    "𝖞",
    "𝖟",
]


@borg.on(events.NewMessage(pattern="^.medibold(?: |$)(.*)"))
async def mediv(medievalx):

    args = medievalx.pattern_match.group(1)
    if not args:
        get = await medievalx.get_reply_message()
        args = get.text
    if not args:
        await medievalx.edit("`What I am Supposed to medieval bold for U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            medievalcharacter = medievalbold[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, medievalcharacter)
    await medievalx.edit(string)


doublestruckt = [
    "𝕒",
    "𝕓",
    "𝕔",
    "𝕕",
    "𝕖",
    "𝕗",
    "𝕘",
    "𝕙",
    "𝕚",
    "𝕛",
    "𝕜",
    "𝕝",
    "𝕞",
    "𝕟",
    "𝕠",
    "𝕡",
    "𝕢",
    "𝕣",
    "𝕤",
    "𝕥",
    "𝕦",
    "𝕧",
    "𝕨",
    "𝕩",
    "𝕪",
    "𝕫",
]


@borg.on(events.NewMessage(pattern="^.ds(?: |$)(.*)"))
async def doublex(doublestrucktx):

    args = doublestrucktx.pattern_match.group(1)
    if not args:
        get = await doublestrucktx.get_reply_message()
        args = get.text
    if not args:
        await doublestrucktx.edit("`What I am Supposed to double struck for U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            strucktcharacter = doublestruckt[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, strucktcharacter)
    await doublestrucktx.edit(string)


cursiveboldx = [
    "𝓪",
    "𝓫",
    "𝓬",
    "𝓭",
    "𝓮",
    "𝓯",
    "𝓰",
    "𝓱",
    "𝓲",
    "𝓳",
    "𝓴",
    "𝓵",
    "𝓶",
    "𝓷",
    "𝓸",
    "𝓹",
    "𝓺",
    "𝓻",
    "𝓼",
    "𝓽",
    "𝓾",
    "𝓿",
    "𝔀",
    "𝔁",
    "𝔂",
    "𝔃",
]


@borg.on(events.NewMessage(pattern="^.curb(?: |$)(.*)"))
async def cursive2(cursivebolded):

    args = cursivebolded.pattern_match.group(1)
    if not args:
        get = await cursivebolded.get_reply_message()
        args = get.text
    if not args:
        await cursivebolded.edit("`What I am Supposed to cursive bold for U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            cursiveboldcharacter = cursiveboldx[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, cursiveboldcharacter)
    await cursivebolded.edit(string)


medival2 = [
    "𝔞",
    "𝔟",
    "𝔠",
    "𝔡",
    "𝔢",
    "𝔣",
    "𝔤",
    "𝔥",
    "𝔦",
    "𝔧",
    "𝔨",
    "𝔩",
    "𝔪",
    "𝔫",
    "𝔬",
    "𝔭",
    "𝔮",
    "𝔯",
    "𝔰",
    "𝔱",
    "𝔲",
    "𝔳",
    "𝔴",
    "𝔵",
    "𝔶",
    "𝔷",
]


@borg.on(events.NewMessage(pattern="^.medi(?: |$)(.*)"))
async def medival22(medivallite):

    args = medivallite.pattern_match.group(1)
    if not args:
        get = await medivallite.get_reply_message()
        args = get.text
    if not args:
        await medivallite.edit("`What I am Supposed to medival for U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            medivalxxcharacter = medival2[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, medivalxxcharacter)
    await medivallite.edit(string)


cursive = [
    "𝒶",
    "𝒷",
    "𝒸",
    "𝒹",
    "𝑒",
    "𝒻",
    "𝑔",
    "𝒽",
    "𝒾",
    "𝒿",
    "𝓀",
    "𝓁",
    "𝓂",
    "𝓃",
    "𝑜",
    "𝓅",
    "𝓆",
    "𝓇",
    "𝓈",
    "𝓉",
    "𝓊",
    "𝓋",
    "𝓌",
    "𝓍",
    "𝓎",
    "𝓏",
]


@borg.on(events.NewMessage(pattern="^.cur(?: |$)(.*)"))
async def xcursive(cursivelite):

    args = cursivelite.pattern_match.group(1)
    if not args:
        get = await cursivelite.get_reply_message()
        args = get.text
    if not args:
        await cursivelite.edit("`What I am Supposed to cursive for U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            cursivecharacter = cursive[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, cursivecharacter)
    await cursivelite.edit(string)


musicalfont = [
    "♬",
    "ᖲ",
    "¢",
    "ᖱ",
    "៩",
    "⨏",
    "❡",
    "Ϧ",
    "ɨ",
    "ɉ",
    "ƙ",
    "ɭ",
    "៣",
    "⩎",
    "០",
    "ᖰ",
    "ᖳ",
    "Ʀ",
    "ន",
    "Ƭ",
    "⩏",
    "⩔",
    "Ɯ",
    "✗",
    "ƴ",
    "Ȥ",
]


@borg.on(events.NewMessage(pattern="^.musi(?: |$)(.*)"))
async def xmusical(musical):

    args = musical.pattern_match.group(1)
    if not args:
        get = await musical.get_reply_message()
        args = get.text
    if not args:
        await musical.edit("`What I am Supposed to musicify for U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            musicalstyle = musicalfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, musicalstyle)
    await musical.edit(string)


SYNTAX.update(
    {
        "weebify": "Usage: Good Fonts\
\n\n`.weeb` Weebify a text\
\n\n`.cur` make text cursive.\
\n\n`.curb` make text cursive bold.\
\n\n`.medi` make text medival.\
\n\n`.medib` make text medival bold.\
\n\n`.ds` make text doublestruck.\
\n\n`.bold` make text bold.\
\n\n`.musi` make text musical."
    }
)
