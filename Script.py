class script(object):
    START_TXT = """
<pre>Hey, {} how are you:).
𝖨𝗆 𝖺 music x 𝖿𝗂𝗅𝗍𝖾𝗋 𝖻𝗈𝗍 𝗐𝗁𝗂𝖼𝗁 𝖼𝖺𝗇 𝗉𝗋𝗈𝗏𝗂𝖽𝖾 Musics here or add me to 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉 and request there.</pre>

<b>Click Help for more information.</b></blockquote>
"""
    HELP_TXT = """
🎵 <b>help for music search:</b>

Hey  {} , To find music just enter it's name of the song here. or you can add me in your Group and request there.
"""
    ABOUT_TXT = """<b>
× <b>Owner of Repo:</b> <a href=https://github.com/adi-code22>Eva-Maria</a>
• <b>Language:</b> Python 3
× <b>Database:</b> Mongo DB
• <b>Server:</b> VPS👀</b>"""
    SOURCE_TXT = """<b>NOTE:</b>
- Music Filter x Bot  is a open source project. 
- Source - <ahref=https://github.com/adi-code22/EvaMaria>Click Here to get source code</a>

<b>DEVS:</b>
-<a href=https://github.com/adi-code22/EvaMaria>Eva</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter is the feature were users can set automated replies for a particular keyword and shobana will respond whenever a keyword is found the message
<b>NOTE:</b>
1. This Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- This Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/xbots_x)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """
<b>Add MUSIC'S to my DB, and use to your group!</b>

× Add me to your music requesting group.
×✅ Make me admin in your Group ✖️🎵.
× and request Music's there.

×+ If you want to add your musics files to my Database, just forward last message from your music DB channel, or copy the last message link from your music database channel and paste here.
×÷ and don't forward movie files. Audios file's only

/buggs to report my owner.
"""
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
these are the extra features of ShobanaFilterBot

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>
• /start - <code>Check I'm Alive.</code>
• /ping - <code>check ping.</code>
• /usage - <code>usage of bot.</code>
• /info - <code>User info .</code>
• /id - <code>User id  .</code>
• /broadcast - <code>Broadcast (owner only).</code>
"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
/logs - <code>to get the rescent errors</code>
/stats - <code>to get status of files in db.</code>
/delete - <code>to delete a specific file from db.</code>
/users - <code>to get list of my users and ids.</code>
/chats - <code>to get list of the my chats and ids </code>
/leave  - <code>to leave from a chat.</code>
/disable  -  <code>do disable a chat.</code>
/ban  - <code>to ban a user.</code>
/unban  - <code>to unban a user.</code>
/channel - <code>to get list of total connected channels</code>
/broadcast - <code>to broadcast a message to all users</code>
/ping - <code>check ping.</code>
/usage - <code>usage of bot.</code>
/delete| /deleteall - delete files 
/set_template
/setskip
"""

    
    STATUS_TXT = """
<b>My Status:</b>
    
× <b>We are here saved <code>{}</code> audio files.</b>

<pre>× <b>Users:</b> <code>{}</code>
× <b>Chats:</b> <code>{}</code>
 
× <b>Used Storage:</b> <code>{}</code> 
× <b>Free Storage:</b> <code>{}</code></pre>
 """
    
    LOG_TEXT_G = """#NewGroup
× <b>Group id:</b> {}(<code>{}</code>)
• <b>Total Members:</b> <code>{}</code>
× <b>Added By:</b> {}
"""
    RESULT_TXT="""
<pre><blockquote>🎧Here is your results.</blockquote></pre>"""

    CUSTOM_FILE_CAPTION = """
<pre><blockquote>🎧 {file_name} | {file_size}</blockquote></pre>

<b>©️: @XBOTS_X</b>
"""
#</pre>
    
    RESTART_GC_TXT = """
<b>𝖡𝗈𝗍 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽 !</b>

📅 𝖣𝖺𝗍𝖾 : <code>{}</code>
⏰ 𝖳𝗂𝗆𝖾 : <code>{}</code>
🌐 𝖳𝗂𝗆𝖾𝗓𝗈𝗇𝖾 : <code>Asia/Kolkata</code>
🛠️ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌 : <code>𝗏1 [ 𝖲𝗍able ]</code></b>"""
    
    LOG_TEXT_P = """#NewUser
UserID: <code>{}</code>
Name: {}
"""
    SPOLL_NOT_FND="""<blockquote> Hi,</blockquote>
I couldn't find anything related to your request. 
Try reading the instruction below 👇🏼
    """
#SPELL CHECK LANGUAGES TO KNOW callback
    ENG_SPELL="""Please Note Below📓
    Ask in Correct Spelling
    """
    MAL_SPELL="""ദയവായി താഴെ ശ്രദ്ധിക്കുക
ശരിയായ അക്ഷരവിന്യാസത്തിൽ ചോദിക്കുക
    """
    HIN_SPELL="""
    👀👀👀
    """
    TAM_SPELL="""
   👀👀👀
    """

    CHK_MOV_ALRT="""♻️ Cheking files on my DB... ♻️"""
    
    OLD_MES="""Dont Click Old Message!!!"""
    
    MOV_NT_FND="""
<pre>Report To ADMIN BY USING /bugs command </pre> 
"""
    RESTART_TXT = """
<b><u>𝖡𝗈𝗍 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽 ✅</u></b>"""
