from discord.ext.commands import Bot
from matplotlib.path import Path
from config.location_config import LOCATION_CHATS


def get_chat_by_location(location, bot: Bot):
    for region, channel_id in LOCATION_CHATS:
        region_path = Path(region)

        if region_path.contains_point(location):
            channel = bot.get_channel(channel_id)

            return channel

    return bot.resend_channel
