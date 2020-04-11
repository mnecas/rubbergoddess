import requests

import discord
from discord.ext import commands

from core import utils
from config.config import config
from config.messages import Messages as messages


class Name_day(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def svatek(self, ctx):
        url = config.nameday_cz
        res = requests.get(url).json()
        names = []
        for i in res:
            names.append(i["name"])
        await ctx.send(messages.name_day_cz.format(name=", ".join(names)))

    @commands.command()
    async def meniny(self, ctx):
        url = config.nameday_sk
        res = requests.get(url).json()
        names = []
        for i in res:
            names.append(i["name"])
        await ctx.send(messages.name_day_sk.format(name=", ".join(names)))


def setup(bot):
    bot.add_cog(Name_day(bot))
