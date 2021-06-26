from environs import Env

env = Env()
env.read_env()

TOKEN = env.str('TOKEN')
OWNER_IDS = env.list('OWNER_IDS')
PREFIX = "+"
COGS_DIR = "bot/cogs/*.py"

GUILD_ID = 833681226983276594
RESEND_CHANNEL_ID = 833681226983276597

LOG_FILES_DIR = r"data/"
