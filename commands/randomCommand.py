from discord.ext import commands
from builtins import bot
from random import randint

@bot.command(pass_context=True)
async def random(ctx):
    await ctx.send(randint(1, 100))