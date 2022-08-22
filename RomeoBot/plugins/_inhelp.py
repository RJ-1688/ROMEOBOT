import asyncio
import html
import os
import re
import random
import sys

from math import ceil
from re import compile

from telethon import Button, custom, events, functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

from RomeoBot.sql.gvar_sql import gvarstat
from . import *

hell_row = Config.BUTTONS_IN_HELP
hell_emoji = Config.EMOJI_IN_HELP
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"
LOG_GP = Config.LOGGER_ID
USER_BOT_WARN_ZERO = "𝐎𝐲𝐞 𝐛𝐬𝐬𝐬 𝐤𝐚𝐫 𝐛𝐨𝐥𝐚 𝐧 𝐬𝐩𝐚𝐦 𝐧𝐡𝐢 𝐰𝐚𝐫𝐧𝐚 𝐛𝐥𝐨𝐜𝐡 𝐡𝐨𝐠𝐞"

alive_txt = """{}\n
<b><i>🌹 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🌹</b></i>
"""

def button(page, modules):
    Row = hell_row
    Column = 3

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(f"🔥" + pair + f"🔥", data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
               f"🔥 𝐁𝐚𝐜𝐤 💥", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"• ❌ •", data="close"
            ),
            custom.Button.inline(
               f"💥 𝐍𝐞𝐱𝐭 🔥", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]


    modules = CMD_HELP
if Config.BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(InlineQuery)
    async def inline_handler(event):
        cids = await client_id(event, event.query.user_id)
        ForGo10God, HELL_USER, hell_mention = cids[0], cids[1], cids[2]
        builder = event.builder
        result = None
        query = event.text
        auth = await clients_list()
        if event.query.user_id in auth and query == "RomeoBot_help":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            a = gvarstat("HELP_PIC")
            if a:
                help_pic = a.split(" ")[0]
            else:
                help_pic = "https://telegra.ph/file/59b9eba6a5c7801d287d1.jpg"
                
                help_msg = f"🌹 **{hell_mention}**\n\n🌹𝐏𝐥𝐮𝐠𝐢𝐧𝐬: `{len(CMD_HELP)}` \n🌹𝐂𝐦𝐝𝐬: `{len(apn)}`\n🌹𝐏𝐚𝐠𝐞: 1/{veriler[0]}"
                
                #help_msg = f"╔═══💫✨💫═══\n"
                #help_msg = f"┃**{hell_mention}**\n"
                #help_msg = f"╚═══💫✨💫═══\n"
                #help_msg = f"╔══════✣✤༻⋇༺✤✣══════╗\n"
                #help_msg = f"┣🌹𝐏𝐥𝐮𝐠𝐢𝐧𝐬: `{len(CMD_HELP)}` \n"
                #help_msg = f"┣🌹𝐂𝐦𝐝𝐬: `{len(apn)}`\n"
                #help_msg = f"┣🌹𝐏𝐚𝐠𝐞: 1/{veriler[0]}`\n"
                #help_msg = f"╚══════✣✤༻⋇༺✤✣══════╝\n"""
                
            if help_pic == "DISABLE":
                result = builder.article(
                    f"Hey! Only use {hl}help please",
                    text=help_msg,
                    buttons=veriler[1],
                    link_preview=False,
                )
            elif help_pic.endswith((".jpg", ".png")):
                result = builder.photo(
                    help_pic,
                    text=help_msg,
                    buttons=veriler[1],
                    link_preview=False,
                )
            elif help_pic:
                result = builder.document(
                    help_pic,
                    text=help_msg,
                    title="RomeoBot Alive",
                    buttons=veriler[1],
                    link_preview=False,
                )
        elif event.query.user_id in auth and query == "alive":
            uptime = await get_time((time.time() - StartTime))
            alv_msg = gvarstat("ALIVE_MSG") or "»»» <b>𝐑𝐨𝐦𝐞𝐨 𝐨𝐧 𝐝𝐮𝐭𝐲</b> «««"
            he_ll = alive_txt.format(alv_msg, tel_ver, hell_ver, uptime, abuse_m, is_sudo)
            alv_btn = [
                [Button.url(f"{HELL_USER}", f"tg://openmessage?user_id={ForGo10God}")],
                [Button.url("𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐂𝐇𝐍𝐋", f"https://t.me/{my_channel}"), 
                Button.url("𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐏", f"https://t.me/{my_group}")],
            ]
            a = gvarstat("ALIVE_PIC")
            pic_list = []
            if a:
                b = a.split(" ")
                if len(b) >= 1:
                    for c in b:
                        pic_list.append(c)
                PIC = random.choice(pic_list)
            else:
                PIC = "https://telegra.ph/file/59b9eba6a5c7801d287d1.jpg"
            if PIC and PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    PIC,
                    text=he_ll,
                    buttons=alv_btn,
                    link_preview=False,
                    parse_mode="HTML",
                )
            elif PIC:
                result = builder.document(
                    PIC,
                    text=he_ll,
                    title="RomeoBot Alive",
                    buttons=alv_btn,
                    link_preview=False,
                    parse_mode="HTML",
                )
            else:
                result = builder.article(
                    text=he_ll,
                    title="RomeoBot Alive",
                    buttons=alv_btn,
                    link_preview=False,
                    parse_mode="HTML",
                )

        elif event.query.user_id in auth and query == "pm_warn":
            CSTM_PMP = gvarstat("CUSTOM_PMPERMIT") or "𝐊𝐲𝐚 𝐤𝐚𝐚𝐦 𝐇"
            HELL_FIRST = "**𝐇𝐞𝐥𝐥𝐨 \n    𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 {}'𝐬 𝐩𝐦**\n\n 😎 𝐃𝐨𝐧𝐭'𝐧 𝐓𝐫𝐲 𝐓𝐨 𝐒𝐩𝐚𝐦 𝐇𝐞𝐫𝐞 😎".format(hell_mention, CSTM_PMP)
            a = gvarstat("PMPERMIT_PIC")
            pic_list = []
            if a:
                b = a.split(" ")
                if len(b) >= 1:
                    for c in b:
                        pic_list.append(c)
                PIC = random.choice(pic_list)
            else:
                PIC = "https://telegra.ph/file/59b9eba6a5c7801d287d1.jpg"
            if PIC and PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    file=PIC,
                    text=HELL_FIRST,
                    buttons=[
                        [custom.Button.inline("📝 𝐑𝐞𝐪𝐮𝐞𝐬𝐭", data="req")],
                        [custom.Button.inline("🚫 𝐁𝐥𝐨𝐜𝐤", data="heheboi")],
                        [custom.Button.inline("❓ 𝐂𝐮𝐫𝐢𝐨𝐮𝐬", data="pmclick")],
                    ],
                    link_preview=False,
                )
            elif PIC:
                result = builder.document(
                    file=PIC,
                    text=HELL_FIRST,
                    title="𝐏𝐦 𝐏𝐞𝐫𝐦𝐢𝐭",
                    buttons=[
                        [custom.Button.inline("📝 𝐑𝐞𝐪𝐮𝐞𝐬𝐭", data="req")],
                        [custom.Button.inline("🚫 𝐁𝐥𝐨𝐜𝐤", data="heheboi")],
                        [custom.Button.inline("❓ 𝐂𝐮𝐫𝐢𝐨𝐮𝐬", data="pmclick")],
                    ],
                    link_preview=False,
                )
            else:
                result = builder.article(
                    text=HELL_FIRST,
                    title="𝐏𝐦 𝐏𝐞𝐫𝐦𝐢𝐭",
                    buttons=[
                        [custom.Button.inline("📝 𝐑𝐞𝐪𝐮𝐞𝐬𝐭", data="req")],
                        [custom.Button.inline("🚫 𝐁𝐥𝐨𝐜𝐤", data="heheboi")],
                        [custom.Button.inline("❓ 𝐂𝐮𝐫𝐢𝐨𝐮𝐬", data="pmclick")],
                    ],
                    link_preview=False,
                )
                
        elif event.query.user_id in auth and query == "repo":
            result = builder.article(
                title="Repository",
                text=f"**🌹 𝐑𝐨𝐦𝐞𝐨𝐁𝐨𝐭 🌹**",
                buttons=[
                    [Button.url("🌹 𝐆𝐑𝐎𝐔𝐏 🌹", "https://t.me/Bot_Updates_Chnl")],
                ],
            )

        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )

        else:
            result = builder.article(
                "@Bot_Support_Grp",
                text="""**𝐇𝐞𝐲 𝐓𝐡𝐢𝐬 𝐢𝐬 [𝐑𝐨𝐦𝐞𝐨𝐁𝐨𝐭](https://t.me/Bot_Support_Grp)**""",
                buttons=[
                    [
                        custom.Button.url("🌹 𝐑𝐨𝐦𝐞𝐨_𝐒𝐭𝐫𝐢𝐧𝐠 🌹", "https://t.me/Rjssgbot"),
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"pmclick")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for Other Users..."
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"🔰 This is Lêɠêɳ̃dẞø† PM Security for {legend_mention} to keep away unwanted retards from spamming PM..."
            )

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"req")))
    async def on_pm_click(legend):
        if legend.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master {legend_mention} Im Try To Get Rid Of This Nigga Pls Dont Touch"
            await legend.answer(fck_bit, cache_time=0, alert=True)
            return
        await legend.get_chat()
        legend.query.user_id
        await legend.edit(
            "Oh You Wanna Talk With My Master\n\nPls Wait Dear \n\n**Btw** **You Can Wait For My Master**"
        )
        await asyncio.sleep(2)
        await legend.edit(
            "Which Type Of Request U Want?",
            buttons=[
                [Button.inline("Register", data="school")],
                [Button.inline("As Usual", data="tg_okay")],
            ],
        )
        yup_text = "`Warning`-❗️⚠️Don't send any message now wait kindly!!!❗️⚠️"
        await bot.send_message(legend.query.user_id, yup_text)



    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"tg_okay")))
    async def yeahbaba(event):
        if event.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master.This Is for other users"
            await event.answer(fck_bit, cache_time=0, alert=True)
        else:
            event_mention = f"[{bot.me.first_name}](tg://user?id={bot.uid})"
            await event.edit(
                f"✅ **Request Registered** \n\n{event_mention} will now decide to talk with u or not\n😐 Till then wait patiently and don't spam!!"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
                tosend = f"**👀 Hey {event_mention} !!** \n\n⚜️ You Got A Request From [{first_name}](tg://user?id={ok}) In PM!!"
                await bot.send_message(LOG_GP, tosend)

     
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"school")))
    async def yeahbaba(event):
        if event.query.user_id == bot.uid:
            fck_bit = f"This Is For Other user"
            await event.answer(fck_bit, cache_time=0, alert=True)
        else:
            event_mention = f"[{bot.me.first_name}](tg://user?id={bot.uid})"
            await event.edit(
                f"✅ **Request Registered** \n\n{event_mention} will now decide to look for your request or not.\n😐 Till then wait patiently and don't spam!!"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"**👀 Hey {event_mention} !!** \n\n⚜️ You Got A Request From [{first_name}](tg://user?id={ok}) In PM!!"
            await bot.send_message(LOG_GP, tosend)
 

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"chat")))
    async def on_pm_click(event):
        event.query.user_id
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            event_mention = f"[{bot.me.first_name}](tg://user?id={bot.uid})"
            await event.edit(
                f"Ahh!! You here to do chit-chat!!\n\nPlease wait for {event_mention} to come. Till then keep patience and don't spam."
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"**👀 Hey {event_mention} !!** \n\n⚜️ You Got A PM from  [{first_name}](tg://user?id={ok})  for random chats!!"
            await bot.send_message(LOG_GP, tosend)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"heheboi")))
    async def on_pm_click(legend):
        if legend.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master{legend_mention} Im Try To Get Rid Of This Nigga Pls Dont Touch"
            await legend.answer(fck_bit, cache_time=0, alert=True)
            return
        await legend.get_chat()
        legend_id = legend.query.user_id
        await legend.edit("Okay let Me Think🤫")
        await asyncio.sleep(2)
        await legend.edit("Okay Giving You A Chance🤨")
        await asyncio.sleep(2)
        await legend.edit(
            "Will You Spam?",
            buttons=[
                [Button.inline("Yes", data="lemme_ban")],
                [Button.inline("No", data="hmm")],
            ],
        )

        reqws = "`Warning`- ❗️⚠️Don't send any message now wait kindly!!!❗️⚠️"

        await bot.send_message(legend.query.user_id, reqws)
        await bot.send_message(
            LOG_GP,
            message=f"Hello, Master  [Nibba](tg://user?id={legend_id}). Wants To Request Something.",
            buttons=[Button.url("Contact Him", f"tg://user?id=legend_id")],
        )


    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hmm")))
    async def yes_ucan(legend):
        if legend.query.user_id == bot.uid:
            lmaoo = "You Are Not Requesting , Lol."
            await legend.answer(lmaoo, cache_time=0, alert=True)
            return
        await legend.get_chat()
        await asyncio.sleep(2)
        legend.query.user_id
        await legend.edit("Okay You Can Wait Till Wait")
        hmmmmm = "Okay Kindly wait  i will inform you"
        await bot.send_message(legend.query.user_id, hmmmmm)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lemme_ban")))
    async def yes_ucan(legend):
        if legend.query.user_id == bot.uid:
            lmaoo = "You Are Not Requesting , Lol."
            await legend.answer(lmaoo, cache_time=0, alert=True)
            return
        await legend.get_chat()
        await asyncio.sleep(2)
        legend_id = legend.query.user_id
        await legend.edit("Get Lost Retard")
        ban = f"Pahli Fursat Me Nikal\nU Are Blocked"
        await bot.send_message(legend.query.user_id, ban)
        await bot(functions.contacts.BlockRequest(legend.query.user_id))
        await bot.send_message(
            LOG_GP,
            message=f"Hello, Master  [Nibba](tg://user?id={legend_id}). Has Been Blocked Due to Choose Spam",
            buttons=[Button.url("Contact Him", f"tg://user?id=legend_id")],
        )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lemme_ban")))
    async def yes_ucan(legend):
        if legend.query.user_id == bot.uid:
            lmaoo = "You Are Not Requesting , Lol."
            await legend.answer(lmaoo, cache_time=0, alert=True)
            return
        await legend.get_chat()
        await asyncio.sleep(2)
        legend_id = legend.query.user_id
        await legend.edit("Get Lost Retard")
        ban = f"Pahli Fursat Me Nikal\nU Are Blocked"
        await bot.send_message(legend.query.user_id, ban)
        await bot(functions.contacts.BlockRequest(legend.query.user_id))
        await bot.send_message(
            LOG_GP,
            message=f"Hello, Master  [Nibba](tg://user?id={legend_id}). Has Been Blocked Due to Choose Spam",
            buttons=[Button.url("Contact Him", f"tg://user?id=legend_id")],
        )

   
    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"unmute")))
    async def on_pm_click(event):
        hunter = (event.data_match.group(2)).decode("UTF-8")
        legend = hunter.split("+")
        if not event.sender_id == int(legend[0]):
            return await event.answer("This Ain't For You!!", alert=True)
        try:
            await bot(GetParticipantRequest(int(legend[1]), int(legend[0])))
        except UserNotParticipantError:
            return await event.answer("You need to join the channel first.", alert=True)
        await bot.edit_permissions(
            event.chat_id, int(legend[0]), send_message=True, until_date=None
        )
        await event.edit("Yay! You can chat now !!")


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"reopen")))
    async def reopn(event):
        cids = await client_id(event, event.query.user_id)
        ForGo10God, HELL_USER, hell_mention = cids[0], cids[1], cids[2]
        auth = await clients_list()
        if event.query.user_id in auth:
            current_page_number=0
            simp = button(current_page_number, CMD_HELP)
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            await event.edit(
                         f"🌹**{hell_mention}**\n\n🌹𝐏𝐥𝐮𝐠𝐢𝐧𝐬: `{len(CMD_HELP)}` \n🌹𝐂𝐦𝐝𝐬: `{len(apn)}`\n🌹𝐏𝐚𝐠𝐞: 1/{veriler[0]}",
                
                           #f"╔═══💫✨💫═══\n"
                           #f"┃**{hell_mention}**\n"
                           #f"╚═══💫✨💫═══\n"
                           #f"╔══════✣✤༻⋇༺✤✣══════╗\n"
                           #f"┣🌹𝐏𝐥𝐮𝐠𝐢𝐧𝐬: `{len(CMD_HELP)}` \n"
                           #f"┣🌹𝐂𝐦𝐝𝐬: `{len(apn)}`\n"
                           #f"┣🌹𝐏𝐚𝐠𝐞: 1/{veriler[0]}`\n"
                           #f"╚══════✣✤༻⋇༺✤✣══════╝\n","""
                           
                buttons=simp[1],
                link_preview=False,
            )
        else:
            reply_pop_up_alert = "𝐘𝐨𝐮 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        cids = await client_id(event, event.query.user_id)
        ForGo10God, HELL_USER, hell_mention = cids[0], cids[1], cids[2]
        auth = await clients_list()
        if event.query.user_id in auth:
            veriler = custom.Button.inline(f"{hell_emoji} Re-Open Menu {hell_emoji}", data="reopen")
            await event.edit(f"**🌹 𝐁𝐨𝐭 𝐦𝐞𝐧𝐮 𝐏𝐫𝐨𝐯𝐢𝐝𝐞𝐫 𝐧𝐨𝐰 𝐜𝐥𝐨𝐬𝐞𝐝 🌹**\n\n**𝐑𝐎𝐌𝐄𝐎𝐁𝐎𝐓**  {hell_mention}\n\n        [©️𝕽𝖔𝖒𝖊𝖔𝕭𝖔𝖙 ™️]({chnl_link})", buttons=veriler, link_preview=False)   
                                #f"╔═══💫✨💫═══\n"
                                #f"┃**🌹 𝐁𝐨𝐭 𝐦𝐞𝐧𝐮 𝐏𝐫𝐨𝐯𝐢𝐝𝐞𝐫 𝐧𝐨𝐰 𝐜𝐥𝐨𝐬𝐞𝐝 🌹**\n"
                                #f"┃**𝕽𝖔𝖒𝖊𝖔𝕭𝖔𝖙 :**  {hell_mention}\n"  
                                #f"╚═══💫✨💫═══\n"
                                #[©️ ԱӀէɾօղβօէ ™️]({chnl_link})", buttons=veriler, link_preview=False)"
        else:
            reply_pop_up_alert = "𝐘𝐨𝐮 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
   

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        cids = await client_id(event, event.query.user_id)
        ForGo10God, HELL_USER, hell_mention = cids[0], cids[1], cids[2]
        auth = await clients_list()
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        apn = []
        for x in CMD_LIST.values():
            for y in x:
                apn.append(y)
        if event.query.user_id in auth:
            await event.edit(
                           f"🌹 **{hell_mention}**\n\n🌹𝐏𝐥𝐮𝐠𝐢𝐧𝐬: `{len(CMD_HELP)}` \n🌹𝐂𝐦𝐝𝐬: `{len(apn)}`\n🌹𝐏𝐚𝐠𝐞: 1/{veriler[0]}",
                           #f"╔═══💫✨💫═══\n"
                           #f"┃**{hell_mention}**\n"
                           #f"╚═══💫✨💫═══\n"
                           #f"╔══════✣✤༻⋇༺✤✣══════╗\n"
                           #f"┣🌹𝐏𝐥𝐮𝐠𝐢𝐧𝐬: `{len(CMD_HELP)}` \n"
                           #f"┣🌹𝐂𝐦𝐝𝐬: `{len(apn)}`\n"
                           #f"┣🌹𝐏𝐚𝐠𝐞: 1/{veriler[0]}`\n"
                           #f"╚══════✣✤༻⋇༺✤✣══════╝\n","""
                buttons=veriler[1],
                link_preview=False,
            )
        else:
            return await event.answer("𝐘𝐨𝐮 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞", cache_time=0, alert=True)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)")))
    async def Information(event):
        cids = await client_id(event, event.query.user_id)
        ForGo10God, HELL_USER, hell_mention = cids[0], cids[1], cids[2]
        auth = await clients_list()
        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline("🌹 " + cmd[0] + " 🌹", data=f"commands[{commands}[{page}]]({cmd[0]})")
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer("No Description is written for this plugin", cache_time=0, alert=True)

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline(f"🌹 𝐌𝐚𝐢𝐧 𝐌𝐞𝐧𝐮 🌹", data=f"page({page})")])
        if event.query.user_id in auth:
            await event.edit(
                f"**📗 File :**  `{commands}`\n**🔢 Number of commands :**  `{len(CMD_HELP_BOT[commands]['commands'])}`",
                buttons=buttons,
                link_preview=False,
            )
        else:
            return await event.answer("𝐘𝐨𝐮 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞", cache_time=0, alert=True)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)")))
    async def commands(event):
        cids = await client_id(event, event.query.user_id)
        ForGo10God, HELL_USER, hell_mention = cids[0], cids[1], cids[2]
        auth = await clients_list()
        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")
        result = f"**📗 File :**  `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ Warning :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n"
        else:
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ Warning :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**ℹ️ Info :**  {CMD_HELP_BOT[cmd]['info']['info']}\n"
        sextraa = CMD_HELP_BOT[cmd]["extra"]
        if sextraa:
            a = sorted(sextraa.keys())
            for b in a:
                c = b
                d = sextraa[c]["content"]
                result += f"**{c} :**  `{d}`\n"
        result += "\n"
        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**🛠 Commands :**  `{HANDLER[:1]}{command['command']}`\n"
        else:
            result += f"**🛠 Commands :**  `{HANDLER[:1]}{command['command']} {command['params']}`\n"
        if command["example"] is None:
            result += f"**💬 Explanation :**  `{command['usage']}`\n\n"
        else:
            result += f"**💬 Explanation :**  `{command['usage']}`\n"
            result += f"**⌨️ For Example :**  `{HANDLER[:1]}{command['example']}`\n\n"
        if event.query.user_id in auth:
            await event.edit(
                result,
                buttons=[custom.Button.inline(f"🌹 𝐑𝐞𝐭𝐮𝐫𝐧 🌹", data=f"Information[{page}]({cmd})")],
                link_preview=False,
            )
        else:
            return await event.answer("𝐘𝐨𝐮 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞", cache_time=0, alert=True)


# RomeoBot
