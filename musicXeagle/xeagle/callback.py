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
        f"""<b>✨ Welcome {message.from_user.mention()}!</b>
**🎶 I'm here to help you listen to music in voice chat !**
⛑️ Find out all the **Bot's commands** and how they work by clicking on the **» ⚙️ Commands** button!""",
        reply_markup=InlineKeyboardMarkup(
                        [ 
                [
                    InlineKeyboardButton(
                        "➕ Add me to your group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "⚙️ Command​​", callback_data="cbhelp"
                    ),
                    InlineKeyboardButton(
                        "🕵🏻‍♂️ Owner", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "📣 Updates", callback_data="cmdsp"
                    ),
                    InlineKeyboardButton(
                        "🛠️ Source Code 🛠️", url=f"{SOURCE_CODE}") 
                ],[
                    InlineKeyboardButton(
                        "🗑️ Close", callback_data="close"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
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
                    InlineKeyboardButton("📝 Basic Command", callback_data="cbbasic"),
                    InlineKeyboardButton("👤 Admin Command", callback_data="cbadmin")
                ],
                [
                    InlineKeyboardButton("🥷 Owner Command", callback_data="cbowner"),
                    InlineKeyboardButton("🎶 Music Guide", callback_data="cbguide")
                ],
                [
                    InlineKeyboardButton("☚ Bᴀᴄᴋ", callback_data="cbstart")
                ]
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
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/video (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [    
                    InlineKeyboardButton("☚ Bᴀᴄᴋ", callback_data="cbhelp")
                ]
            ]
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
            [
                [
                    InlineKeyboardButton("☚ Bᴀᴄᴋ", callback_data="cbhelp")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the owner commands**
/broadcast (reply to message) - send a broadcast message from bot
🔥 __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("☚ Bᴀᴄᴋ", callback_data="cbhelp")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **HOW TO USE THIS BOT:**
1.) **first, add me to your group.**
2.) **then promote me as admin and give all permissions except anonymous admin.**
3.) **add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **turn on the video chat first before start to play music.**
🗣️ **if userbot has not joined VCG, make sure VCG is active. If so, please type /userbotleave and then type /userbotjoin again.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📖 Command List", callback_data="cbhelp")
                ],
                [
                    InlineKeyboardButton("🗑️ Close", callback_data="close")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cmdhome"))
async def cmdhome(_, query: CallbackQuery):
    
    bttn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("⛑️ Command", callback_data="cmdp")
            ],[
                InlineKeyboardButton("🗑️ Close", callback_data="close")
            ]
        ]
    )
    
    nofound = "❌ **Song not found**\n\n☛ **Please give the correct song name or click the button below to see the command**"
    
    await query.edit_message_text(nofound, reply_markup=bttn)


@Client.on_callback_query(filters.regex("cmdp"))
async def cmdsyntax(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Command** to play music on **Voice Chat:**

• `/play (query)` - for playing music via youtube
• `/ytplay (query)` - for playing music directly via youtube

Updates channel [Click here](https://t.me/{UPDATES_CHANNEL})""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("☚ Bᴀᴄᴋ", callback_data="cmdhome")]]
        ),
    )


@Client.on_callback_query(filters.regex("cmdsp"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Hello 👋** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
✨ Let's support this project, just join the channel and group 🎉""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📣 Updates", url=f"https://t.me/{UPDATES_CHANNEL}"),
                    InlineKeyboardButton("👤 Support", url=f"https://t.me/{SUPPORT_GROUP}")
                ],
                [
                    InlineKeyboardButton("🗑️ Close", callback_data="close")
                ]
            ]
        ),
    )
