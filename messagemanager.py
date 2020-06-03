# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 22:48:24 2020

Message Manager

@author: Zane Fadul and Vera Zhong
"""

class MessageManager:
    
    def __init__(self):
        self.message = ''
        self.features = {} #dictionary with keyword as key and func name as value
    
    def analyze(self, message):
        if message.content in self.features:
            self.features[message.content]() #execute function
