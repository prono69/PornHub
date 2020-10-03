"""For .cowsay module, PepeBot wrapper for cow which says things.
    **⚠️🔞 NSFW WARNING**
   +++++CREDIT+++++++
   Code : @NeoMatrix90
   **Ported by @NeoMatrix90 (Ultra Legend)**
   Syntax : .cowsay {text} (cow will say dirty things. BE AWARE)
   		 .milksay {text} (A milk guy who hates cow)
   		 .tuxsay {text} (Find Out yourself)
   		 and many more, find out yourself, I iz Nub.

   ***#Curse WHOEVER Change this, is a Gay and will be a Motherfucker, and cannot able to produce children. And he/she is a Bhosdiwala***
         ***🔴 DON'T COPY WITHOUT CREDIT***
         """

from cowpy import cow

from uniborg.util import admin_cmd, edit_or_reply


@borg.on(admin_cmd(pattern=r"^.(\w+)say (.*)", allow_sudo=True))
async def univsaye(event):
    """ For .cowsay module, uniborg wrapper for cow which says things. """
    if event.text[0].isalpha() or event.text[0] in ("/", "#", "@", "!"):
        return

    arg = event.pattern_match.group(1).lower()
    text = event.pattern_match.group(2)

    if arg == "cow":
        arg = "default"
    if arg not in cow.COWACTERS:
        return await edit_or_reply(event, "`This Character is not Supported`")
    cheese = cow.get_cow(arg)
    cheese = cheese()

    await edit_or_reply(event, f"`{cheese.milk(text).replace('`', '´')}`")
