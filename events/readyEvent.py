from builtins import bot

@bot.event
async def on_ready():
    print('Bot is ready')
    print(f'Running on {len(bot.guilds)} servers')