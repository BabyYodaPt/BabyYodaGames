import discord
import os
import time
import asyncio
import random
from discord.ext import commands 
from PIL import Image,ImageFont,ImageDraw
from io import BytesIO

client = commands.Bot(command_prefix = "b/")

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
@client.command()
async def verdade(ctx):
  lista = ['verdadeiro ✅', 'mentira ❌']
  resp = random.choice(lista)
  await ctx.reply(f'O que voce disse é **' + resp + '**')

@client.command()
async def moeda(ctx):
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

@client.command()
async def ping(ctx):
    await ctx.message.add_reaction('🏓')
    await ctx.reply(f'🏓Pong! A Lantecia da API é **{round(client.latency * 1000)}ms**')



@client.command()
async def invite(ctx):
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

@client.command()
async def wanted(ctx, user: discord.Member = None):
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

    
client.run('Nzg5NDk0MTM0NjU4MTcwODgx.X9y3tQ.SIfxRYApyqRE08iDngbA7iUGoOs')