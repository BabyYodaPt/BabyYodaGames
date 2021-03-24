import discord
import random
import asyncio
from discord.ext import commands


class Diverso(commands.Cog):
    def __init__(self, client):
        self.client = client

@commands.command()
async def test(self, ctx):
    list = ['Cara', 'Coroa']
    res = random.choice(list)
    embedmoeda = discord.Embed(
    title="<a:coinflip:823964309776105492>Moeda<a:coinflip:823958659414884392>",
    description='A moeda está girando',
    colour=discord.Colour(0x33DDFF),
    )
    embedmoeda.set_image(
    url="https://img.fireden.net/co/image/1465/92/1465929727447.gif"
    )
    embedmoeda.set_footer(
        text=f"Solicitado por {ctx.author.name}",
        icon_url=f"{ctx.author.avatar_url}")
    embedmoeda1 = discord.Embed(
    title="<a:coinflip:823964309776105492>Moeda<a:coinflip:823958659414884392>",
    description='A moeda girou e calhou **' + res + '**',
    colour=discord.Colour(0x33DDFF),
    )
    embedmoeda1.set_footer(
        text=f"Solicitado por {ctx.author.name}",
        icon_url=f"{ctx.author.avatar_url}")
    msg = await ctx.reply(embed=embedmoeda)
    await asyncio.sleep(3.0)
    await msg.edit(embed=embedmoeda1)
    

def setup(client):
    client.add_cog(Diverso(client))

