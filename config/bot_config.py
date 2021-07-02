from environs import Env

ENV = Env()
ENV.read_env()

TOKEN = ENV.str('TOKEN')
OWNER_IDS = ENV.list('OWNER_IDS')
PREFIX = "+"
COGS_DIR = "bot/cogs/*.py"

GUILD_ID = 833681226983276594
