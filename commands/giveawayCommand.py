from threading import Timer
from discord import Embed
from random import choice
from discord.ext.commands import command

def get_id(member):
    return member.user.id

@command(pass_context=True)
async def giveaway(self, ctx, time: str, *item):
    if not time.isdigit():
        return await ctx.send('Use: `?giveaway (time in minutes) (item)`')

    embed = Embed(
        title = 'Giveaway',
        color = 'red',
        description = ' '.join(item))
    msg = await ctx.send(embed)
    msg.add_reaction('🎉')

    def check():
        reacted = [reaction for reaction in msg.reactions if reaction.emoji is '🎉'][0].users().flatten()
        pps = [user for user in reacted if user.id is not self.bot.user.id and user.id in map(get_id, iter(ctx.guild.members))]
        winner = choice(pps)
        msg.send_message(f'{winner.mention} won the giveaway!')

    t = Timer(int(time), check)
    t.run()