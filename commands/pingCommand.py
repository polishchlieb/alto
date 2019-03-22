from discord.ext.commands import command

@command(pass_context=True)
async def ping(self, ctx):
    await ctx.send(f'Pong! The ping is {self.bot.latency}')