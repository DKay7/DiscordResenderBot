from discord import Embed
from config.chat_types import CHAT_COLORS
from utils.location_finder import get_chat_by_location


async def send_messages(parsed_dict, bot):
    datetimes, chat_types, locations, messages, authors = parsed_dict.values()

    for index, message in enumerate(messages):
        color = CHAT_COLORS.get(chat_types[index], 0x000000)

        embed = Embed(description=message,
                      timestamp=datetimes[index],
                      color=color)
        embed.set_author(name=authors[index])

        channel = get_chat_by_location(locations[index], bot)
        await channel.send(embed=embed)
