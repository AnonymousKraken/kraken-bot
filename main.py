import discord
from discord.ext import commands
import asyncio


TOKEN = "Njg3MDA0ODc3OTg5MzQ3NDcz.Xm0O6Q._yxahYZOEjUoTO-U7QBQ604HH3I"


bot = commands.Bot(command_prefix='!')
bot.remove_command("help")


extensions = [
    "cogs.Admin",
    "cogs.General",
    "cogs.Economy",
    "cogs.Misc"]

for ext in extensions:
    bot.load_extension(ext)


@bot.event
async def on_ready():
    print("\nLogged on.\n")


bot.run(TOKEN)