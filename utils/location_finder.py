from discord.ext.commands import Bot
from matplotlib.path import Path

from config.location_config import LOCATION_CHATS
from config.parser_config import SEND_DEFAULTS

def get_chat_by_location(location, bot: Bot):
    """
    Finds which ingame location the given got belongs.

    :param location: Given dot coordinates
    :param bot: discord bot which is used to find channel to send messages
    :return: Channel for specific ingame location
    """
    for region, channel_id in LOCATION_CHATS:
        region_path = Path(region)

        if region_path.contains_point(location):
            channel = bot.get_channel(channel_id)

            return channel

    if SEND_DEFAULTS:
        return bot.resend_channel
