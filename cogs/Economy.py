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

        income = 0
        for role in user.roles:
            if role.id in await sql.getJobIds():
                income += await sql.getJobIncome(role.id)
        if income == 0: 
            income = "NOT REGISTERED: 0"
        else: 
            income = str(income)

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
                await ctx.send(f"Gave <@{user.id}> {amount+c}.")

    
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
                await ctx.send(f"Set <@{user.name}>\'s balance to {amount+c}.")


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


    @commands.command()  
    async def shop(self, ctx, detail=None):
        c = await sql.getCurrency()
        categories = await sql.getShopCategories()
        items = await sql.getShopItems()

        if detail == None:
            embed = discord.Embed(
                colour = discord.Colour.purple(),
                title = "Shop"
            )

            for category in categories:
                itemStr = "\n".join(await sql.getShopItems(category))
                embed.add_field(name="**"+category+"**", value=itemStr, inline=False)

            await ctx.send(embed=embed)


        elif detail[0] == "$":
            category = detail[1:].title()

            if category not in categories:
                await ctx.send("Category not found.")
            
            else:

                embed = discord.Embed(
                    colour = discord.Colour.purple(),
                    title = category
                )

                for item in await sql.getShopItems(category):
                    description = await sql.getItemDescription(item)

                    embed.add_field(name=item, value=description, inline=False)

                await ctx.send(embed=embed)
            
        else:
            item = detail.title()
            if item not in items:
                await ctx.send("Item not found.")
            else:
                embed = discord.Embed(
                    colour = discord.Colour.purple(),
                    title = item
                )

                embed.add_field(name="**Category**", value=await sql.getItemCategory(item), inline=False)
                embed.add_field(name="**Description**", value=await sql.getItemDescription(item), inline=False)
                embed.add_field(name="**Price**", value=str(await sql.getItemPrice(item))+c, inline=False)

                await ctx.send("",embed=embed)

    @commands.command()
    async def buy(self, ctx, item, quanity=1):
        pass

def setup(bot):
    bot.add_cog(Economy(bot))