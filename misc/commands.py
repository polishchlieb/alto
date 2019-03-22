from commands.giveawayCommand import giveaway
from commands.pingCommand import ping
from commands.randomCommand import random
from commands.weatherCommand import weather

from misc.commandErrorHandler import on_command_error

class Commands:
    def __init__(self, bot):
        self.bot = bot

def setupCommands(bot):
    Commands.giveaway = giveaway
    Commands.ping = ping
    Commands.random = random
    Commands.weather = weather

    Commands.on_command_error = on_command_error

    bot.add_cog(Commands(bot))