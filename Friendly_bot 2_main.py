Jonse second Discord.py bot with the applied IT idea from EAEcon hackathon 2020!
This bot randomly picks members of my server who are online and reminds them to do pushups and reminds them to do their homework! every 1 hour!
This function is similar to the IT idea of mine from the EAEcon hackathon 2020!

import discord
#from discord.ext import commands 
import asyncio 
import random
import datetime
import keep_alive

bot = discord.Client()
#bot = commands.Bot(command_prefix = '-')

#when bot is ready
@bot.event
async def on_ready():
	await bot.change_presence(
	    status=discord.Status.online, activity=discord.Game("Send -help to see what I can do!"))
print("Friendly bot is online.")
print('To do list for Friendly bot')
print("Need to make the bot announce '@member has left' when a member leaves the server")
print('Need to add the reaction role function like the one @Coldfrost has') 

#Friendly bot functions(bot 2&3 functions)
#function to indicate a member has joined the server created by Jonse
#on_member_join
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name= "welcome")
    Jonse_welcome_message = (f"{member.mention} Welcome to Jonse(AJ) Official Server! Make sure to read the rules and understand them. Bans will occur after 2 warnings! So please do not violate any rules! Hope you like the warm and friendly atmosphere in this server. Thank you for joining!")
    await channel.send(Jonse_welcome_message)

#function to indicate a member isn't longer present in the server 
#on_member_leave
@bot.event
async def on_member_leave(member):
    channel = discord.utils.get(member.guild.channels, name= "leaves and removes")
    Jonse_leave_message = ("Unfortunately, f{member.mention} is longer present in this server!")
    await channel.send(Jonse_leave_message)

#member removed function 
@bot.event
async def on_member_remove(member):
  channel = bot.get_channel(750961593277218838)
  #'leave and remove' channel id
  #channel = discord.utils.get(member.guild.channels, name= "leaves and removes")
  await channel.send(f"Bye {member.mention} !!!")

#reply function,bot replies when message contains trigger words
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    Trigger_words = ["Workout", "Pushup"]
    channel = message.channel
    for Trigger_word in Trigger_words:
        if Trigger_word.lower() in message.content.lower():
            response = f"Did you say {Trigger_word.lower()}? Drop and give me 10, {message.author.name}!"
            await channel.send(response)
            
    Trigger_words = ["Hello", "hey", "sup", "hi"]
    channel = message.channel
    for Trigger_word in Trigger_words:
        if Trigger_word.lower() in message.content.lower():
            response = f"Hi {message.author.name}!"
            await channel.send(response)
    
    Trigger_words = ["what is the month", "what is the current month", "what is this month"]
    channel = message.channel
    for Trigger_word in Trigger_words:
        if Trigger_word.lower() in message.content.lower():
            month = datetime.datetime.now().strftime('%B')
            response = f"Now the month is {month}, {message.author.name}!"
            await channel.send(response)
#help command
    if message.content.startswith('-help'):
        embed = discord.Embed(title="-help command", description="Shows this message", colour=discord.Colour.orange())#help command
        embed.add_field(name="The bot randomly reminds an online member to do their homework in the homework_reminder channel ", value="Check the homework_reminder channel!", inline=False)#homework_reminder
        embed.add_field(name="The bot randomly reminds an online member to do 10 pushups in the pushup_reminder channel ",value="Check the pushup_reminder channel!", inline=False)#pushup_reminder
        embed.add_field(name="The bot replies to a memeber with 'Did you say {Trigger_word}? Drop and give me 10, {the members name} if the member say any of the following Trigger words ", value="Trigger_words = [Workout, Pushup]", inline=False)#reply function to 'workout and pushup'
        embed.add_field(name="The bot replies to a member with 'hi' follow by the member's name if the member say any of the following Trigger words ", value="Trigger_words = [Hello, hey, sup, hi]", inline=False)#reply function to 'Hello, hey, sup, hi'
        embed.add_field(name="The bot tells what is the month when the member asks a question from the following Questions ", value="Questions = [what is the month, what is the current month, what is this month]", inline=False)#month function
        embed.add_field(name="-info command ", value="Gives information about the bot, its developer and gives an invite link which you can use to invite Friendly bot to your own server!", inline=False)#invite command        

        await channel.send(embed=embed)
#info command    
    if message.content.startswith('-info'):
        embed = discord.Embed(title="Friendly bot", description="A bot built with Python 3.8.2", colour=discord.Colour.orange())#info command 
        embed.add_field(name="Bot's command prefix", value="-<command>")#command prefix command        
        embed.add_field(name="Developer", value="Jonse(AJ)", inline=False)#Developer info   
        embed.add_field(name="invite", value="https://tinyurl.com/yyaleu7t", inline=False)
        await channel.send(embed=embed)                    




#Reminder functions
#pushup_reminder
@bot.event
async def pushup_reminder():
  while(True):
    await bot.wait_until_ready()
    online_members = []
    for member in bot.get_all_members():
      if member.status != discord.Status.offline and member.id != bot.user.id:
        online_members.append(member.id)
    if len(online_members) > 0:
      user = random.choice(online_members)
      channel = discord.utils.get(bot.guilds[0].channels, name="pushup_reminder")
      #channel = bot.get_channel(746615461038391307) #only if i want the reminder to work in just this channel and not in every channel with the name "pushup_reminder".
      current_time = int(datetime.datetime.now().strftime("%I"))
      message = f"It's {current_time} o'clock!, time for some pushups <@{user}>!"
      #message = f"It's time for some pushups <@{user}>!" #only if i want the reminder to work without bot giving the current time
      await channel.send(message)
    await asyncio.sleep(3600)
bot.loop.create_task(pushup_reminder())
#homework_reminder for students
async def homework_reminder():
  while(True):
    await bot.wait_until_ready()
    online_members = []
    for member in bot.get_all_members():
      if member.status != discord.Status.offline and member.id != bot.user.id:
        online_members.append(member.id)
    if len(online_members) > 0:
      user = random.choice(online_members)
      channel = discord.utils.get(bot.guilds[0].channels, name="homework_reminder")      
      #channel = bot.get_channel(746615551576768542) #only if i want the reminder to work in just this channel and not in every channel with the name "homework_reminder".      
      current_time = int(datetime.datetime.now().strftime("%I"))
      message = f"It's {current_time} o'clock!, do you have any homework <@{user}>? If you have, do it now! Do not procrastinate <@{user}>!"
      #message = f"Do you have any homework <@{user}>? If you have, do it now! Do not procrastinate <@{user}>!"  #only if i want the reminder to work without bot giving the current time
      await channel.send(message)
    await asyncio.sleep(3600)
bot.loop.create_task(homework_reminder())

token = "MY_BOT_TOKEN"
keep_alive.keep_alive()
bot.run(token)

Notice the bot may send out reminders but will say its {current time} o'clock! The current time it says will be wrong!
For example it may 4pm now but it will say its 7pm!
So this will be fixed in the future!

 role command functions are added to Ultimate bot. Similarly going to add reaction role funtrions to this Friendly bot
