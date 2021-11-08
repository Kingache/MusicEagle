import os
import aiohttp
from Python_ARQ import ARQ
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
ARQ_API_KEY = getenv("ARQ_API_KEY")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Eagle")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/8628c642a266a22effd8c.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/5dd3d6d64ccd785ae5af2.jpg")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
SUPPORT_GROUP = getenv("GROUP_SUPPORT", "EagleSupport")
PROJECT_NAME = getenv("PROJECT_NAME", "musicXeagle")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "infobotrelax")
# isi dengan username kamu tanpa simbol @
OWNER_NAME = getenv("OWNER_NAME", "Manusiabajingann")
# fill with your nickname
ALIVE_NAME = getenv("ALIVE_NAME", "ᴇᴀɢʟᴇ")
# fill with your id as the owner of the bot
OWNER_ID = int(os.environ.get("OWNER_ID"))
# just fill with True or False (optional)
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "30"))
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $ ?").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
SOURCE_CODE = os.environ.get(
    "SOURCE_CODE", "https://github.com/Kingache/MusicEagle"
)

aiohttpsession = aiohttp.ClientSession()
arq = ARQ("https://thearq.tech", ARQ_API_KEY, aiohttpsession)
