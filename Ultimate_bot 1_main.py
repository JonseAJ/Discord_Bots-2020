Jonse first Discord bot.py!
Also this is the best bot he has ever created!
Fully upgraded and an improved version of his prototype of this bot!



import discord
from discord.ext import commands
import random
import keep_alive
import datetime



#command prefix
bot = commands.Bot(command_prefix='!')


#when bot is ready
@bot.event
async def on_ready():
	await bot.change_presence(
	    status=discord.Status.online, activity=discord.Game("Send !help  to see what I can do!"))
	print('Discord Ultimate bot"" is online.', )
	print(
	    'Need to add !unban[user],!join[VC],!leave[VC],!mute[user],!unmute[user] to Ultimate bot'
	)

#error handling vvv
@bot.event
async def on_command_error(ctx, error):
  embed = discord.Embed(description= f'Error: {error}', colour=discord.Colour.red())
  await ctx.send(embed=embed)


#Admin commands

@bot.command()
#@commands.has_permissions(administrator=True)-only adding this if I only want qdmin to kick 
async def kick(ctx, member: discord.Member, reason=None):
	await member.kick(reason=reason)
	embed = discord.Embed(
	    title=f"{ctx.author.name} kicked: {member.name}",
	    description=f"{reason}",
	    colour=discord.Colour.red())
	await ctx.send(embed=embed)

#ban command
@bot.command()
#@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, reason=None):
	await member.ban(reason=reason)
	embed = discord.Embed(
	    title=f"{ctx.author.name} banned: {member.name}",
	    description=f"{reason}",
	    colour=discord.Colour.red())
	await ctx.send(embed=embed)


#unban command not working
@bot.command()
#@commands.has_permissions(administrator=True)
async def unban(ctx, member, *, reason=None):
	member = await bot.fetch_user(int(member))
	await ctx.guild.unban(member, reason=reason)

	embed = discord.Embed(
	    title=f"{ctx.author.name} unbanned: {member.name}", description=reason)
	await ctx.send(embed=embed)

# join command
@bot.command()
async def join(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None: # If the user is not connected to channel
        await ctx.send("Be in a voice channel first!")
        return
    channel = ctx.message.author.voice.voice_channel
    await channel.connect()
 


#slap command
@bot.command()
async def slap(ctx, member: discord.Member, reason=None):
	embed = discord.Embed(
	    title=f':scream_cat: {member.name} has been slapped!',
	    description=f'{reason}',
	    colour=discord.Colour.green())
	await ctx.send(embed=embed)

#warn command
@bot.command()
async def warn(ctx, *, member: discord.Member, reason=True):
	embed = discord.Embed(
	    title=f'{member.name} has been warnned (reason)!',
	    description=f"{reason}",
	    colour=discord.Colour.dark_red())
	await ctx.send(embed=embed)


#dm command
@bot.command()
async def dm(ctx, user_id=None, *, args=None):
    if user_id != None and args != None:
        try:
            target = await bot.fetch_user(user_id)
            await target.send(args)

            await ctx.channel.send("'" + args + "' sent to: " + target.name)
            #await ctx.message.delete()

        except:
            await ctx.channel.send("Couldn't dm the given user.")
        

    else:
        await ctx.channel.send("You didn't provide a user's id and/or a message.")

#dm_all command
@bot.command()
async def dm_all(ctx, *, args=None):
    if args != None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(args)
                print("'" + args + "' sent to: " + member.name)
                await ctx.message.delete()

            except:
                print("Couldn't send '" + args + "' to: " + member.name)

    else:
        await ctx.channel.send("A message was not provided.")

#suggest command
@bot.command()
async def suggest(ctx,*,suggestion):
  author=ctx.message.author
  #file=open("suggestions.txt","a+")
  #file.write(str(author)+" : "+suggestion+"\n")
  embed = discord.Embed(
    title = 'Suggestion',
    description = "This Was Suggested By",
    colour = discord.Colour.orange()
  )

  embed.set_footer(text = "Made By Jonse(AJ) with python 3.8.2")
  embed.set_author(name = "Moderation#2520")
  embed.add_field(name = author, value = suggestion)
  await ctx.send("Suggestion Submitted")
  channel = bot.get_channel(746566318521843793)
  msg = await channel.send(embed=embed)
  await msg.add_reaction('👍')
  await msg.add_reaction('👎')

#adding adding roles
#AutoRole1- tester role
@bot.command()
async def tester_role(ctx):
    member = ctx.message.author
    role = ctx.guild.get_role(731090278450200586)
    await member.add_roles(role)
    await ctx.send("{} Have Been Given The Role!l {}".format(member.mention,role.mention),)
    await ctx.send("You Are Now A {} {}".format(role.mention,member.mention)) 
    celebration_upon_new_role='👏🎉🥳👏🥳🎉👏!'
    await ctx.send(celebration_upon_new_role)

#AutoRole2-member AutoRole1
@bot.command()
async def member_role(ctx):
    member = ctx.message.author
    role = ctx.guild.get_role(749089331787858000)
    await member.add_roles(role)
    await ctx.send("{} Have Been Given The Role! {}".format(member.mention,role.mention),)
    await ctx.send("You Are Now A {} {}".format(role.mention,member.mention)) 
    celebration_upon_new_role='👏🎉🥳👏🥳🎉👏!'
    await ctx.send(celebration_upon_new_role)


#Create Role
@bot.command()
async def create_role(ctx,name,*,reason=None):
  await ctx.guild.create_role(name=name, colour=discord.Colour.orange())




#Server mannagements commands
#clear command
@bot.command(pass_text=True)
async def clear(ctx, amount=1):
	embed = discord.Embed(
	    title=f"{ctx.author.name} cleared: {ctx.channel.name}",
	    description=f"{amount} messages were cleared",
	    colour=discord.Colour.orange())
	await ctx.channel.purge(limit=amount + 1)
	await ctx.send(embed=embed)


#forbidden nuke command
@bot.command()
@commands.has_permissions(administrator=True)
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
            await ctx.channel.send("NUKING NOW!"" <@{}>".format(ctx.author.id))
       
            embed = discord.Embed(title='Nuked Failed!',description=
            "You were unsuccessful in nuking because The owner of the 'Jonse(AJ) Official Server', Jonse has forbidden nuking!"
            " You have violated the rules!"
            " Everyone is forbidden to nuke the server!" 
            " Please follow the rules! " "<@{}>".format(ctx.author.id), colour=discord.Colour.red()) 
       
    await ctx.send(embed=embed) 
    
#Game commands
#coinflip command
@bot.command()
async def coinflip(ctx):
	possible_outcomes = ['Heads', 'Tails']
	await ctx.send(random.choice(possible_outcomes))
#list of  possible outcomes in coinflip command
@bot.command()
async def lscoinflip(ctx):
	embed = discord.Embed(title='Heads  Tails', colour=discord.Colour.green())
	await ctx.send(embed=embed)

#dice_roll command
@bot.command()
async def dice(ctx):
	possible_outcomes = ['1,2,3,4,5,6']
	await ctx.send(random.choice(possible_outcomes))
#list of  possible outcomes in rps command
@bot.command()
async def lsdice(ctx):
	embed = discord.Embed(
	    title='1  2  3  4  5 6', colour=discord.Colour.green())
	await ctx.send(embed=embed)

#rock,paper scissors command
@bot.command()
async def rps(ctx):
	moves = ['Rock', 'Paper', 'Scissors']
	await ctx.send(random.choice(moves))
#list of  possible outcomes in rps command
@bot.command()
async def lsrps(ctx):
	embed = discord.Embed(
	    title='Rock  Paper  Scissors', colour=discord.Colour.green())

	await ctx.send(embed=embed)


#Fun commands


#say command
@bot.command()
async def say(ctx, *, message=None):
	message = message
	if message == None:
		await ctx.channel.send(
		    "You didn't say anything after the command '!say'"
		    "<@{}>".format(ctx.author.id))
	else:
		#await ctx.message.delete()
		await ctx.send(message)


#ping command
@bot.command()
async def ping(ctx, user: discord.User=None):
    try:
        await ctx.send("<@{}>".format(user.id))
    except:
        if user == None:
            await ctx.send("Pls provide a user")
        else:
            await ctx.send("Invalid user")
 

#joke command
@bot.command()
async def joke(ctx):
	jokes = [
	    'I was gonna tell a time-traveling joke, but you guys didn’t like it.',
	    'What do you get when you cross a snowman with a vampire?\nFrostbite',
	    'Why did the robber take a bath before he stole from the bank?\n He wanted to make a clean get away!',
	    'Want to hear a joke about construction?\n Im still working on it',
	    'This graveyard looks overcrowded People must be dying to get in there. #I agree this joke is a bit dark'
	]
	await ctx.send(random.choice(jokes))
#list of jokes in joke command
 

#list of jokes in joke command
@bot.command()
async def lsjoke(ctx):
  embed = discord.Embed(title="list of jokes in '!joke' command",colour=discord.Colour.green())
  embed.add_field(name='I was gonna tell a time-traveling joke, but you guys didn’t like it.',value=':D',inline=False)
  embed.add_field(name='What do you get when you cross a snowman with a vampire?',value='Frostbite',inline=False)
  embed.add_field(name='Why did the robber take a bath before he stole from the bank?',value='He wanted to make a clean get away!',inline=False)
  embed.add_field(name='Want to hear a joke about construction?',value=' Im still working on it',inline=False)
  embed.add_field(name='This graveyard looks overcrowded',value='People must be dying to get in there. #I agree this joke is a bit dark',inline=False)
  
  await ctx.send(embed=embed)

#reply command
@bot.command()
async def reply(ctx, *, question=None):
	responses = ["yes", "maybe", "no"]
	if question == None:
  
    #embed = discord.Embed(title = "You forgot to ask a question after '!reply'" "<@{}>".format(ctx.author.id),colour=discord.Colour.green())
    
    #await ctx.send(embed=embed)

		await ctx.channel.send("You forgot to ask a question after '!reply' " "<@{}>".format(ctx.author.id))
	else:
		await ctx.send(
		    f"question: {question}\nanswer: {random.choice(responses)}")

#list of replies in reply command
@bot.command()
async def lsreply(ctx):
  embed = discord.Embed(
	    title="list of replies in '!reply' command",
      description='yes, maybe, no',colour=discord.Colour.green())
  await ctx.send(embed=embed)


#Other commands

#month command to see the what month is it now!
@bot.command()
async def month(ctx):
  embed = discord.Embed(title='The Current Month', description= datetime.datetime.now().strftime('%B'),colour=discord.Colour.green())
  await ctx.send(embed=embed) 

#Rules command
@bot.command()
async def rules(ctx):
	embed = discord.Embed(
	    title='Server rules',
	    description='1)Everyone here is supposed to follow the rules',
	    colour=discord.Colour.blue())

	embed.add_field(
	    name='Respect everyone at all times',
	    value='Show respect to one another',
	    inline=False)

	embed.add_field(
	    name='2)Vulgarities will not be tolerated',
	    value='No use of vulgar language in both text and voice channels',
	    inline=False)

	embed.add_field(
	    name='No spamming',
	    value=
	    "Don't flood the text channels with messages. Use the bot commands when required",
	    inline=False)

	embed.add_field(
	    name='Channel 5, please',
	    value='In this server please communicate in English only.',
	    inline=False)

	embed.add_field(
	    name='Do not post illigal!inappropirate contents',
	    value='This  includes personal information and 18+ contents.',
	    inline=False)

	embed.add_field(
	    name='No racism',
	    value=
	    'Especially no racism as this country is a multi-racial country. So please respects other races.',
	    inline=False)

	embed.add_field(
	    name='Thank you for reading and following the rules.',
	    value='Message from your cheerful host, Jonse!',
	    inline=False)

	await ctx.send(embed=embed)

#infomation command
@bot.command()
async def info(ctx):
	embed = discord.Embed(
	    title='Ultimate bot',
	    description='A bot build with Python 3.8.2',
	    colour=discord.Colour.green())
	embed.add_field(
	    name="bot's Command Prefix", value='!<command>', inline=False)
	embed.add_field(name='Developer', value="Jonse(AJ)", inline=False)
	embed.add_field(
	    name="Developer's assistant", value="Jaden Loh", inline=False)#Jaden is Jonse's close friend who had helped in the making of this bot
	embed.add_field(name= "invite", value= 
	'https://tinyurl.com/y6ho6zav')

	await ctx.send(embed=embed)


#Help command
bot.remove_command("help")
@bot.command()
async def help(ctx):
	embed = discord.Embed(
	    title='!help command',
	    description='Shows this message',
	    colour=discord.Colour.green())
	embed.add_field(name='!kick[user]', value='Kicks a member', inline=False)
	embed.add_field(name='!ban[user]', value='Bans a member', inline=False)
	#embed.add_field(name='!unban[banned user]', value='Unbans a banned member', inline=False)
	embed.add_field(
	    name='!join[VC]', value='bot joins the voice channel', inline=False)
	embed.add_field(
	    name='!slap[user]',
	    value=' A member will be slapped by another member',
	    inline=False)
	embed.add_field(
	    name='!warn[user]',
	    value=' A member will be warnned by another member',
	    inline=False)
	embed.add_field(
	    name='!dm[user]',
	    value="Dms a member with the author's message",
	    inline=False)
	embed.add_field(
	    name='!dm_all[Everyone]',
	    value="Dms all the members of the server with the author's message",
	    inline=False)
	embed.add_field(
	    name='!suggest[Suggstion]',
	    value="A member can suggest a suggestion in any channel but it will be submitted to the suggestion channel",
	    inline=False)    
	embed.add_field(
	    name='![role.name]_role[User]',
	    value='A member will receive a role. The currently available roles are the !tester_role & !member_role',
	    inline=False)
	#embed.add_field(
	#    name='![newly created role.name]_role[New_role]',
	#    value='A member can create a new role',
	#    inline=False) In progress      
	embed.add_field(
	    name='!clear[amount]',
	    value='Clears a certain number of messages',
	    inline=False)
	embed.add_field(
	    name='!nuke[Destruction]',
	    value=
	    'Deletes all the channels and categories! Therefore this command will be only available to trusted members only!',
	    inline=False)      
	embed.add_field(
	    name='!coinflip[random]',
	    value='Flips a coin to get either head or tails',
	    inline=False)
	embed.add_field(
	    name='!dice[random]',
	    value='Rolls a dice to get a number from 1-6 ',
	    inline=False)
	embed.add_field(
	    name='!rps[random]', value='Rock, paper, scissors game', inline=False)
      
	embed.add_field(
	    name='!say[message]',
	    value="Repeats what the author said after !say",
	    inline=False)
	embed.add_field(
	    name='!ping[author]', value='Pings the author', inline=False)
	embed.add_field(name='!joke[random]', value='Tells a joke', inline=False)
	embed.add_field(
	    name='!reply[question][random]',
	    value='Randomly replies to a question',
	    inline=False)
	embed.add_field(
	    name='!ls[commands with >1 possible outcomes]',
	    value="Shows the list of possible outcomes for the command. Works only on !joke,!reply,!rps,!coinflip,!dice commands",
	    inline=False)       
	embed.add_field(
	    name='!month',
	    value='The bot says the current month!',
	    inline=False)  
	embed.add_field(
	    name='!rules[Information]',
	    value='Tells the rules of the server',
	    inline=False)
	embed.add_field(
	    name='!info[Information]',
	    value='Gives information about the bot, its developer and gives an invite link which you can use to invite Ultimate bot to your own server!',
	    inline=False)
    
  
     

	await ctx.send(embed=embed)



token = 'MY_BOT_TOKEN'
keep_alive.keep_alive()
bot.run(token)

#notice !join and !dm not working properly but there is an output from the bot
#!join
#!dm
#Commands to be fixed and added to the bot
#!unban[user]
#!leave[VC]
#!mute[user]
#!unmute[user]

#to be fixed and added to the !help command

#embed.add_field(name = '!unban[user]',  value = 'Unbans a member' , inline = False )
#embed.add_field(name = '!leave[VC]',  value = 'bot leaves the voice channel' , inline = False )
#embed.add_field(name = '!mute[user]',  value = 'mutes a member' ,   inline = False )
#embed.add_field(name = '!unmute[user]',  value = 'unmutes a member' , inline = False )
