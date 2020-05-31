import discord
from discord.ext import commands

from core import rubbercog, utils
from logic import rng

# Logic (functionality used by features or rubbergoddess directly)
rng = rng.Rng()


class Random(rubbercog.Rubbercog):
    """Pick, flip, roll dice"""

    def __init__(self, bot):
        super().__init__(bot)

    @commands.cooldown(rate=5, per=20.0, type=commands.BucketType.user)
    @commands.command()
    async def pick(self, ctx, *args):
        """"Pick an option"""
        option = rng.pick_option(discord.utils.escape_mentions(" ".join(args)))
        if option:
            await ctx.send("{} {}".format(option, utils.generate_mention(ctx.author.id)))
        await self.roomCheck(ctx)

    @commands.cooldown(rate=5, per=20.0, type=commands.BucketType.user)
    @commands.command()
    async def flip(self, ctx):
        await ctx.send(rng.flip())
        await self.roomCheck(ctx)

    @commands.cooldown(rate=5, per=20.0, type=commands.BucketType.user)
    @commands.command()
    async def roll(self, ctx):
        # TODO: use
        # https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html#basic-converters
        # and only pass integers to the function?
        await ctx.send(rng.generate_number(ctx.message))
        await self.roomCheck(ctx)


def setup(bot):
    bot.add_cog(Random(bot))
