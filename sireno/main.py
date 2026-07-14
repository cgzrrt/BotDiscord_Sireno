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

# *** Comandos

# Say hello
@bot.command()
async def hello(ctx): # s!hello
    await ctx.send(f"Hola {ctx.author.mention}!")

# Añadir rol
@bot.command()
async def assign(ctx): # el rol debe estar debajo del rol del bot
    role = discord.utils.get(ctx.guild.roles, name="PSOE")
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} ahora tiene el rol PSOE")
    else:
        await ctx.send("El rol no existe")

# Eliminar rol
@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name="PSOE")
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} ya no tiene el rol PSOE")
    else:
        await ctx.send("El rol no existe")

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

# Respuesta directa a comando
@bot.command()
async def reply(ctx):
    await ctx.reply("esta es una respuesta a tu mensaje")
    
# Crear embed/encuesta
@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="New poll", description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")

# *** Run
bot.run(token, log_handler=handler)   