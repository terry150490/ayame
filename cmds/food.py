from logging import DEBUG, debug
import discord
from discord import message
from discord.ext import commands
from core.classes import Cog_Extension
import re

import json
import random
#client = discord.Client()
auther_text = ""


with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Food(Cog_Extension):

    @commands.command()
    async def food(self,ctx):
        self.username = ctx.message.author.display_name
        print(self.username)
        msg = await ctx.send("今天想吃什麼")
        self.emojis = ['\N{LARGE GREEN CIRCLE}','\N{LARGE YELLOW CIRCLE}','\N{LARGE RED CIRCLE}','\N{LARGE BLUE CIRCLE}']       
        await msg.add_reaction(self.emojis[0])
        await msg.add_reaction(self.emojis[1])
        await msg.add_reaction(self.emojis[2])
        await msg.add_reaction(self.emojis[3])
        
        
        # emoji = '\N{LARGE GREEN CIRCLE}'
    
    @commands.Cog.listener()

    # async def on_message(self,msg):


    async def on_reaction_add(self,reaction,user):              
        #🟢
        
        if str(reaction) in self.emojis: 
            if(self.username==str(user)[:-5]):     
                print("A")




    # @commands.Cog.listener()
    # async def on_reaction_add(self,reaction,user):



def setup(bot):
    bot.add_cog(Food(bot))


