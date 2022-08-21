from . import *


@hell_cmd(pattern="Uff")
async def _(event):
    if not event.is_reply:
        return await event.edit("Reply to a self distructing pic !.!.!")
    k = await event.get_reply_message()
    pic = await k.download_media()
    await bot.send_file(
        event.chat_id,
        pic,
        caption=f"""
  OwO!! LoL, Destruction Mode Pic Destroyed!!
  Pic captured By Lêɠêɳ̃dẞø†
🌚🌝
  """,
    )
    await event.delete()
CmdHelp("Uff").add_command(
    "Uff", "This Command Can save documents"
).add_info("uff").add_warning("✅ Harmless Module.").add()
