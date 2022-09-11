import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from features.city_game import Adventure

load_dotenv()
rp = Adventure()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name="start")
async def check_bot(ctx):
    await ctx.author.send(rp.intro_message())


@bot.command(name="answer")
async def answer(ctx, *, arg):
    if "get" in arg.lower() or "stankiewicz" in arg.lower:
        await ctx.author.send(embed=rp.first_quest())

    else:
        await ctx.send("Jesteś pewien tej odpowiedzi?")


bot.run(TOKEN)
