from discord.ext import commands

async def on_command_error(self, ctx, error):
    if hasattr(ctx.command, 'on_error'):
        return
    
    ignored = (commands.CommandNotFound, commands.UserInputError)
    error = getattr(error, 'original', error)

    if isinstance(error, ignored):
        await ctx.message.add_reaction('❓')