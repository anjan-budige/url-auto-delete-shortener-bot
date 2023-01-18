import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#Port
PORT = environ.get("PORT", "8080")



# Bot information
SESSION = 'Media_search'
API_ID = '15914139'
API_HASH = 'f5c54e1dd806604552e211b3841c1ad4'
BOT_TOKEN = "5635079039:AAFulnoUbDmBtTyHcMYwTbvTAQw5EsABE3Q"

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False
PICS = 'https://telegra.ph/file/f6fee6f859480e971483a.jpg https://telegra.ph/file/3678dcf40bc9bfed7b79e.jpg https://telegra.ph/file/29f9e03617cd9918c968b.jpg https://telegra.ph/file/0fa2ae936f1ae8944d67c.jpg https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg'.split()

# Admins, Channels & Users
ADMINS = 1121140181
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001313414450').split()]

auth_users = None
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = "-1001539945987"
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = "-1001539945987"
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = "mongodb+srv://enrich:enrich@cluster0.mhghl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
DATABASE_NAME = "M4uVideo_bot"
COLLECTION_NAME = 'Telegram_files'

# others
LOG_CHANNEL = "-1001313414450"
SUPPORT_CHAT = "ml_contact_bot"
P_TTI_SHOW_OFF = True
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = True
CUSTOM_FILE_CAPTION = "ɴᴀᴍᴇ: <code>{file_name}</code> \n\nᴊᴏɪɴ ɴᴏᴡ: [Unique Coders](https://t.me/unique_coders_x)</b>"
BATCH_FILE_CAPTION = "ɴᴀᴍᴇ: <code>{file_name}</code> \n\nᴊᴏɪɴ ɴᴏᴡ: [Unique Coders](https://t.me/unique_coders_x)</b>"
IMDB_TEMPLATE = "🧿 ᴛɪᴛᴛʟᴇ :  {title} \n🌟 ʀᴀᴛɪɴɢ : {rating} \n🎭 ɢᴇɴʀᴇ : {genres} \n📆 ʀᴇʟᴇᴀsᴇ : {year} \n⏰ ᴅᴜʀᴀᴛɪᴏɴ : {runtime} \n🎙️ʟᴀɴɢᴜᴀɢᴇ : {languages} \n🔖 sʜᴏʀᴛ : {plot} \n★ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @unique_coders_x"
LONG_IMDB_DESCRIPTION = False
SPELL_CHECK_REPLY = True
MAX_LIST_ELM = None
INDEX_REQ_CHANNEL = '-1001313414450'
FILE_STORE_CHANNEL = '-1001313414450'
MELCOW_NEW_USERS = True
PROTECT_CONTENT = False
PUBLIC_FILE_STORE = True

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

## EXTRA FEATURES ##
    
      # URL Shortener #

URL_SHORTENR_WEBSITE = 'linksearn.site'
URL_SHORTNER_WEBSITE_API = '8b088f1bec72e5db45502b832a1116b99e11e876'

     # Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = 300
SELF_DELETE = False
if SELF_DELETE == "True":
    SELF_DELETE = True

    # Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/unique_coders_x"

   # Custom Caption Under Button #
CAPTION_BUTTON = "Join"
CAPTION_BUTTON_URL = "https://t.me/unique_coders_x"

   # Auto Delete For Bot Sending Files #
