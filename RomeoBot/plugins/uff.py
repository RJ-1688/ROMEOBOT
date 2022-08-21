from . import *


@hell_cmd(pattern="uff")
async def _(event):
    if not event.is_reply:
        return await event.edit("Reply to a self distructing pic !.!.!")
    k = await event.get_reply_message()
    pic = await k.download_media()
    await bot.send_file("me", downloadtargetcontent,
        event.chat_id,
        pic,
            )
    await event.delete()
CmdHelp("uff").add_command(
    "uff", "This Command Can save documents"
).add_info("uff").add_warning("✅ Harmless Module.").add()
