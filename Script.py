class script(object):
    START_TXT = """<b>Hello {},\n
๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด ๐ธ๐ <a href=https://t.me/{}>{}</a>, ๐๐ป Im a movie provider bot of @CinemaCompanyofficials I can share Movies and Series ๐\n

๐๐ค๐๐ฃ @CinemaCompanyOfficials for Movie Updates\n

๐๐๐ฃ๐๐๐ ๐
๐ฏ๐๐๐ ๐พ๐๐๐ ๐ธ๐...๐ค\n

๐๐จ๐ฐ๐๐ซ๐๐ ๐๐ฒ @CinemaCompanyofficials\n

๐ ๐ฎ๐ถ๐ป๐๐ฎ๐ถ๐ป๐ฒ๐ฑ ๐๐ @Tiyaan_bots\n
"""
    HELP_TXT = """๐ท๐ด๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐๐ท๐ด ๐ท๐ด๐ป๐ฟ ๐ต๐พ๐ ๐ผ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐.\n
๐๐๐ฃ๐๐๐ ๐
๐ฏ๐๐๐ ๐พ๐๐๐ ๐ธ๐...๐ค\n

๐๐จ๐ฐ๐๐ซ๐๐ ๐๐ฒ @CinemaCompanyofficials\n

๐ ๐ฎ๐ถ๐ป๐๐ฎ๐ถ๐ป๐ฒ๐ฑ ๐๐ @Tiyaan_bots
"""
    ABOUT_TXT = """โฏ ๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด: {}
๐จโ๐ป แดแดแด แดสแดแดแดส : <a href=https://t.me/sreehari3><b></b>SH</a>\n
๐ สแดษดษขแดแดษขแด : แดสสแดษขสแดแด\n
๐ ๊ฐสแดแดแดแดกแดสแด : แดสแดสแดษด 3\n
๐ก สแดsแดแดแด แดษด : KOYEB\n
๐ข แดแดแดแดแดแดs แดสแดษดษดแดส : <a href=https://t.me/CinemaCompanyOffiz><b></b>แดแดแดแดแดแด</a>\n
๐ แด แดสsษชแดษด : แด  1.1.0\n</b></i>"""
    SOURCE_TXT = """<b>๐๐ซ๐๐๐ญ๐ ๐๐ง๐ ๐๐ข๐ค๐ ๐๐ก๐ข๐ฌ:</b>
ยป I will Create One Bot For You<b>
ยป Contact Me @Tiyaan_SH<b
<b>DEVS:</b>
- <a href=https://t.me/CinemaCompanyofficials>๐พ๐๐ฃ๐๐ข๐ ๐พ๐ค๐ข๐ฅ๐๐ฃ๐ฎ</a>"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
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
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b><u>Cแดสสแดษดแด Dแดแดแดสแดsแด Sแดแดแดแดs</b></u>
    
๐ าษชสแดs sแดแด แดแด: <code>{}</code>
๐ฉ๐ปโ๐ป แดsแดสs: <code>{}</code>
๐ฅ ษขสแดแดแดs: <code>{}</code>
๐๏ธ แดแดแดแดแดษชแดแด: <code>{}</code>
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
