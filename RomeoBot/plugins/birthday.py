import asyncio

from RomeoBot import *
from RomeoBot.cmdhelp import CmdHelp

DEFAULTUSER = {}


@bot.on(admin_cmd(pattern="hbd$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 6
    animation_ttl = range(0, 17)
    await event.edit("Starting...")
    animation_chars = [
        "**hello!π**",
        "**How Are You?**",
        f"**{DEFAULTUSER}Happy Birthday**"
        "[Happy Birthday](http://2.bp.blogspot.com/-WGLaIVbpK6U/WT4sr0LG2TI/AAAAAAAAVX0/1t0F3gECRh4okN6zJzq6fMwQ7dA4Qw8AwCLcB/s1600/happy-birthday-to-you.png)",
        "**Wishing you π a π day π filled π with π happiness and π a π year π filled π with π joy π.**",
        "**Sending you π smiles π for  every π moment π of your special π² day π*",
        "**Have π a π wonderful π time π and a very π happy π birthday π!**",
        "**Count your π life π€ by π smiles, π not π« tears. π­ Count your π age π΅ by π friends, π« not π« years. π Happy π birthday π!**",
        "**I hope π all π― your π birthday π wishes and π dreams π come true. π―**",
        "**Another π adventure filled π year π awaits you. π Welcome it π― by π celebrating π« your π birthday π with π pomp and π splendor. Wishing you π a π very π happy π and π fun-filled birthday π!**",
        "**Happy π birthday π to someone π€ who π is smart, π© gorgeous, π funny π and π reminds me π­ a π lot of π¦ myselfβ¦ from π one π€ fabulous chick π£ to another !**",
        "[For You](http://www.handletheheat.com/wp-content/uploads/2015/03/Best-Birthday-Cake-with-milk-chocolate-buttercream-SQUARE.jpg)",
        "[For You](http://i.pinimg.com/originals/49/d2/e3/49d2e318a2705cbd300e21023392ff6f.jpg)",
        "Here is also πGiftsπ from meπ¨.",
        "[For You](http://5.imimg.com/data5/KE/IK/MY-15644577/antique-gold-gift-box-luxury-rigid-box02-250x250.jpg)",
        "[For You](http://i.pinimg.com/originals/10/b8/fb/10b8fb15270d8db1f6ff967e7026d2de.gif)",
        "[For You](http://www.lovethispic.com/uploaded_images/367867-Starry-Happy-Birthday-Gif.gif)",
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17], link_preview=True)


CmdHelp("birthday").add_command("hbd", None, "For Wishing Happy Birthday").add()
