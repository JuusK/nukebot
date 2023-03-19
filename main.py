import discord #Imports the discord module.
from discord.ext import commands #Imports discord extensions.
import config






prefix = "!"
#The below code verifies the "client".
client = commands.Bot(command_prefix=prefix)
#The below code stores the token.
token = config.TOKEN


client.remove_command("help")






@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    activity = discord.Activity(type=discord.ActivityType.watching, name="Your messages")
    await client.change_presence(status=discord.Status.idle, activity=activity)





# Kick
@client.command(name="kick", help="Command to kick user")
async def __kick__(ctx, member: discord.Member, *, reason=None):
    """ command to ban user. Check !help kick """
    try:
        await member.kick(reason=reason)
        await ctx.message.delete()
        await ctx.channel.send(f'{member.name} has been kicked from server, '
                               f'Reason: {reason}')
    except Exception:
        await ctx.channel.send(f"Bot doesn't have enough permission to kick someone. Upgrade the Permissions")

# Ban
@client.command(name="ban", help="Command to ban user")
async def __ban__(ctx, member: discord.Member, *, reason=None):
    """ command to ban user. Check !help ban """
    try:
        await member.ban(reason=reason)
        await ctx.message.delete()
        await ctx.channel.send(f'{member.name} has been banned from server, '
                               f'Reason: {reason}')
    except Exception:
        await ctx.channel.send(f"Bot doesn't have enough permission to ban someone. Upgrade the Permissions")



### MISC ###



#Spam
@client.command(name="spam", help="Spam's a amount of messages")
async def spam(ctx):
    embed = discord.Embed(title="LLLLL", description=f"BEAMED BY YOUR MOM!!")
    while(True):
        await ctx.send(embed=embed)
        
        
#CreateChannel
@client.command(name="channel", help="Spam's a amount of channel's")
async def spam(ctx):
    await ctx.guild.create_text_channel("nuked-by-yourmom")
    




#The below code runs the bot.
client.run(token)
