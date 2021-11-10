# (C) 2021 VeezMusic-Project

from musicXeagle.helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from musicXeagle.config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    SUPPORT_GROUP,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music on groups through the new Telegram's voice chats!**
💡 **Find out all the Bot's commands and how they work by clicking on the » 📚 Commands button!**
🔖 **To know how to use this bot, please click on the » ❓ Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [[
               InlineKeyboardButton("➕ Add me to your Group 🙋‍♀️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
            [
               InlineKeyboardButton("📲 Updates", url=f"https://t.me/{UPDATES_CHANNEL}"),
               InlineKeyboardButton("💬 Support", url=f"https://t.me/{SUPPORT_GROUP}")
            ],
            [
               InlineKeyboardButton("🛠 Source Code 🛠", url=f"https://{SOURCE_CODE}")
           ]]
        ),
        reply_to_message_id=message.message_id,
    )

@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello !**
» **press the button below to read the explanation and see the list of available commands !**
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ʙᴀsɪᴄ ᴄᴍᴅ", callback_data="cbbasic"),
                    InlineKeyboardButton("ᴀᴅᴠᴀɴᴄᴇᴅ ᴄᴍᴅ", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("ᴀᴅᴍɪɴ ᴄᴍᴅ", callback_data="cbadmin"),
                    InlineKeyboardButton("sᴜᴅᴏ ᴄᴍᴅ", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("ᴏᴡɴᴇʀ ᴄᴍᴅ", callback_data="cbowner")],
                [InlineKeyboardButton("☚ ʙᴀᴄᴋ", callback_data="cbguide")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the basic commands**
🎧 [ VOICE CHAT PLAY CMD ]
/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/video (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("☚ ʙᴀᴄᴋ", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the advanced commands**
/start (in group) - see the bot alive status
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("☚ ʙᴀᴄᴋ", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the admin commands**
/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/join - invite userbot join to your group
/leave - order the userbot to leave your group
/music (on / off) - disable / enable music player in your group
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("☚ ʙᴀᴄᴋ", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the sudo commands**
/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/clear - remove all .jpg files
/eval (query) - execute code
/sh (query) - run code
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("☚ ʙᴀᴄᴋ", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the owner commands**
/stats - show the bot statistic
/broadcast (reply to message) - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot
📝 note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("☚ ʙᴀᴄᴋ", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **HOW TO USE THIS BOT:**
1.) **first, add me to your group.**
2.) **then promote me as admin and give all permissions except anonymous admin.**
3.) **after promoting me, type /reload in group to update the admin list.**
3.) **add @{ASSISTANT_NAME} to your group or type /join to invite her.**
4.) **turn on the video chat first before start to play music.**
📌 **if the userbot not joined to video chat, make sure if the video chat already turned on, or type /leave then type /join again.**
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ", callback_data="cbhelp")],
                [InlineKeyboardButton("••ᴛᴜᴛᴜᴘ••", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**💡 here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⏸ pause", callback_data="cbpause"),
                    InlineKeyboardButton("▶️ resume", callback_data="cbresume"),
                ],
                [
                    InlineKeyboardButton("⏩ skip", callback_data="cbskip"),
                    InlineKeyboardButton("⏹ stop", callback_data="cbend"),
                ],
                [InlineKeyboardButton("ᴀɴᴛɪ ᴄᴍᴅ", callback_data="cbdelcmds")],
                [InlineKeyboardButton("••ᴛᴜᴛᴜᴘ••", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""📚 **this is the feature information:**
        
**💡 Feature:** delete every commands sent by users to avoid spam in groups !
❔ usage:**
 1️⃣ to turn on feature:
     » type `/delcmd on`
    
 2️⃣ to turn off feature:
     » type `/delcmd off`
      
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("☚ ʙᴀᴄᴋ", callback_data="cbback")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
» **press the button below to read the explanation and see the list of available commands !**
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ʙᴀsɪᴄ ᴄᴍᴅ", callback_data="cblocal"),
                    InlineKeyboardButton("ᴀᴅᴠᴀɴᴄᴇᴅ ᴄᴍᴅ", callback_data="cbadven"),
                ],
                [
                    InlineKeyboardButton("ᴀᴅᴍɪɴ ᴄᴍᴅ", callback_data="cblamp"),
                    InlineKeyboardButton("sᴜᴅᴏ ᴄᴍᴅ", callback_data="cblab"),
                ],
                [InlineKeyboardButton("ᴏᴡɴᴇʀ ᴄᴍᴅ", callback_data="cbmoon")],
                [InlineKeyboardButton("☚ ʙᴀᴄᴋ", callback_data="cbstart")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **HOW TO USE THIS BOT:**
1.) **first, add me to your group.**
2.) **then promote me as admin and give all permissions except anonymous admin.**
3.) **after promoting me, type /reload in group to update the admin list.**
3.) **add @{ASSISTANT_NAME} to your group or type /join to invite her.**
4.) **turn on the video chat first before start to play music.**
📌 **if the userbot not joined to video chat, make sure if the video chat already turned on, or type /leave then type /join again.**
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("☚ ʙᴀᴄᴋ", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblocal"))
async def cblocal(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👤 **here is the basic commands**
🎧 [ VOICE CHAT PLAY CMD ]
/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/video (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("☚ ʙᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadven"))
async def cbadven(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👤 **here is the advanced commands**
/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("☚ ʙᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblamp"))
async def cblamp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👤 **here is the admin commands**
/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/join - invite userbot join to your group
/leave - order the userbot to leave your group
/auth - authorized user for using music bot
/unauth - unauthorized for using music bot
/delcmd (on | off) - enable / disable del cmd feature
/music (on / off) - disable / enable music player in your group
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("☚ ʙᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblab"))
async def cblab(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👤 **here is the sudo commands**
/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/clear - remove all .jpg files
/eval (query) - execute code
/sh (query) - run code
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("☚ ʙᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmoon"))
async def cbmoon(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👤 **here is the owner commands**
/broadcast - send a broadcast message from bot
📝 note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("☚ ʙᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )
