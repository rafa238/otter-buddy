import os

SERVER_INVITE = "https://discord.gg/dATz7vwbN2"
BOT_INVITE = "https://discord.com/api/oauth2/authorize?client_id=796548435825393674&permissions=2550656064&scope=bot"
GITHUB_LINK = "https://github.com/Proyecto-Nutria/otter-buddy"

OTTER_ADMIN = os.environ.get('OTTER_ADMIN', 'Admin')
OTTER_MODERATOR = os.environ.get('OTTER_MODERATOR', 'Moderator')
OTTER_ROLE = os.environ.get('OTTER_ROLE', 'Interviewee')

LOGS_DIR = 'logs'

LOG_FILE_PATH = os.path.join(LOGS_DIR, 'otter-buddy.log')

ALL_DIRS = (attrib_value for attrib_name, attrib_value in list(globals().items())
            if attrib_name.endswith('DIR'))

PREFIX = "&"
BRAND_COLOR = 0x0099A2
