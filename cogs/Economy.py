import discord
from discord.ext import commands
import sql


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''
    @commands.command()
    async def economy(self, ctx):

    @commands.command()
    async def steal(self, ctx, user, amount):
    '''

    @commands.command(aliases=["bal"])
    async def balance(self, ctx, mention=None):
        c = await sql.getCurrency()

        if mention == None:
            user = ctx.author
        else:
            user = ctx.message.mentions[0]

        money = str(await sql.getUserMoney(user.id))
        income = str(await sql.getUserIncome(user.id))
        if income == "None": 
            income = "NOT REGISTERED: 0"

        embed = discord.Embed(
            colour = discord.Colour.green()
        )

        embed.set_author(name=f"{user.name}'s Balance")
        embed.add_field(name="Money", value=money+c, inline=False)
        embed.add_field(name="Income", value=income+c, inline=False)

        await ctx.send("",embed=embed)


    @commands.has_any_role("Administrator")
    @commands.command()
    async def givemoney(self, ctx, mention, amount):
        c = await sql.getCurrency()
        users = ctx.message.mentions

        if len(users) < 1:
            await ctx.send("Please mention a valid user.")
        else:
            for user in users:
                await sql.addUserMoney(int(user.id), int(amount))
                await ctx.send(f"Gave {user.name} {amount+c}.")

    
    @commands.has_any_role("Administrator")
    @commands.command()
    async def setmoney(self, ctx, mention, amount):
        c = await sql.getCurrency()
        users = ctx.message.mentions

        if len(users) < 1:
            await ctx.send("Please mention a valid user.")
        else:
            for user in users:
                await sql.setUserMoney(int(user.id), str(amount))
                await ctx.send(f"Set {user.name}\'s balance to {amount+c}.")


    @commands.has_any_role("Administrator")
    @commands.command()
    async def fixmoney(self, ctx):
        
        users = self.bot.get_all_members()
        ids = [user.id for user in users
            if "Bot" not in [role.name for role in user.roles]]

        newUsers = 0

        for id in ids:
            if not await sql.userExists(id):
                await sql.createUser(id)
                newUsers += 1

        await ctx.send("Added " + str(newUsers) + " new users to the database.")

        # await ctx.send("Restarted the economy.")



def setup(bot):
    bot.add_cog(Economy(bot))