import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7277077546:AAG-C3bES-fGjxq0I8fs_t-7LaCC4IlwvIo")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23902408"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6a36a4ef2f07d63aeba7b53b99c64d73")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002238449892"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7179837246"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://mex:rex@cluster7.jrzowqz.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "papa1234")

# Put 0 on on that which you don't want to enable
FORCE_CHANNEL = int(os.environ.get("FORCE_CHANNEL", "-1002173795861"))
FORCE_CHANNEL2 = int(os.environ.get("FORCE_CHANNEL2", "-1002044619047"))
REQUEST_CHANNEL = int(os.environ.get("REQUEST_CHANNEL", "-1002150655465"))

#TXT
HELP_TXT = "<b>Hi Dude!\nThis is an file to link bot work for @Alliance_Planet\n\n❏ Bot Cammands\n├/start : start the bot\n├/about : Our Information\n└/help : Help related Bot\n\n💥 Simply click on link and start the bot join both channels and try again thats it.....!\n\n🧑‍💻 Developed by <a href=https://t.me/RarelySukuna>S U K U N A</a></b>"
ABOUT_TXT = "<b><i>About Us..\n\n‣ Made for : @Alliance_Planet\n‣ Owned by : @RarelySukuna\n‣ Maintained by : @RarelySukuna\n‣ Developed by : @RarelySukuna\n\n Adios !!</i></b>"

#PICS
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/b80d277d0cd8d861522fc.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/59e3cb7c12205d4f2a7c4.jpg")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello Baby!!💋❤️ {first}\n\nI am Tsunade a Powerful file store bot⚡️.</b>")
try:
    ADMINS=[7179837246]
    for x in (os.environ.get("ADMINS", "7179837246").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "😐sᴏʀʀʏ ʙᴀʙy💋 ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴄʜᴀɴɴᴇʟ ᴘʟᴇᴀsᴇ😋 ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴡᴀᴛᴄʜ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ ᴩᴏʍ ᴩᴏʍ⚡️🤡.")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ​ - @Anime_X_Hunters"

# Auto-delete configuration
AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "600"))
DEL_MSG = "<b>This message will be deleted automatically in {time}. Forward it to your saved messages..!</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(7179837246)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
