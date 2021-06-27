import os
from discord.ext import tasks
from discord.ext.commands import Cog

from config.bot_config import LOG_FILES_DIR
from utils.parser import parse_file
from utils.sender import send_messages


class TransitionCog(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.known_files = os.listdir(LOG_FILES_DIR)

        self.check_new_files.start()

    @tasks.loop(seconds=1)
    async def check_new_files(self):

        new_files_list = os.listdir(LOG_FILES_DIR)

        for file in new_files_list:
            if file not in self.known_files:
                self.known_files.append(file)
                result_dict = parse_file(os.path.join(r"data/", file))

                print("New file", file)
                print(result_dict)

                await send_messages(result_dict, self.bot)


def setup(bot):
    bot.add_cog(TransitionCog(bot))
