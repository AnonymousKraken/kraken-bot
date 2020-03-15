import discord
from discord.ext import commands

import sql


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_any_role("Administrator")
    @commands.command()
    async def execute(self, ctx, cmd):
        await exec(cmd)

    @commands.has_any_role("Administrator")
    @commands.command()
    async def sql(self, ctx, cmd):
        await sql.execute(cmd)



def setup(bot):
    bot.add_cog(Admin(bot))