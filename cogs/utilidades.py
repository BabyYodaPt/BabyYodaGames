import discord
import asyncio
import time
from discord.ext import commands


class Utilidades(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self, ctx):
        embedinvite = discord.Embed(
        title="Me convide para o seu servidor",
        description='[Clique aqui para me convidar](https://discord.com/oauth2/authorize?client_id=789494134658170881&scope=bot&permissions=8)',
        colour=discord.Colour(0x33DDFF),
        )
        embedinvite.set_image(
        url="https://media1.tenor.com/images/df38c174a2becc894086b1fd913d3adb/tenor.gif"
        )
        embedinvite.set_footer(
            text=f"Solicitado por {ctx.author.name}",
            icon_url=f"{ctx.author.avatar_url}")
        await ctx.reply(
        embed=embedinvite,
        )
    @commands.command()
    async def ping(self, ctx):
        pong = await ctx.send('Calculando o ping...') 
        init_time = int(round(time.time() * 1000))
        await pong.edit(content='Calculando o ping...') 
        ping = int(round(time.time() * 1000)) - init_time 
        await pong.edit(content=f'O ping da API é **{ping}ms**') 


def setup(client):
    client.add_cog(Utilidades(client))
