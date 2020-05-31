# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:19:29 2020

Janet Bot

@author: Zane Fadul, Vera Zhong
"""

import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


def connect():  
    load_dotenv()   
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')
    client = discord.Client()
    
    @client.event
    async def on_ready():
        guild = discord.utils.get(client.guilds, name=GUILD)
        print(f'{client.user} appears in {guild.name}!')
        
    client.run(TOKEN)

def event_listeners():
    bot = commands.Bot(command_prefix = '!')

    #Join Voice Channel
    @bot.command(pass_context=True)
    async def join(ctx):
        if ctx.message.author.voice:
            channel = ctx.message.autor.voice.channel
            await channel.connect()
            await ctx.send('Okay, joining you in the voice channel!')


if __name__ == '__main__':
    event_listeners()
    connect()
    