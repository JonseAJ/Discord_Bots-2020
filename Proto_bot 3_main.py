This bot created by Jonse and is the prototype of the first bot(Ultimate bot)
This bot may not be upgraded or further improved, because it is just a prototype of the first bot!
The 1st bot(Ultimate bot) and the 2nd bot(Friendly bot) will definitely be further improved with more features! 


import discord
from discord.ext import commands
#import random 
#import asyncio 
#from discord import Embed 
#import datetime
#import youtube_dl  
import keep_alive



#command prefix
bot = commands.Bot(command_prefix = '$')

#when Bot is ready
@bot.event
async def on_ready():
    print("Command Bot is ready")
    print(bot.user)


#clear command
@bot.command(pass_text=True)
@commands.has_permissions(manage_messages=True) 
async def clear(ctx, amount=1):   
	embed = discord.Embed(
	    title=f"{ctx.author.name} cleared: {ctx.channel.name}",
	    description=f"{amount} messages were cleared",
	    colour=discord.Colour.orange())
	await ctx.channel.purge(limit=amount + 1)
	await ctx.send(embed=embed)


#kick command
@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'kicked {member.mention}')

#ban command
@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
   await member.ban(reason=reason)
   await ctx.send(f' Banned {member.mention}')


#unban command
@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()  
    member_name, member_descriminator = member.split('#')  

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.descriminator) == (member_name, member_descriminator):
            await  ctx.guild.unban(user)
            await  ctx.send(f'unbanned {user.mention}')
            return

#mute command
@bot.command()
async def mute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
           await member.add_roles(role)
           await ctx.send("{} has {} has been muted" .format(member.mention,ctx.author.mention))
           return

           overwrite = discord.PermissionsOverwrite(send_messages=False)
           newRole = await guild.create_role(name="Muted")

           for channel in guild.text_channels:
               await channel.set_permissions(newRole,overwrite=overwrite)
               
           await member.add_roles(newRole)
           await ctx.send("{} has {} has been muted" .format(member.mention,ctx.author.mention))
           

#unmute command
@bot.command()
async def unmute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
           await member.remove_roles(role)
           await ctx.send("{} has {} has been unmuted" .format(member.mention,ctx.author.mention))
           return

#forbidden nuke command
@bot.command()
async def nuke(ctx):
    channels = ctx.guild.channels

    for channel in channels:
        try:
 
            #await channel.delete()
            print(channel.name + " has been deleted.")           
        
        except Exception as error:
            print(channel.name + " failed to delete.") 
            print(error)
    else: 
            
            await ctx.channel.send('NUKE COMMAND TRIGGERED!')
            embed = discord.Embed(title='Nuked Failed!',description=
            "You were unsuccessful in nuking because The owner of the 'Jonse(AJ) Official Server', Jonse has forbidden nuking!"
            " You have violated the rules!"
            " Everyone is forbidden to nuke the server!" 
            " Please follow the rules! " "<@{}>".format(ctx.author.id), colour=discord.Colour.red()) 
       
    await ctx.send(embed=embed) 


    
#Help command
bot.remove_command("help")
@bot.command()
async def help(ctx):
  embed = discord.Embed(title='$help command', description='shows this message',colour=discord.Colour.dark_red())
  embed.add_field(name = '$kick[user]',  value = 'Kicks a member' ,            inline = False )
  embed.add_field(name = '$ban[user]',  value = 'Bans a member' ,            inline = False )
  embed.add_field(name = '$unban[user]',  value = 'Unbans a member' ,            inline = False )
  embed.add_field(name = '$mute[user]',  value = 'Mutes a member' ,            inline = False )
  embed.add_field(name = '$unmute[user]',  value = 'Unmutes a member' ,            inline = False )
  embed.add_field(name = '$leave[VC]',  value = 'Bot leaves the voice channel' , inline = False )
  embed.add_field(name = '$coinflip[Random]',  value = 'Flips a coin to get either head or tails' , inline = False )
  embed.add_field(name = '$clear[Amount]',  value = 'Clears a certain number of messages' , inline = False )
  embed.add_field(
	    name='$nuke[Destruction]',
	    value=
	    "Deletes all the channels and categories! However you cannot bomb in Jonse's (developer) Server. But your free to destroy your Server! Enjoy bombing! ",inline=False)
  embed.add_field(
	    name='$info[Information]',
	    value='Gives information about the bot, its developer and gives an invite link which you can use to invite Proto bot to your own server!')
  await ctx.send(embed = embed) 

#infomation command
@bot.command()
async def info(ctx):
	embed = discord.Embed(
	    title='Ultimate bot',
	    description='A bot build with Python 3.8.2',
	    colour=discord.Colour.red())
	embed.add_field(
	    name="bot's Command Prefix", value='$<command>', inline=False)
	embed.add_field(name='Developer', value="Jonse(AJ)", inline=False)
	embed.add_field(
	    name="Developer's assistant", value="Jaden Loh", inline=False)#Jaden is Jonse's close friend who had helped in the making of this bot
	embed.add_field(name= "invite", value= 'https://tinyurl.com/y3urj59j')

	await ctx.send(embed=embed)  
  
