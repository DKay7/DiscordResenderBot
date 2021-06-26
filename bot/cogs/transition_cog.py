import os
from discord.ext import tasks
from discord.ext.commands import Cog
from utils.parser import parse_file


class TransitionCog(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.known_files = os.listdir(r"data/")

        self.check_new_files.start()

    @tasks.loop(seconds=1)
    async def check_new_files(self):

        new_files_list = os.listdir(r"data/")

        for file in new_files_list:
            if file not in self.known_files:
                self.known_files.append(file)
                print("New file", file)
                result_dict = parse_file(os.path.join(r"data/", file))
                print(result_dict)


def setup(bot):
    bot.add_cog(TransitionCog(bot))
