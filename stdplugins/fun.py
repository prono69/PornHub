"""COMMAND : .runs , .metoo , .rape , .inkut , .pro , .abuse , .gey"""
import random

from uniborg.util import admin_cmd

METOOSTR = [
    "`Hm`",
    "`Me too thanks`",
    "`Haha yes, me too`",
    "`Same lol`",
    "`Me irl`",
    "`Same here`",
    "`Haha yes`",
    "`Same pinch bsdk`",
]
RUNSREACTS = [
    "`Hm`",
    "`Runs to Thanos`",
    "`Runs to Modiji For Achey Din`",
    "`Runs far, far away from earth`",
    "`Running faster than usian bolt coz I'mma Bot`",
    "`Runs to Marie`",
    "`This Group is too cancerous to deal with.`",
    "`Cya bois`",
    "`I am a mad person. Plox Ban me.`",
    "`I go away`",
    "`I am just walking off, coz me is too fat.`",
    "`I Fugged off!`",
    "`Will run for sax & gurls.`",
    "`Will run for Biriyani.`",
    "`I run because I really like food.`",
    "`Running...because dieting is not an option.`",
    "`Wicked fast runnah`",
    "`If you wanna catch me, you got to be fast...if you wanna stay with me, you got to be good...if you wanna pass me...You've got to be kidding.`",
    "`Anyone can run a hundred meters, it's the next forty-two thousand and two hundred that count.`",
    "`Why are all these people following me?`",
    "`Are the kids still chasing me?`",
    "`Running a marathon...there's an app for that.`",
]
RAPE_STRINGS = [
    "`Bsdk`",
    "`Rape Done Drink The Cum`",
    "`EK baat yaad rkhio, Chut ka Chakkar matlab maut se takkar`",
    "`The user has been successfully raped`",
    "`Dekho Bhaiyya esa hai! Izzat bachailo apni warna Gaand maar lenge tumhari`",
    "`Relax your Rear, ders nothing to fear,The Rape train is finally here`",
    "`Rape coming... Raped! haha 😆`",
    "`Kitni baar Rape krvyega mujhse?`",
    "`Tu Randi hai Sabko pta hai😂`",
    "`Don't rape too much bossdk, else problem....`",
    "`Tu sasti rendi hai Sabko pta hai😂`",
    "`Lodu Andha hai kya Yaha tera rape ho raha hai aur tu abhi tak yahi gaand mara raha hai lulz`",
]
ABUSE_STRINGS = [
    "`Lawde`",
    "`Madharchod`",
    "`Gaandu`",
    "`Chutiya he rah jaye ga`",
    "`Ja be Gaandu`",
    "`Ma ka Bhodsa madharchod`",
    "`You MotherFukcer`",
    "`You Betichod`",
    "`you are lodu no.1`"
    "`Muh Me Lega Bhosdike ?`"
    "`Kro Gandu giri kam nhi toh Gand Maar lenge tumhari hum😂`",
    "`Suno Lodu Jyda muh na chalo be muh me lawda pel Diyaa jayega`",
    "`Sharam aagyi toh aakhe juka lijia land me dam nhi hai apke toh Shilajit kha lijia`",
    "`Kahe Rahiman Kaviraaj C**t Ki Mahima Aisi,L**d Murjha Jaaye Par Ch**t Waisi Ki Waisi`",
    "`Chudakkad Raand Ki Ch**T Mein Pele L*Nd Kabeer, Par Aisa Bhi Kya Choda Ki Ban Gaye Fakeer`",
    "`Taare hai Asmaan me very very bright jaat na jla bskd dekh le apni hight.`",
    "`Zindagi ki na toote lari iski lulli hoti nhi khadi`",
    "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata hai😂.`",
    "`Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.`",
    "`Dil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.`",
    "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya maine is lodu ko randi khane me paya.`",
    "`Mirza galib ki yeh khani hai tu bhosdika hai yeh sab ki jubani hai.`",
    "`Mashoor Rand, Ne Arz Kiya Hai. Aane Wale Aate Hai, Jaane Wale Jaate Hai. Yaade Bas Unki Reh Jaati Hai, Jo G**Nd Sujaa Ke Jaate Hai`",
    "`Pani kam hai matke me gand marlunga jhatke me.`",
    "`Aand kitne bhi bade ho, lund ke niche hi rehte hai`",
    "`Tum Ameer hum gareeb hum jhopdiwale Tum bhosiwale`",
    "`Sisi Bhari Gulab ki padi palang ke pass chodne wale chod gye ab q baitha udaas`",
    "`Phuloo Ka Raja Gulaab Kaato me Rehta hai Jeewan ka Nirmata jaato me rehta hai😂`",
    "`Chude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna`",
    "`Gand mare gandu Chut mare Chutiya Sabse accha mutti 2 mint me chutti😛`",
    "`Marzi Ka Sex Pap Nahi Hota.. Piche Se Dalne Wala Kabhi Baap Nahi Hota.. Condom Zarur Lagana Mere Dost Qki.. Sex K Waqt Popat Ke Pass Dimag Nahi Hota.`",
    "`Uss Ne Hothon Se Chhu Kar Lowd* Pe Nasha Kar Diya; Lu*D Ki Baat To Aur Thi, Uss Ne To Jhato* Ko Bhi Khada Kar Diya!`",
]

GEY_STRINGS = [
    "`Nu Bsdk`",
    "`you gey bsdk`",
    "`you gey`",
    "`you gey in the house`",
    "`you chakka`",
    "`Bhago BC! Chakka aya`",
    "`you gey gey gey gey gey gey gey gey`",
    "`you gey go away`",
]
PRO_STRINGS = [
    "LOL",
    "`This gey is pro as phack.`",
    "`Pros here -_- Time to Leave`",
    "`Proness Lebel: 6969696969`",
    "`Itna pro banda dekhlia bc, ab to marna hoga.`",
    "`U iz pro but i iz ur DAD, KeK`",
    "`What are you Bsdk? Human or Gawd(+_+)`",
    "`Aye pro , ek baat yaad rakhna, Agar Bharosa khud par ho to ksi ki chut tumhari kamzori nahi bnskti.`",
]

INSULT_STRINGS = [
    "Ik right",
    "`Owww ... Such a stupid idiot.`",
    "`BC.. Gaand na fulao, maa chod denge tumhari`",
    "`Don't drink and type.`",
    "`Command not found. Just like your brain.`",
    "`Bot rule 544 section 9 prevents me from replying to stupid humans like you.`",
    "`Sorry, we do not sell brains.`",
    "`Believe me you are not normal.`",
    "`I bet your brain feels as good as new, seeing that you never use it.`",
    "`If I wanted to kill myself I'd climb your ego and jump to your IQ.`",
    "`You didn't evolve from apes, they evolved from you.`",
    "`What language are you speaking? Cause it sounds like bullshit.`",
    "`You are proof that evolution CAN go in reverse.`",
    "`I would ask you how old you are but I know you can't count that high.`",
    "`As an outsider, what do you think of the human race?`",
    "`Ordinarily people live and learn. You just live.`",
    "`Keep talking, someday you'll say something intelligent!.......(I doubt it though)`",
    "`Everyone has the right to be stupid but you are abusing the privilege.`",
    "`I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.`",
    "`You should try tasting cyanide.`",
    "`You should try sleeping forever.`",
    "`Pick up a gun and shoot yourself.`",
    "`Try bathing with Hydrochloric Acid instead of water.`",
    "`Go Green! Stop inhaling Oxygen.`",
    "`God was searching for you. You should leave to meet him.`",
    "`Give your 100%. Now, go donate blood.`",
    "`Try jumping from a hundred story building but you can do it only once.`",
    "`Sharam kar bsdwale,kitni bkchodi deta.`",
    "`Chup Madarhox, bilkul chup..`",
    "`Me zindagi me chunotiyo se jyda inn jese Chutiyo se pareshaan hu.`",
    "`You should donate your brain seeing that you never used it.`",
    "`Volunteer for target in an firing range.`",
    "`Head shots are fun. Get yourself one.`",
    "`You should try swimming with great white sharks.`",
    "`You should paint yourself red and run in a bull marathon.`",
    "`You can stay underwater for the rest of your life without coming back up.`",
    "`How about you stop breathing for like 1 day? That'll be great.`",
    "`Try provoking a tiger while you both are in a cage.`",
    "`Have you tried shooting yourself as high as 100m using a canon.`",
    "`You should try holding TNT in your mouth and igniting it.`",
    "`Try playing catch and throw with RDX its fun.`",
    "`I heard phogine is poisonous but i guess you wont mind inhaling it for fun.`",
    "`Launch yourself into outer space while forgetting oxygen on Earth.`",
    "`You should try playing snake and ladders, with real snakes and no ladders.`",
    "`Dance naked on a couple of HT wires.`",
    "`Active Volcano is the best swimming pool for you.`",
    "`You should try hot bath in a volcano.`",
    "`Try to spend one day in a coffin and it will be yours forever.`",
    "`Hit Uranium with a slow moving neutron in your presence. It will be a worthwhile experience.`",
    "`You can be the first person to step on sun. Have a try.`",
    "`You should Volunteer for target in an firing range.`",
    "`Try playing catch and throw with RDX its fun.`",
    "`People like you are the reason we have middle fingers.`",
    "`Jaana chodu chad jake land chaat`",
    "`Yaar ajab tere nkhare,gazab tera style hain, gand dhone ki tameez nahi, haath main mobile hai`",
    "`When your mom dropped you off at the school, she got a ticket for littering.`",
    "`You’re so ugly that when you cry, the tears roll down the back of your head…just to avoid your face.`",
    "`If you’re talking behind my back then you’re in a perfect position to kiss my a**!.`",
]


@borg.on(admin_cmd(pattern="runs($)"))
async def _(event):
    if event.fwd_from:
        return
    bro = random.randint(0, len(RUNSREACTS) - 1)
    # input_str = event.pattern_match.group(1)
    reply_text = RUNSREACTS[bro]
    await event.edit(reply_text)


@borg.on(admin_cmd(pattern="disable runs", outgoing=True))
async def disable_runs(norun):
    """ Some people don't like running... """
    if not norun.text[0].isalpha() and norun.text[0] not in ("/", "#", "@", "!"):
        global DISABLE_RUN
        DISABLE_RUN = True
        await norun.edit("```Disabled .runs !!```")


@borg.on(admin_cmd(pattern="enable runs", outgoing=True))
async def enable_runs(run):
    """ But some do! """
    if not run.text[0].isalpha() and run.text[0] not in ("/", "#", "@", "!"):
        global DISABLE_RUN
        DISABLE_RUN = False
        await run.edit("```Enabled .runs !!```")


@borg.on(admin_cmd(pattern="metoo($)"))
async def _(event):
    if event.fwd_from:
        return
    bro = random.randint(0, len(METOOSTR) - 1)
    # input_str = event.pattern_match.group(1)
    reply_text = METOOSTR[bro]
    await event.edit(reply_text)


@borg.on(admin_cmd(pattern="rape($)"))
async def _(event):
    if event.fwd_from:
        return
    bro = random.randint(0, len(RAPE_STRINGS) - 1)
    # input_str = event.pattern_match.group(1)
    reply_text = RAPE_STRINGS[bro]
    await event.edit(reply_text)


@borg.on(admin_cmd(pattern="inkut($)"))
async def _(event):
    if event.fwd_from:
        return
    bro = random.randint(0, len(INSULT_STRINGS) - 1)
    # input_str = event.pattern_match.group(1)
    reply_text = INSULT_STRINGS[bro]
    await event.edit(reply_text)


@borg.on(admin_cmd(pattern="pro($)"))
async def _(event):
    if event.fwd_from:
        return
    bro = random.randint(0, len(PRO_STRINGS) - 1)
    # input_str = event.pattern_match.group(1)
    reply_text = PRO_STRINGS[bro]
    await event.edit(reply_text)


@borg.on(admin_cmd(pattern="abuse($)"))
async def _(event):
    if event.fwd_from:
        return
    bro = random.randint(0, len(ABUSE_STRINGS) - 1)
    # input_str = event.pattern_match.group(1)
    reply_text = ABUSE_STRINGS[bro]
    await event.edit(reply_text)


@borg.on(admin_cmd(pattern="gey($)"))
async def _(event):
    if event.fwd_from:
        return
    bro = random.randint(0, len(GEY_STRINGS) - 1)
    event.pattern_match.group(1)
    reply_text = GEY_STRINGS[bro]
    await event.edit(reply_text)
