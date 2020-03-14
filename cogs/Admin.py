import discord
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def execute(self, ctx, cmd):
        await exec(cmd)



def setup(bot):
    bot.add_cog(Admin(bot))