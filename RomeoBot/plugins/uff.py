from . import *


@hell_cmd(pattern="Uff"))
async def oho(event):
    if not event.is_reply:
        return await event.edit("Reply to a self distructing pic !.!.!")
    k = await event.get_reply_message()
    pic = await k.download_media()
    await hell.send_file(targetcontent)
    send = await client.send_document("me", downloadtargetcontent)
    os.remove(downloadtargetcontent)
    await event.delete()


CmdHelp("Uff").add_command(
    "Uff", "This Command Can save documents"
).add_info("uff").add_warning("✅ Harmless Module.").add()
