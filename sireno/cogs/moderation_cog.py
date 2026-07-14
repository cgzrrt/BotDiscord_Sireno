import logging

logger = logging.getLogger(__name__)

import discord
from discord.ext import commands

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Elimina n mensajes en un canal, reason=razon por la que se eliminan
    @commands.hybrid_command(name="purge", help="Borra N mensajes")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, n: int, reason: str | None = "No se dio razón"):
        await ctx.defer()
        
        await ctx.channel.purge(limit=n+1, reason=reason)
        await ctx.send(f'Se borraron {n} mensajes por: {reason}')
    
    # Expulsa a un miembro sin banearlo
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kickMember(self, ctx, member: discord.Member, reason: str | None = "No se dio razón"):
        await member.kick(reason=reason)
        await ctx.send(f'El usuario {member} ha sido expulsado')
    @kickMember.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes los permisos para hacer esto :)")

# Añadir al cog
async def setup(bot: commands.Bot):
    await bot.add_cog(ModerationCog(bot))