#from logging import DEBUG, debug
from typing import Text
import discord
from discord.ext import commands
from core.classes import Cog_Extension
#import re

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
        self.text_place = ctx.message.channel
        # print(self.text_place)
        msg = await ctx.send("今天想吃什麼")
        self.emojis = ['\N{LARGE GREEN CIRCLE}','\N{LARGE YELLOW CIRCLE}','\N{LARGE RED CIRCLE}','\N{LARGE BLUE CIRCLE}','\N{LARGE BROWN CIRCLE}','\N{MEDIUM BLACK CIRCLE}','\N{MEDIUM WHITE CIRCLE}']       
        await msg.add_reaction(self.emojis[0])
        await msg.add_reaction(self.emojis[1])
        await msg.add_reaction(self.emojis[2])
        await msg.add_reaction(self.emojis[3])       
        # emoji = '\N{LARGE GREEN CIRCLE}'
    
    @commands.Cog.listener()    
    async def on_reaction_add(self,reaction,user):
        random_breakfast = random.choice(jdata['breakfast_list'])
        random_lunch = random.choice(jdata['lunch_list'])   
        random_dinner = random.choice(jdata['dinner_list'])
        random_night_snack = random.choice(jdata['night_snack_list'])
        eat_what1 = {
            '🟢' : "想吃早餐，",
            '🟡' : "想吃午餐，",
            '🔴' : "想吃晚餐，",
            '🔵' : "想吃消夜，"
        }
        eat_what2 = {
            '🟢' : random_breakfast,
            '🟡' : random_lunch,
            '🔴' : random_dinner,
            '🔵' : random_night_snack
        }
        # await self.text_place.message.delete()
        if self.username == str(user)[:-5]:
            I = str(reaction)
            if I == '🟢' or I == '🟡' or I == '🔴' or I == '🔵':
                cnt = 0
                if cnt !=1:
                    self.icon = I
                    cnt+=1
                A = f"{eat_what1[I]}那要吃{eat_what2[I]}嗎？\n可以按白，下一個按黑"
                # print(I)
                # print(A)  
                self.msg = await discord.TextChannel.send(self.text_place,A)
                # print(self.emojis[6])
                # print(self.emojis[5])
                await self.msg.add_reaction(self.emojis[6])
                await self.msg.add_reaction(self.emojis[5])
            elif I == '⚫':
                #await self.msg.edit(content="bang")
                await self.msg.edit(content=f"{eat_what1[self.icon]}那要吃{eat_what2[self.icon]}嗎？\n可以按白，下一個按黑")
            elif I == '⚪':
                self.msg = await discord.TextChannel.send(self.text_place,"enjoy!")

                
            # if str(reaction) == "⚫":
            #     print("A")
                # await msg.edit(content=f"{eat_what1[I]}那要吃{eat_what2[I]}嗎？\n可以按白，下一個按黑")
                #⚪

            #eat_what[str(reaction)]()              
        # #🟢
        # if str(reaction) == "🟢": 
        #     if self.username == str(user)[:-5]:

            # '🟢' : await discord.TextChannel.send(self.text_place,"1"),
            # '🟡' : await discord.TextChannel.send(self.text_place,"2"),
            # '🔴' : await discord.TextChannel.send(self.text_place,"3"),
            # '🔵' : await discord.TextChannel.send(self.text_place,"4")

        #         self.time = 1
        #         if self.time == 1:
        #             msg = await discord.TextChannel.send(self.text_place,"想吃麵還是飯")
        #             await msg.add_reaction(self.emojis[5])
        #             await msg.add_reaction(self.emojis[6])
        #             await msg.add_reaction(self.emojis[4])

    
    # async def on_reaction_add(self,reaction,user):


def setup(bot):
    bot.add_cog(Food(bot))


