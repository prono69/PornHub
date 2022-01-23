"""Count Number of Files in a Chat
Original Module Credits: https://t.me/UniBorg/127"""


@borg.on(slitu.admin_cmd(pattern="conftc ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    entity = event.chat_id
    if input_str := event.pattern_match.group(1):
        entity = input_str
    status_message = await event.reply(
        "... this might take some time "
        "depending on the number of messages "
        "in the chat ..."
    )
    mus = 0
    hmm = {}
    async for message in event.client.iter_messages(
        entity=entity,
        limit=None
    ):
        if message and message.file:
            if message.file.mime_type not in hmm:
                hmm[message.file.mime_type] = 0
            hmm[message.file.mime_type] += message.file.size
    hnm = {key: slitu.humanbytes(hmm[key]) for key in hmm}
    await status_message.edit(
        slitu.yaml_format(hnm),
        parse_mode=slitu.parse_pre
    )

