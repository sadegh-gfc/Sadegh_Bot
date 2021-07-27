import discord
from inspect import ClassFoundException
from discord import colour, message
from discord import embeds
from discord import client
from discord.ext import commands
from discord.ext import tasks
from asyncio import * 
import random
from discord.ext.commands.core import command
from discord.ext.commands.errors import DisabledCommand
client = commands.Bot(command_prefix = '!')
Token = "ODU2MTU3OTkzNzMyNTM4Mzc4.YM89RA.RogZvlarXs5SiEwNxDNf0FMk-hc"

@client.event
async def onReady():
    await client.changePrefrence(status = discord.Status.online)
    print("Bot Ready")
async def onMessage(ctx):
    await ctx.channel.purge(Limit = 1)

@client.command()
async def l(value):
    #print(type(value))
    await value.channel.purge(limit = 1)
    await value.send("──────────────────────")


client.run(Token)
