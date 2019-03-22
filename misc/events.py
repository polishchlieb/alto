from events.messageEvent import on_message
from events.readyEvent import on_ready

class Events:
    def __init__(self, bot):
        self.bot = bot

def setupEvents(bot):
    Events.on_message = on_message
    Events.on_ready = on_ready

    bot.add_cog(Events(bot))