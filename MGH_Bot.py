import discord
from discord import colour
from discord import embeds
from discord import client
from discord import message
from discord import file
from discord import channel
from discord.asset import VALID_STATIC_FORMATS
from discord.ext import commands
from discord.ext import tasks
from asyncio import *
import random
from discord.ext.commands.bot import Bot
from discord.ext.commands.core import command
from discord.ext.commands.errors import DisabledCommand
from discord.file import File
from discord.user import User



client = commands.Bot(command_prefix = '!')

client.remove_command("help")

Token = ""
sadegh_id = 671807746743730230
line = '●▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬●'



#source Path
#-----------------
lockMessagePath = 'D:\EhsanSadegh\Python Projects\Sadegh_Bot\chlock.png'
unLockMessagePath = 'D:\EhsanSadegh\Python Projects\Sadegh_Bot\chUnlock.png'
greenLinePath = 'D:\EhsanSadegh\Python Projects\Sadegh_Bot\lineG.png'
#-----------------

    

@client.event
async def on_Ready():
    activity = discord.Game(name='Mafia Game Helpering', type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    # await client.Client.change_presence(status = discord.Status.online)
    #await client.change_presence(game=discord.Game(name='Helping For Mafia Game'))
    

# Define Methodes For Use
async def darkLordErorr(ctx):
    await ctx.channel.purge(limit =1) 
    await ctx.send('```' +"Your not 𝐃𝐚𝐫𝐤 𝐋𝐨𝐫𝐝"+ '```')
    await ctx.send(line)

@client.command()
async def l(ctx): 
    await ctx.channel.purge(limit=1)
    await ctx.send(line)

@client.command()  
async def c(ctx,amount = ''):
    if ctx.message.author.id == sadegh_id:
        if amount == 'c':
            messageErorr = "Delete " + 'Every Messages in This Channel' 
            numDeleteMessage = 60
            await ctx.channel.purge(limit=numDeleteMessage + 1) 
            await ctx.send('```' + messageErorr + '```')
        else:
           # limit = int(amount)
            messageErorr = "Delete " + amount + " Messages! "
            await ctx.channel.purge(limit = int(amount)) 
            await ctx.channel.purge(limit = 1) 
            await ctx.send('```' + messageErorr + '```')   
    else:
        await darkLordErorr(ctx)

@client.command()
async def s(ctx):
    if ctx.message.author.id == sadegh_id:
        shot = ""
        await ctx.channel.purge(limit=1)
        await ctx.send(line) 
        await ctx.send('**' + "PLease Give Me Shot: " + '**')     
    else:
        await darkLordErorr(ctx)
# Lock Channel
@client.command()
async def lo(ctx):
    if ctx.message.author.id == sadegh_id:
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.channel.purge(limit=1)
        await ctx.send(file = discord.File(lockMessagePath))
    else:
        await darkLordErorr(ctx)
# UnLock Channel
@client.command()
async def ul(ctx):
    if ctx.message.author.id == sadegh_id:
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.channel.purge(limit=1) 
        await ctx.send(file = discord.File(unLockMessagePath))
    else:
        await darkLordErorr(ctx)

@client.command()  
async def g(ctx,gerogangirName = '',gerogangirNum = ''):
    if gerogangirName == '' or gerogangirNum == '':
        await ctx.send('```' +"Your miss Some Things!"+ '```')
    else:
        if ctx.message.author.id == sadegh_id: 
            await ctx.channel.purge(limit=1) 
            await ctx.send('**' +' Your Gerogangir Name is: '+ gerogangirName +
            '\n' +' Your Gerogangir Number is: '+ str(gerogangirNum) +'\n'+ line + '**' )
        else:
            await darkLordErorr(ctx) 
            
@client.command()
async def help(ctx):
    if ctx.message.author.id == sadegh_id:
        await ctx.channel.purge(limit=1) 
        await ctx.send('```' +"l = This put Line in Text Channel"+'\n'+'s = This Gonna Get Shot As Mafia'+
        '\n'+'g = This Write Gerogangir'+'\n'+'lo = This Gonna Lock Channel'+'\n'+'ul = This Gonna Un Lock Channel'+
        '\n'+'c = This Gonna Clear some Message'+'\n'+'lend = Put Green Phoenix Line' '```')
    else:
        await darkLordErorr(ctx)

@client.command()
async def lend(ctx):
    if ctx.message.author.id == sadegh_id:   
        await ctx.channel.purge(limit=1)
        await ctx.send(file = discord.File(greenLinePath))
    else:
        await darkLordErorr(ctx)

client.run(Token)
