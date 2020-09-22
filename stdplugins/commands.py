"""to get command's list type .cl"""

import asyncio

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "cl":

        await event.edit(input_str)

        animation_chars = [
            "https://telegra.ph/command-list-for-BotHub-Userbot-11-08",
            "https://github.com/ravana69/UniBorg",
            "https://github.com/spechide/UniBorg",
        ]

        animation_interval = 0.8

        animation_ttl = range(1)

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 3])


"""https://telegra.ph/command-list-for-BotHub-Userbot-11-08


.helpme
.stdplugins
.3Cube
.bothub
.armor
.love
.hero
.earth
.fexit
.ft
.f
.kill
.mayur
.web
.pbic
.ppic
.pname
.ae
.afk
.all
.anime
.setflood
.apk
.apkr
.magnet
.tor
.url
.show
.ariaRM
.ariastart
.addmagnet magnetLink
.addtorrent file_path
.showariastatus
.ariaRES
.ariaP
.autoname
.autobio
.autopp
.bar
.upb
.BBL
.belo
.addblacklist
.listblacklist
.rmblacklist
.bomb
.leave
.calendar YYYY-MM-DD
./calling
.admin
.carbon
.chain
.isro
.geta
.getc
.sclock
.clock animation
.cname
.code
.coinflip
.color
.cd
.scd
.padmin
.cowsay
.defaultsay
.wwwsay
.kisssay
.tuxsay
.bunnysay
.moosesay
.sheepsay
.rensay
.cheesesay
.ghostbusterssay
.skeletonsay
[manythings will say soon]

.create (b|g)
.cry
.currency <source> <destination>
.dns
.link
.unshort
.myip
.myisp
.myhead
.mywho
.myup
.decide
.deepfry
.deploy
.join
.pay
.work
.push
.aag
.climb
.meaning <word>
.ding
.dir
.download url filename.extension
.ddg search quiry
.dump
.dump all
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-
.eval pythoncode
.exec code
.cpu
.uptime
.suicide
.env
.pip
.neofetch
.date
.coffeehouse
.telegram
.stdplugins
.fast,
.listpip
.fuggi
.eye
.url
.fsave
.ftrim
.fgdrive
.figlet
.nfc
.filext
.lsroot
.lslocal
.vadapanv
.savefilter
.listfilters
.clearfilter
.fix
.fleave
.floodwarn
.fpost word
.runs
.metoo
.pro
.oo
.gban
.ungban
.gdl file-link
.gdrive
.sdrive
.gdir
.dfolder
.drive delete | get
.gclear
.g_admin
.g_bot
.g_id
.gift
.gts
.guthub
.github username
.commit
.glink
.gs query
.gi query
.grs
.gotm
.hack
.heroku
.hypno
.ifsc rp [ifsc code]
.img [name]
.song [song keyword]
.invite
.max
.malove
.madog
.maconfused
.mathinking
.mawaving
.masad
.madead
.ma h
.jio
.json
.copi
.packinfo
.ZIP
.Karaniya
.karbon1
.karbon2
.karbon3
.karbon4
.karbon5
.kbass_* [plugins]
.labstack
.fleave
.leave
.lmg search query
.lmy search query
.ddg search query
.lmalt search news
.lmvar heroku app name
.lmlog heroku app name
.dyno type billing
.ducduckgo
.load
.square
.up
.round
.heart
.anim
.locks
.lock
.unlock
.lol
.eai
.dai
.lai
.meme
.✋🏻
.men
.smoon
.tmoon
.moon
.nccreatedch
.nolog
.dellog
.apm
.blockpm
.lapms
.ocr [langcode]
.on
.OS
.Macos
.Windows
.Linux
.Stock
.owner
.padmin
.paste
.cpin [LOUD]
.ping
.pingme
.pong
.install
.police
.get_poll
.restart
.shutdown
.fastboot
.reboot
.asciiboot
.p
.ppg @username
.premote
.demote
.prankpremote
.demote
.purge
.getqr reply msg
.makeqr <long text to include>
.quickheal
.sqh
.vquickheal
.dab
.brain
.rl <link>
.react happy/thinking/waving/love/confused/dead/sad/dog
.remove.bg
.rnupload filename.extension
.rnstreamupload filename.extension
.rndlup
.repeat <#> <text>
.sca <option> <time in sec>
.scaoptions
.schd <time in seconds> <message to send>
.screencapture <website url>
.screenlong <website url>
.img <name>
.shout messege
.shoot <reply to the message>
.admem to shout admin
.spem
.slap
.snips
.snipl
.snipd
.snow
.solar
.sch <search query>
.tspam <text>
.speedtest image/file/text
.stat to know your user status
.stt
.switch
.neofetch
.sysd
.telegraph media as reply
.telegraph text as reply to a large text
.test
.think
.savethumbnail
.clearthumbnail
.getthumbnail
.time
.timepass
.movie torrentz2.eu / idop.se
.search search_string
.otransfer @username
.tr language code as reply/ text to translate
.tts LanguageCode as reply to a message
.tts LangaugeCode | text to speak
.ban
.unban
.mute
.repo
.unzip
.upload <Path To File>
.uploaddir <Path To Directory>
.uploadasstream <Path To File>
.mirrorace
.ud <query>
.userlist
.verystream
.virus
.warn0 / 1 / 2 / 3
.gbun
.fw
.ocb
.weather location
.wttr location
.clearwelcome
.savewelcome
.whatscrapp
.who to know the name username and id of the chat
.info @username
.wikimedia query
.wiki
.wchar
.wupload
.xkcd <search>
.compress
.izal
.df @username
.sg @username
.unbanall

.kick option
Available Options: d, y, m, w, o, q, r, p
p - reserved for channel
e - usercount
y - userstatusempty
m - userstatuslastmonth
w - userstatuslastweek
o - userstatusoffline
q - userstatusonline
r - userstatusrecently
b - bot
d - deleted account

--------------------------------------
.vapor
.cp
.str
.hi
.owo
.10iq
.roon
.mock
.clap
.bt
"""
