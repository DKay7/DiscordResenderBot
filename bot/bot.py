from config.bot_config import TOKEN, OWNER_IDS, PREFIX, COGS_DIR, GUILD_ID, RESEND_CHANNEL_ID

from discord.ext.commands import Bot as BaseBot
from os.path import splitext, basename
from discord import Intents
from glob import glob


class Bot(BaseBot):
    def __init__(self):
        self.PREFIX = PREFIX
        self.TOKEN = TOKEN
        self.OWNER_IDS = OWNER_IDS

        self.guild = None
        self.resend_channel = None

        self.ready = False
        intents = Intents().all()

        super(Bot, self).__init__(command_prefix=self.PREFIX, owner_ids=self.OWNER_IDS, intents=intents)

    async def on_ready(self):
        if not self.ready:
            self.guild = self.get_guild(GUILD_ID)
            self.resend_channel = self.guild.get_channel(RESEND_CHANNEL_ID)

            print(f'Logged in as {self.user}')
            self.ready = True

        else:
            print(f'RE-Logged in as {self.user}')

    async def on_error(self, err, *args, **kwargs):
        if args and hasattr(args[0], "send"):
            await args[0].send("Возникла ошибка")
        raise

    def _setup(self):
        cogs = [splitext(basename(path))[0] for path in glob(COGS_DIR)]

        for cog in cogs:
            self.load_extension(f"bot.cogs.{cog}")

    def run(self, *args, **kwargs):
        self._setup()
        super().run(self.TOKEN, reconnect=True)

    @staticmethod
    async def on_connect():
        print("Bot connected")

    @staticmethod
    async def on_disconnect():
        print("Bot disconnected")
