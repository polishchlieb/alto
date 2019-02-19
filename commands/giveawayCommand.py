# not tested, but probably works xD

from builtins import bot
from threading import Timer
from discord import Embed
from random import choice

def id_get(member):
    return member.user.id

@bot.command(pass_context=True)
async def giveaway(ctx, time: str, *item):
    if not time.isdigit():
        return await ctx.send('Use: `?giveaway (time in minutes) (item)`')

    itemBuilder = []
    for arg in item:
        itemBuilder.append(arg)

    embed = Embed(
        title = 'Giveaway',
        color = 'red',
        description = ' '.join(itemBuilder))

    msg = await ctx.send(embed)
    msg.add_reaction('🎉')

    def check():
        reacted = [reaction for reaction in msg.reactions if reaction.emoji is '🎉'][0].users().flatten()
        # winner can't be our bot and must be in the guild
        pps = [user for user in reacted if user.id is not bot.user.id and user.id in map(id_get, iter(ctx.guild.members))]
        winner = choice(pps)
        msg.send_message(f'{winner.mention} won the giveaway!')

    t = Timer(int(time), check)
    t.run()