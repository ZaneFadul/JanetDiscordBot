# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 22:48:24 2020

Message Manager

@author: Zane Fadul and Vera Zhong
"""
import discord
from discord.ext import commands
from bot import CLIENT

class MessageManager:
    def __init__(self):
        self.features = {'scream':[self.respond,"AHHHHHHHHHHH"],
                         'girl':[self.respond,"Not a girl."],
                         "who's the best":[self.respond,"Zane is, of course!"],
                         'go away janet':[self.leave, "Goodbye!"],
                         'shut up janet':[self.respond,"Okay!"],
                         "wasn't so bad":[self.respond,"It actually went terribly!"]} #dictionary with keyword as key and func name as value
        
    async def analyze(self, message):
        for feature in self.features:
            message.content = message.content.lower()
            if feature in message.content:
                func = self.features[feature][0]
                response = self.features[feature][1]

                await func(message, response) #execute function

    async def respond(self, message, response):
        await message.channel.send(response)

    async def leave(self, message, response):
        print(response)
        await message.channel.send(response)
        tempClient = discord.Client()
        server = tempClient.get_server("id")
        await server.leave()
    
    