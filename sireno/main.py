import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

from events import startEvents

# Discord setup
load_dotenv() # carga el .env 
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Crear el bot
bot = commands.Bot(command_prefix='s!', intents=intents) # el prefijo usado será s!

# *** Eventos
startEvents(bot)

# Say hello
@bot.command()
async def hello(ctx): # s!hello
    await ctx.send(f"Hola {ctx.author.mention}!")

# Secret command 
@bot.command()
@commands.has_role("PSOE")
async def secret(ctx):
    await ctx.send("Rojo")
@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("no tienes permiso")

# Enviar DM
async def dm(ctx, *, msg):
    await ctx.author.send(f"You said {msg}")


# *** Run
bot.run(token, log_handler=handler)   