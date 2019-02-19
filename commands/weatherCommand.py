from discord import Embed, Colour
from builtins import bot
from requests import get
from urllib.parse import urlparse

@bot.command(pass_context=True)
async def weather(ctx, country):
    appid = 'your app id'

    url = f'http://api.openweathermap.org/data/2.5/weather?APPID={appid}&units=metric&q='
    response = get(url + urlparse(country).geturl()).json()

    embed = Embed(
        title = f'Weather in {country}',
        colour = Colour.red())

    embed.add_field(
        name = 'Temperature:',
        value = str(response['main']['temp']) + ' °C')
    embed.add_field(
        name = 'Wind speed:',
        value = str(response['wind']['speed']) + ' m/s')

    await ctx.send(embed = embed)
