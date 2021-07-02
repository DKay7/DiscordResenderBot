from discord.ext.commands import Cog
from discord.ext import tasks

from utils.parser import parse_file_content, get_last_file_path
from utils.sender import send_messages


class TransitionCog(Cog):
    def __init__(self, bot):
        """
        Initialize class TransitionCog
        :param bot: discord.ext.commands.Bot object
        """

        self.bot = bot
        self.file = None
        self.last_filename = None
        self.file_bytes_position = 0

        self.check_and_read_new_files.start()

    @tasks.loop(seconds=1)
    async def check_and_read_new_files(self):
        """
        Method which continuously checks if is there a
        new file or are there new data in existing file.
        If there are some new data method parses it
        and sends messages with it
        """

        file_path = get_last_file_path()

        if file_path != self.last_filename:

            if self.file:
                self.file.close()

            self.file = open(file_path, mode="r", encoding="cp1251")
            self.file_bytes_position = 0
            self.last_filename = file_path

        self.file.seek(self.file_bytes_position)
        content = self.file.read()
        self.file_bytes_position = self.file.tell()

        if content:
            result_dict = parse_file_content(content)
            await send_messages(result_dict, self.bot)

    @check_and_read_new_files.before_loop
    async def before_check_new_files(self):
        """
        Called before "check_and_read_new_files"
        and waiting for discord.bot to becomes ready to work.
        """
        print('Bot is starting...')
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(TransitionCog(bot))
