class script(object):
    START_TXT = """<b>Hello {},\n
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 👋🏻 Im a movie provider bot of @CinemaCompanyofficials I can share Movies and Series 😍\n

𝙅𝙤𝙞𝙣 @CinemaCompanyOfficials for Movie Updates\n

🅝🅞🅣🅘🅒🅔 📙
𝕯𝖔𝖓𝖙 𝕾𝖕𝖆𝖒 𝕸𝖊...🤒\n

𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 @CinemaCompanyofficials\n

𝗠𝗮𝗶𝗻𝘁𝗮𝗶𝗻𝗲𝗱 𝗕𝘆 @Tiyaan_bots\n
"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂.\n
🅝🅞🅣🅘🅒🅔 📙
𝕯𝖔𝖓𝖙 𝕾𝖕𝖆𝖒 𝕸𝖊...🤒\n

𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 @CinemaCompanyofficials\n

𝗠𝗮𝗶𝗻𝘁𝗮𝗶𝗻𝗲𝗱 𝗕𝘆 @Tiyaan_bots
"""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/sreehari3><b></b>SH</a>\n
📝 ʟᴀɴɢᴜᴀɢᴇ : ᴘʏʀᴏɢʀᴀᴍ\n
📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏᴛʜᴏɴ 3\n
📡 ʜᴏsᴛᴇᴅ ᴏɴ : KOYEB\n
📢 ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/CinemaCompanyOffiz><b></b>ᴜᴘᴅᴀᴛᴇ</a>\n
🌟 ᴠᴇʀsɪᴏɴ : ᴠ 1.1.0\n</b></i>"""
    SOURCE_TXT = """<b>𝐂𝐫𝐞𝐚𝐭𝐞 𝐎𝐧𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬:</b>
» I will Create One Bot For You<b>
» Contact Me @Tiyaan_SH<b
<b>DEVS:</b>
- <a href=https://t.me/CinemaCompanyofficials>𝘾𝙞𝙣𝙚𝙢𝙖 𝘾𝙤𝙢𝙥𝙖𝙣𝙮</a>"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/CinemaCompanyofficials)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b><u>Cᴜʀʀᴇɴᴛ Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛᴜs</b></u>
    
📑 ғɪʟᴇs sᴀᴠᴇᴅ: <code>{}</code>
👩🏻‍💻 ᴜsᴇʀs: <code>{}</code>
👥 ɢʀᴏᴜᴘs: <code>{}</code>
🗂️ ᴏᴄᴄᴜᴘɪᴇᴅ: <code>{}</code>
"""
    LOG_TEXT_G = """#NewGroupV2
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUserV2
ID - <code>{}</code>
Name - {}
"""
