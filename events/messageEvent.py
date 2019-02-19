from builtins import bot
from discord import DMChannel

@bot.event
async def on_message(message):
    if isinstance(message.channel, DMChannel):
        return await message.channel.send('Don\'t dm me ;)')

    await bot.process_commands(message)