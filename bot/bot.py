from datetime import datetime
from glob import glob
from os.path import splitext, basename

from discord.ext.commands import Bot as BaseBot
from discord import Intents

from config.bot_config import TOKEN, OWNER_IDS, PREFIX, COGS_DIR, GUILD_ID, HEART_BEAT_TIMEOUT
from config.parser_config import DEFAULT_RESEND_CHANNEL_ID


class Bot(BaseBot):
    def __init__(self):
        """
        Initializes Bot class
        """

        self.PREFIX = PREFIX
        self.TOKEN = TOKEN
        self.OWNER_IDS = OWNER_IDS

        self.guild = None
        self.resend_channel = None

        self.ready = False
        intents = Intents().all()

        super(Bot, self).__init__(command_prefix=self.PREFIX,
                                  owner_ids=self.OWNER_IDS,
                                  intents=intents,
                                  heartbeat_timeout=HEART_BEAT_TIMEOUT)

    async def on_ready(self):
        """
        Running while bot is getting ready
        """

        if not self.ready:
            self.guild = self.get_guild(GUILD_ID)
            self.resend_channel = self.guild.get_channel(DEFAULT_RESEND_CHANNEL_ID)

            print(f'Logged in as {self.user}')
            self.ready = True

        else:
            print(f'RE-Logged in as {self.user}')

    def _setup(self):
        """
        Setups bot's command groups (Cogs)
        """

        cogs = [splitext(basename(path))[0] for path in glob(COGS_DIR)]

        for cog in cogs:
            self.load_extension(f"bot.cogs.{cog}")

    def run(self, *args, **kwargs):
        """
        Runs the bot
        """
        self._setup()
        super().run(self.TOKEN, reconnect=True)

    @staticmethod
    async def on_connect():
        """
        Called when bot is connected
        """
        print("Bot connected")

    @staticmethod
    async def on_disconnect():
        """
        Called when bot is disconnected
        """
        print(f"Bot disconnected {datetime.now()}")
