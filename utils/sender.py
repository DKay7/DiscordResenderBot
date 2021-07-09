from discord import Embed

from config.chat_types import CHAT_COLORS
from utils.location_finder import get_chat_by_location


async def send_messages(parsed_dict, bot):
    """
    Sends messages with given data

    :param parsed_dict: Data which are messages are built of
    :param bot: discord bot which is used to find channel to send messages
    """

    datetimes, chat_types, locations, messages, authors = parsed_dict.values()

    for index, message in enumerate(messages):

        if chat_types[index] not in CHAT_COLORS.keys():
            continue

        color = CHAT_COLORS[chat_types[index]]

        embed = Embed(description=message,
                      timestamp=datetimes[index],
                      color=color)
        embed.set_author(name=authors[index])

        channel = get_chat_by_location(locations[index], bot)

        if channel:
            await channel.send(embed=embed)
