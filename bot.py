from discord.ext.commands import Bot

from misc.events import setupEvents
from misc.commands import setupCommands

bot = Bot(command_prefix = '?')
token = 'your token'

setupEvents(bot)
setupCommands(bot)

bot.run(token)