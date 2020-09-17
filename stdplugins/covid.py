"""CoronaVirus LookUp
Syntax: .covid <country>"""

from covid import Covid

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="covid ?(.*)", allow_sudo=True))
async def corona(event):
    await event.edit("`Processing...`")
    if event.pattern_match.group(1):
        country = event.pattern_match.group(1)
    else:
        country = "World"
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    ####country_data['confirmed'] + country_data['new_cases']
    #####country_data['deaths'] + country_data['new_deaths']
    if country_data:
        output_text = f"😷 **Confirmed**    : `{country_data['confirmed']}`\n"
        output_text += f"🤒 **Active**      : `{country_data['active']}`\n"
        output_text += f"🤕 **Critical**    : `{country_data['critical']}`\n"
        output_text += f"⚰️ **Deaths**      : `{country_data['deaths']}`\n"
        output_text += f"😇 **Recovered**   : `{country_data['recovered']}`\n"
        output_text += f"🧪 **Total tests** : `{country_data['total_tests']}`\n\n"

        output_text += (
            "Data provided by [Johns Hopkins University](https://j.mp/2xf6oxF)"
        )
    else:
        output_text = "No information yet about this country!"
    await event.edit(f"Corona Virus Info in **{country}**:\n\n{output_text}")
