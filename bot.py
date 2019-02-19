from discord.ext.commands import Bot
import builtins

bot = Bot(command_prefix = '?')
builtins.bot = bot
token = 'your token'

import commands.randomCommand
import commands.pingCommand
import commands.weatherCommand
import commands.giveawayCommand

import events.readyEvent
import events.messageEvent

from commandErrorHandler import setup
setup(bot)

bot.run(token)
