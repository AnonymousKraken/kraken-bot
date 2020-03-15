import discord
from discord.ext import commands

import yaml, sql


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(member.name, "just joined the server.")
        
        mainChannel = self.bot.get_channel(688057033886662770)
        jobChannel = self.bot.get_channel(688067828242448428)
        
        await mainChannel.send(f"Welcome to the UAPR, <@{member.id}>!")
        await jobChannel.send("Welcome! You can sign up for a job here.")
    
        if not await sql.userExists(member.id):
            await sql.createUser(member.id)

    
    @commands.command()
    async def help(self, ctx, command=None):


        def getCommand(helpInfo, cmd):
            for name,command in helpInfo["commands"].items():
                if cmd == command["name"] or cmd in command["aliases"]:
                    return command
                    
            return None


        with open("storage/help.yaml", newline="") as helpYaml:
            helpInfo = yaml.safe_load(helpYaml)
        

        if command == None:
            embed = discord.Embed(
                colour = discord.Colour.orange(),
                title = "Help"
            )

            for category, cmds in helpInfo["categories"].items():

                commandList = []
                for cmd in cmds:
                    if helpInfo["commands"][cmd]["perms"] == "Administrator":
                        commandList.append("* " + cmd)
                    else:
                        commandList.append("- " + cmd)
                
                commandStr = "\n".join(commandList)
                embed.add_field(name="**"+category+"**", value=commandStr, inline=False)

            await ctx.send("",embed=embed)


        else:
            cmdInfo = getCommand(helpInfo, command)

            if cmdInfo == None:
                await ctx.send(f"Command {command} not found.")
            
            else:
                embed = discord.Embed(
                    colour = discord.Colour.orange(),
                    title = cmdInfo["name"]
                )

                embed.add_field(name="**Description**", value=cmdInfo["description"], inline=False)
                embed.add_field(name="**Usage**", value="!"+cmdInfo["usage"], inline=False)
                embed.add_field(name="**Aliases**", value=", ".join(cmdInfo["aliases"]), inline=False)
                embed.add_field(name="**Permissions**", value=cmdInfo["perms"], inline=False)

                await ctx.send("",embed=embed)


    @commands.has_any_role("Administrator")
    @commands.command()
    async def purge(self, ctx, amount=None):
        if amount != None:
            deleted = await ctx.channel.purge(limit=int(amount)+1)
        else:
            deleted = await ctx.channel.purge()
        await ctx.send(f'<@{ctx.author.id}> deleted {len(deleted)-1} message(s)')




def setup(bot):
    bot.add_cog(General(bot)) 