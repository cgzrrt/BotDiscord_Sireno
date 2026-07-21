import discord
from discord.ext import commands

# TODO filtro de palabras mejorado
# def message_sent(bot):
#     @bot.event
#     async def on_message(message):
#         if message.author == bot.user:  # para que no se responda a sí mismo
#             return

#         if "mierda" in message.content.lower():
#             await message.delete()
#             await message.channel.send(f"{message.author.mention} no digas eso!!")

#         await bot.process_commands(message)  # obligatorio