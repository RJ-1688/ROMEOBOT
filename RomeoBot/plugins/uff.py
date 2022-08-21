from . import *


@hell_cmd(pattern="Uff")
async def downloader(_, message: Message):
    targetcontent = message.reply_to_message
    downloadtargetcontent = await client.download_media(targetcontent)
    send = await client.send_document("me", downloadtargetcontent)
    os.remove(downloadtargetcontent)



CmdHelp("Uff").add_command(
    "Uff", "This Command Can save documents"
).add_info("uff").add_warning("✅ Harmless Module.").add()
