import discord
from discord.ext import commands
import random 
import asyncio 
from discord import Embed
#import datetime
#import youtube_dl  
#import keep_alive

#command prefix
bot = commands.Bot(command_prefix = '!')

bot.remove_command("help")
#when bot is ready
@bot.event
async def on_ready():
    print("Jonse's bot is online.")

#Music bot commands(bot no.4)
# join command
@bot.command()
async def join(ctx):
        if ctx.author.voice is None or ctx.author.voice.channel is None:
            await ctx.send("Be in a voice channel first!")
        channel = ctx.message.author.voice.channel
        await channel.connect()

@bot.command()
async def leave(ctx):
       channel = ctx.message.author.voice.channel
       await channel.disconnect()

#play command
#players = {}
#bot.command(pass_context=True)
#sync def play(ctx, url):
   #server = ctx.message.server
   #voice_bot = bot.voice_bot_in(server)
   #player = await voice_bot.create_ytdl_player(url)
   #players[server.id] = player
   #player.start()

#kick command-works only in jonse test server 

@bot.command()
async def kick(ctx, member: discord.Member, reason=None):
   await member.kick(reason=reason)
   await ctx.send(f"{member} has been kicked")

#ban command
@bot.command()
async def ban(ctx, member: discord.Member, reason=None):
   await member.ban(reason=reason)
   await ctx.send(f"{member} has been banned")

#unban command
@bot.command()
async def unban(ctx, member: discord.Member, reason=None):
   await member.unban(reason=reason)
   await ctx.send(f"{member} has been unbanned")
   
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

#clear command
@bot.command(pass_text=True)
async def clear(ctx, amount=2):
  if not ctx.author.permissions_in(ctx.channel).manage_messages:
    await ctx.send("Sorry you dont have permission!")
    return
  await ctx.channel.purge(limit=amount)

#coinflip command
@bot.command()
async def coinflip(ctx):
    possible_outcomes = ['Heads','Tails']
    await ctx.send(random.choice(possible_outcomes))

#dice_roll command
@bot.command()
async def dice(ctx):
    possible_outcomes = ['1','2','3','4','5','6']
    await ctx.send(random.choice(possible_outcomes))

#rock,paper scissors command
@bot.command()
async def rps(ctx):
    moves = ['Rock','Paper','Scissors']
    await ctx.send(random.choice(moves)) 

#joke command
@bot.command()
async def joke(ctx):
    jokes = ['I was gonna tell a time-traveling joke, but you guys didn’t like it.','What do you get when you cross a snowman with a vampire?\n Frostbite','Why did the robber take a bath before he stole from the bank?\n He wanted to make a clean get away!','Want to hear a joke about construction? Im still working on it','This graveyard looks overcrowded. People must be dying to get in there.',]
    await ctx.send(random.choice(jokes))    

#ping command
@bot.command()
async def ping(ctx):
  await ctx.send("<@{}>".format(ctx.author.id))

#slap command
@bot.command()
async def slap(ctx, member: discord.Member, reason=None):
   await member.slap(reason=reason)
   await ctx.send(f"{member} has been slapped")

#echo command
#@bot.command()
#async def echo(ctx):
		#await ctx.message()
		#await ctx.send(message)

#Help command
@bot.command()
async def help(ctx):
  embed = discord.Embed(title='help command', description='shows this message')
  embed.add_field(name = '!kick[user]',  value = 'Kicks a member' ,            inline = False )
  embed.add_field(name = '!ban[user]',  value = 'Bans a member' ,            inline = False )
  embed.add_field(name = '!join[VC]',  value = 'Bot joins a voice channel' ,   inline = False )
  embed.add_field(name = '!leave[VC]',  value = 'Bot leaves the voice channel' , inline = False )
  embed.add_field(name = '!coinflip[Random]',  value = 'Flips a coin to get either head or tails' , inline = False )
  embed.add_field(name = '!clear[Amount]',  value = 'Clears a certain number of messages' , inline = False )
  embed.add_field(name = '!dice[Random]',  value = 'Rolls a dice to get a number from 1-6 ' , inline = False )
  embed.add_field(name = '!pingme[author]',  value = 'Pings the author' , inline = False )
  embed.add_field(name = '!rps[random]',  value = 'Rock,paper,scissors game' , inline = False )
  embed.add_field(name = '!joke[random]',  value = 'Tells a joke' ,      inline = False )
  embed.add_field(name = '!rules[random]',  value = 'Tells the rules of the server' ,      inline = False )
  await ctx.send(embed = embed) 

#Rules command
@bot.command()
async def rules(ctx):
  embed = discord.Embed(title='Server rules', description='1)Everyone here is supposed to follow the rules')
  
  embed.add_field(name = 'Respect everyone at all times',  value = 'Show respect to one another' ,            inline = False )
  
  embed.add_field(name = '2)Vulgarities will not be tolerated',  value = 'No use of vulagr lanuguage in both text and voice channels' ,       inline = False )
  
  embed.add_field(name = 'No spamming',  value = 'Dont flood the text channels with messages. Use the bot commands when required' ,   inline = False )
  
  embed.add_field(name = 'Channel 5 please',  value = 'In this server please communicate in English only' , inline = False )
  
  embed.add_field(name = 'Do not post illigal/inappropirate contents',  value = 'This  includes personal information and 18+ contents' , inline = False )
  
  embed.add_field(name = 'No racisim',  value = 'Especially no racisim as this country is a multi-racial country. So please respects other races.' , inline = False )
  
  embed.add_field(name = 'Thank you for reading and following the rules',  value = 'Created by your cheerful host Jonse' , inline = False )
 
  await ctx.send(embed = embed) 

token ='NzMyMTEwMjcwNjM3Mjc3MTg0.XxLScQ.J46fnZtH9uJoLgT9OlL__jCKcaA'
#keep_alive.keep_alive()
bot.run(token)
