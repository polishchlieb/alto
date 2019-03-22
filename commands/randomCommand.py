from discord.ext.commands import command
from random import randint

@command(pass_context=True)
async def random(self, ctx):
    await ctx.send(randint(1, 100))