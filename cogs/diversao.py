import discord
import random
import asyncio
from discord.ext import commands
from PIL import Image,ImageFont,ImageDraw
from io import BytesIO


class Diversão(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def moeda(self, ctx):
        list = ['Cara', 'Coroa']
        res = random.choice(list)
        embedmoeda = discord.Embed(
        title="<a:coinflip:823964309776105492>Moeda<a:coinflip:823964309776105492>",
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
        title="<a:coinflip:823964309776105492>Moeda<a:coinflip:823964309776105492>",
        description='A moeda girou e calhou **' + res + '**',
        colour=discord.Colour(0x33DDFF),
        )
        embedmoeda1.set_footer(
            text=f"Solicitado por {ctx.author.name}",
            icon_url=f"{ctx.author.avatar_url}")
        msg = await ctx.reply(embed=embedmoeda)
        await asyncio.sleep(3.0)
        await msg.edit(embed=embedmoeda1)

    @commands.command()
    async def wanted(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        wanted = Image.open("./img/wantedtemp.jpg")
        asset = user.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((177,177))
        wanted.paste(pfp, (120,212))
        wanted.save("wanted.jpg")
        await ctx.send(file = discord.File("wanted.jpg"))
    
    @commands.command()
    async def verdade(self, ctx):
        lista = ['verdadeiro ✅', 'mentira ❌']
        resp = random.choice(lista)
        await ctx.reply(f'O que voce disse é **' + resp + '**')
    
    
def setup(client):
    client.add_cog(Diversão(client))

