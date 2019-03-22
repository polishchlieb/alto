from discord import DMChannel

async def on_message(self, message):
    if isinstance(message.channel, DMChannel):
        return await message.channel.send('Don\'t dm me ;)')