import logging
import discord
from discord.ext import commands
import random

logger = logging.getLogger(__name__)

import discord
from discord.ext import commands

respuestasCaracola = [
    'Sí',
    'No',
    'Depende del punto de vista',
    'Prueba preguntando de nuevo',
    '¿Realmente quieres saber la respuesta?',
    'Tal vez',
    'Solo si vuelve el dab',
]

class FunCog(commands.Cog):
    
    
    def __init__(self, bot):
        self.bot = bot
        
    # Tirar dados
    @commands.command()
    async def dado(self, ctx, dado: str):
        """Lanza un dado en formato NdN."""
        try:
            rolls, limit = map(int, dado.split('d'))
        except Exception:
            await ctx.reply('El formato tiene que ser NdN!')
        
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.reply(f'Ha salido: {result}')
    
    # Caracola mágica
    @commands.command()
    async def caracola(self, ctx, *, pregunta: str):
        """Hazle una pregunta de sí/no a la caracola mágica"""
        if not pregunta:
            await ctx.reply('¡Tienes que preguntar algo!')
            return
        respuesta = respuestasCaracola[random.randint(0, len(respuestasCaracola)-1)]
        await ctx.reply(embed=discord.Embed(colour=4, title=pregunta, description=respuesta))
        
    # Crear embed/encuesta
    @commands.command()
    async def encuesta(self, ctx, *, pregunta):
        """Encuesta de sí/no"""
        embed = discord.Embed(title="Nueva encuesta", description=pregunta)
        poll_message = await ctx.send(embed=embed)
        await poll_message.add_reaction("👍")
        await poll_message.add_reaction("👎")
    
    # Puntuar
    @commands.command()
    async def rate(self, ctx, *, pregunta):
        """Puntúa algo del 0 al 100"""
        if not pregunta:
            await ctx.reply('¡Tienes que darme algo para valorar!')
            return
        respuesta = random.randint(0, 100)
        embed = discord.Embed(colour=0, title='[0/100] Le doy una puntuación de...', description=respuesta)
        await ctx.reply(embed=embed)
        


# Añadir al cog
async def setup(bot: commands.Bot):
    await bot.add_cog(FunCog(bot))