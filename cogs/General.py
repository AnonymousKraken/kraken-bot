import discord
from discord.ext import commands

import yaml


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(member.id, "just joined the server.")
        
        role = discord.utils.get(member.server.roles, name="VERIFY")
        await member.add_roles(member, role)
        
        verifyChannel = [channel for channel in self.bot.get_all_channels() if channel.name == "verify"][0]
        await verifyChannel.send("Welcome! Please enter your name and school.")

    
    @commands.command()
    async def help(self, ctx):

        with open("storage/help.yml", newline="") as helpYaml:
            helpInfo = yaml.safe_load(helpYaml)
        
        for category, info in helpInfo.items():
            embed = discord.Embed(
                colour = discord.Colour.orange(),
                title = category
            )
            for command,description in info.items():
                embed.add_field(name=command, value=description, inline=False)

            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))