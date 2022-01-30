import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('bots online')

@bot.command()
async def sarah(ctx):
    await ctx.send("Coucou t'as faim ?", file=discord.File('sarah2.png'))

@bot.command()
async def elon(ctx):
    await ctx.send(file=discord.File('elon_v2.png'))
    await ctx.send(file=discord.File('elonito.mp4'))

bot.run(TOKEN)
