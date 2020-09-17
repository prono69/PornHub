import asyncio
import re

from uniborg import MODULE, SYNTAX
from uniborg.util import admin_cmd
from userbot import AioHttp

MODULE.append("animals")

animal = r"([^.]*)$"
ok_exts = ["jpg", "jpeg", "png"]

animals_data = {
    "dog": {"url": "https://random.dog/woof.json", "key": "url"},
    "cat": {"url": "http://aws.random.cat/meow", "key": "file"},
    "panda": {"url": "https://some-random-api.ml/img/panda", "key": "link"},
    "redpanda": {"url": "https://some-random-api.ml/img/red_panda", "key": "link"},
    "bird": {"url": "https://some-random-api.ml/img/birb", "key": "link"},
    "fox": {"url": "https://some-random-api.ml/img/fox", "key": "link"},
    "koala": {"url": "https://some-random-api.ml/img/koala", "key": "link"},
}

animals = [x for x in animals_data]


async def prep_animal_image(animal_data):
    ext = ""
    image = None
    while ext not in ok_exts:
        data = await AioHttp().get_json(animal_data["url"])
        image = data[animal_data["key"]]
        ext = re.search(animal, image).group(1).lower()
    return image


@borg.on(admin_cmd(pattern="animal ?(.*)"))
async def animal_image(message):
    lol = message.pattern_match.group(1)
    if not lol:
        await message.edit("`Are you really a Human ?`")
        return

    animal_data = animals_data[lol]
    await message.delete()
    await message.client.send_file(
        message.chat_id,
        file=await prep_animal_image(animal_data),
        reply_to_id=message.reply_to_msg_id,
    )


@borg.on(admin_cmd(pattern="afact ?(.*)"))
async def fact(message):
    cmd = message.pattern_match.group(1)
    if not cmd:
        await message.edit("```Not enough params provided```")
        await asyncio.sleep(3)
        await message.delete()
        return

    await message.edit(f"```Getting {cmd} fact```")
    link = "https://some-random-api.ml/facts/{animal}"
    if cmd.lower() in animals:
        fact_link = link.format(animal=cmd.lower())
        try:
            data = await AioHttp().get_json(fact_link)
            fact_text = data["fact"]
        except Exception:
            await message.edit("```The fact API could not be reached```")
            await asyncio.sleep(3)
            await message.delete()
        else:
            await message.edit(f"__{cmd}__\n\n`{fact_text}`")
    else:
        await message.edit("`Unsupported animal...`")
        await asyncio.sleep(3)
        await message.delete()


SYNTAX.update(
    {
        "animals": ">`.animal` <dog|cat|panda|redpanda|koala|bird|fox>"
        "\nUsage: Send you a animal picture.\n"
        ">`.afact <animal name>`"
        "\nUsage: A fact about that animal."
    }
)
