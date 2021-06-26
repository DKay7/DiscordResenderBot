from environs import Env

env = Env()
env.read_env()

TOKEN = env.str('TOKEN')
OWNER_IDS = env.list('OWNER_IDS')
PREFIX = "+"
COGS_DIR = "bot/cogs/*.py"
