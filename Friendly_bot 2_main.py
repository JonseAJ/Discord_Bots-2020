import discord
#from discord.ext import commands 
import asyncio 
import random
import datetime
import keep_alive

bot = discord.Client()
#bot = commands.Bot(command_prefix = '.')



#when bot is ready
@bot.event
async def on_ready():
    print("Friendly bot is online.")
    print('To do list for Friendly bot')
    print("Need to make the bot announce '@member has left' when a member leaves the server")
    print('Need to add the reaction role function like the one @Coldfrost has') 


#Friendly bot functions(bot 2&3 functions)
#on_member_join
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name= "welcome")
    Jonse_welcome_message = (f"{member.mention} Welcome to Jonse(AJ) Official Server! Make sure to read the rules and understand them. Bans will occur after 2 warnings! So please do not violate any rules! Hope you like the warm and friendly atmosphere in this server. Thank you for joining!")
    await channel.send(Jonse_welcome_message)

#on_member_leave
@bot.event
async def on_member_leave(member):
    channel = discord.utils.get(member.guild.channels, name= "leaves")
    Jonse_leave_message = ("Unfortunately, f{member.mention} is longer present in this server!")
    await channel.send(Jonse_leave_message)

#message function,bot replies when message contains any of the trigger words
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
      channel = bot.get_channel(736930120228536381)
      current_time = int(datetime.datetime.now().strftime("%I")) 
      message = f"It's {current_time} o'clock!, time for some pushups <@{user}>!"
      await channel.send(message)
    await asyncio.sleep(3600)
bot.loop.create_task(pushup_reminder())

token = "NzMxMDk2NDU0NTI0OTYwODQ5.XwhEoQ.x6cDj3499z_ERdudCQUDaoSh_xs"
keep_alive.keep_alive()
bot.run(token)