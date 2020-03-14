import discord
from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ping(self, ctx, description="returns ping of bot"):
        latency = self.bot.latency * 1000
        await ctx.send("Responding with ping of " + str(round(latency, 2)) + "ms.")


def setup(bot):
    bot.add_cog(Misc(bot))