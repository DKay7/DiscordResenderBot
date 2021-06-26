from discord import TextChannel
from discord import Embed


async def send_messages(parsed_dict, channel: TextChannel):
    datetimes, messages, authors = parsed_dict.values()

    for index, message in enumerate(messages):
        embed = Embed(description=message,
                      timestamp=datetimes[index])
        embed.set_author(name=authors[index])

        await channel.send(embed=embed)
