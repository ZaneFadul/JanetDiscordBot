# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:19:29 2020

Janet Bot

@author: Zane Fadul, Vera Zhong
"""

import os
import discord
#import random
from discord.ext import commands
from dotenv import load_dotenv
from messagemanager import MessageManager

try:
    load_dotenv()
except Exception as inst:
    print(inst)
            
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CLIENT = commands.Bot(command_prefix = '!')
manager = MessageManager()

def connect():  
    CLIENT.run(TOKEN)
    
@CLIENT.event
async def on_ready():
    guild = discord.utils.get(CLIENT.guilds, name=GUILD)
    print(f'{CLIENT.user} appears in {guild.name}!')
    
@CLIENT.event
async def on_message(message):
    if message.author == CLIENT.user:
        return
    manager.analyze(message)
    
@CLIENT.command(pass_context=True)
async def join(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
        await ctx.send('Okay, joining you in the voice channel!')

if __name__ == '__main__':
    connect()
    