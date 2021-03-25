import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = "b/")


for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('token')