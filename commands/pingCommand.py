from discord.ext import commands
from builtins import bot

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send(f'Pong! The ping is {bot.latency}')