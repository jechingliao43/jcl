import os
import asyncio
import discord

from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '.', intents = intents)

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def hello(ctx):
    await ctx.send("hello")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot.run(TOKEN)