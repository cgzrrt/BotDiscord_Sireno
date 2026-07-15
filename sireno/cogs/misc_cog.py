import logging
import discord
from discord.ext import commands
import random

logger = logging.getLogger(__name__)

class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # Tirar dados
    @commands.command()
    async def coms(self, ctx):
        """Muestra una lista de todos los comandos"""
        embed = discord.Embed(
            title='Comandos de sireno `s!`',
            description="""**Comandos de gestión:**\n
                        `s!ban`, `s!kick`, `s!purge`, `s!darRol`, `s!quitarRol`\n
                        **Comandos divertidos**\n
                        `s!dado`, `s!caracola`, `s!encuesta`, `s!rate`, `s!say`, `s!hola`"""
        )
        await ctx.reply(embed=embed)
    
# Añadir al cog
async def setup(bot: commands.Bot):
    await bot.add_cog(MiscCog(bot))