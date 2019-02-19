# https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612

import traceback
import sys
from discord.ext import commands

class CommandErrorHandler:
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        
        ignored = (commands.CommandNotFound, commands.UserInputError)
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return await ctx.message.add_reaction('❓')
                

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))