import os, time, re
id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "20793620")
    API_HASH  = os.environ.get("API_HASH", "a712d2b8486f26c4dee5127cc9ae0615")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7650038873:AAE3251kM19h0BExI-KTou2LfJEKDJ0Q6gI") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","rename")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://pokemonchannel098:yaE7BvFwWIXdb3HQ@cluster0.gdr57.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://envs.sh/jUp.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "Weoo_Animes") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "1002296271857"))
    BIN_CHANNEL = int(os.environ.get("BIN_CHANNEL", "1002296271857"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """{},

𝖴𝗌𝗂𝗇𝗀 𝗍𝗁𝗂𝗌 𝖻𝗈𝗍 𝗒𝗈𝗎 𝖼𝖺𝗇 𝗋𝖾𝗇𝖺𝗆𝖾 𝖺𝗇𝖽 𝖼𝗁𝖺𝗇𝗀𝖾 𝗍𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅 𝖿𝖿 𝗒𝗈𝗎𝗋 𝖿𝗂𝗅𝖾𝗌. 𝖠𝗇𝖽 𝗒𝗈𝗎 𝖼𝖺𝗇 𝖺𝗅𝗌𝗈 𝖼𝗈𝗇𝗏𝖾𝗋𝗍 𝗏𝗂𝖽𝖾𝗈 𝗍𝗈 𝖿𝗂𝗅𝖾 𝖺𝗇𝖽 𝖿𝗂𝗅𝖾 𝗍𝗈 𝗏𝗂𝖽𝖾𝗈.

𝖳𝗁𝗂𝗌 𝖻𝗈𝗍 𝖺𝗅𝗌𝗈 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝗌 𝖼𝗎𝗌𝗍𝗈𝗆 𝗍𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅, 𝖼𝗎𝗌𝗍𝗈𝗆 𝖼𝖺𝗉𝗍𝗂𝗈𝗇, 𝖼𝗎𝗍𝗈𝗆 𝗉𝗋𝖾𝖿𝗂𝗑 𝖺𝗇𝖽 𝗌𝗎𝖿𝖿𝗂𝗑.

<b>𝘕𝘰𝘵𝘦 :</b> 𝘙𝘦𝘯𝘢𝘮𝘪𝘯𝘨 𝘖𝘧 𝘈𝘥𝘶𝘭𝘵 𝘊𝘰𝘯𝘵𝘦𝘯𝘵 𝘐𝘴 𝘚𝘵𝘳𝘪𝘤𝘵𝘭𝘺 𝘗𝘳𝘰𝘩𝘪𝘣𝘪𝘵𝘦𝘥. 𝘐𝘧 𝘠𝘰𝘶 𝘞𝘪𝘭𝘭 𝘋𝘰 𝘠𝘰𝘶 𝘞𝘪𝘭𝘭 𝘎𝘦𝘵 𝘗𝘦𝘳𝘮𝘢𝘯𝘦𝘯𝘵 𝘉𝘢𝘯."""

    ABOUT_TXT = """
<b>❍ ᴍʏ ɴᴀᴍᴇ : https://t.me/Weoo_Rename_Bot
❍ ʜᴏsᴛᴇᴅ ᴏɴ : ᴋᴏʏᴇʙ
❍ ᴅᴀᴛᴀʙᴀsᴇ : ᴍᴏɴɢᴏ ᴅʙ
❍ ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 𝟹
❍ ᴍʏ ᴄʀᴇᴀᴛᴏʀ :t.me/Otakukart7

➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ꜰᴏʀ ɢᴇᴛᴛɪɴɢ ᴍᴏʀᴇ ɪɴꜰᴏ ᴀʙᴏᴜᴛ ᴍᴇ.</b>
"""

    HELP_TXT = """
<b>ʀᴇɴᴀᴍᴇ ʙᴏᴛ ɪꜱ ᴀ ʜᴀɴᴅʏ ᴛᴏᴏʟ ᴛʜᴀᴛ ʜᴇʟᴘꜱ ʏᴏᴜ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ ᴇꜰꜰᴏʀᴛʟᴇꜱꜱʟʏ.

➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ꜰᴏʀ ɢᴇᴛᴛɪɴɢ ᴍᴏʀᴇ ɪɴꜰᴏ.</b>
"""

    THUMBNAIL_TXT = """<b>» <u>ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ</u></b>
    
➲ /start: ꜱᴇɴᴅ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ꜱᴇᴛ ɪᴛ ᴀꜱ ᴀ ᴛʜᴜᴍʙɴᴀɪʟ.
➲ /delthumb: ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ.
➲ /viewthumb: ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.

<b>ɴᴏᴛᴇ :</b> ɪꜰ ɴᴏ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ ɪɴ ʙᴏᴛ ᴛʜᴇɴ, ɪᴛ ᴡɪʟʟ ᴜꜱᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ᴛʜᴇ ᴏʀɪɢɪɴɪᴀʟ ꜰɪʟᴇ ᴛᴏ ꜱᴇᴛ ɪɴ ʀᴇɴᴀᴍᴇᴅ ꜰɪʟᴇ"""

    CAPTION_TXT = """<b>» <u>ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴀɴᴅ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ</u></b>
    
<b>ᴠᴀʀɪᴀʙʟᴇꜱ :</b>         
ꜱɪᴢᴇ: {filesize}
ᴅᴜʀᴀᴛɪᴏɴ: {duration}
ꜰɪʟᴇɴᴀᴍᴇ: {filename}

➲ /set_caption: ᴛᴏ ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.
➲ /see_caption: ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.
➲ /del_caption: ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.

» ᴇx: /set_caption ꜰɪʟᴇ ɴᴀᴍᴇ: {filename}
"""

    PREFIX = """<b>» <u>ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴘʀᴇꜰɪx</u></b>

➲ /set_prefix: ᴛᴏ ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴘʀᴇꜰɪx.
➲ /see_prefix: ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴘʀᴇꜰɪx.
➲ /del_prefix: ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴘʀᴇꜰɪx.

» ᴇx: `/set_prefix @TechifyBots`
"""

    SUFFIX = """<b>» <u>ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ sᴜꜰꜰɪx</u></b>

➲ /set_suffix: ᴛᴏ ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ sᴜꜰꜰɪx.
➲ /see_suffix: ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ sᴜꜰꜰɪx.
➲ /del_suffix: ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ sᴜꜰꜰɪx.

» ᴇx: `/set_suffix @TechifyBots`
"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}

    SEND_METADATA = """🖼️ 𝗛𝗼𝘄 𝗧𝗼 𝗦𝗲𝘁 𝗖𝘂𝘀𝘁𝗼𝗺 𝗠𝗲𝘁𝗮𝗱𝗮𝘁𝗮

For Example :-

<code>By: @Otakukart7</code>

💬 For Help Contact @weoo_animes
"""
