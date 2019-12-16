import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'm!')
game = discord.Game("in the market")

@client.event
async def on_ready():
    print ('Bot is ready.')
    await client.change_presence(activity=game)

@client.command()
async def bothelp(ctx):
    embed = discord.Embed(
        title = 'Command List',
        value = 'See below a list of commands to help you get used to running me!',
        colour = discord.Colour.blue()
    )
    embed.add_field(name = 'm!bothelp', value = 'Displays this list.\n')
    embed.add_field(name = 'm!kick', value = 'Kicks a member. (Senior Manager+ only!)\n')
    embed.add_field(name = 'm!invite', value = 'Displays an invite for the server.\n')
    embed.add_field(name = 'm!invite', value = 'Displays an invite for the IRF Discord.\n')

    await ctx.send(embed=embed)


client.run('NjU1MDI0Mzg2NTIwMjUyNDM2.XfOFCg.d7HYawhHcM_utrY29mmcIhuW43s')
