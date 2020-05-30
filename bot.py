# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:19:29 2020

Janet Bot

@author: Zane Fadul, Vera Zhong
"""

import os

import discord
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

if __name__ == '__main__':
    connect()
    