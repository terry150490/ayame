import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random
client = discord.Client()
auther_text = ""


with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Food(Cog_Extension):

    @commands.command()
    async def food(self,ctx):
        username = ctx.message.author.display_name
        print(username)
        msg = await ctx.send("今天想吃什麼")
        emoji1 = '\N{LARGE GREEN CIRCLE}'
        emoji2 = '\N{LARGE YELLOW CIRCLE}'
        emoji3 = '\N{LARGE RED CIRCLE}'
        emoji4 = '\N{LARGE BLUE CIRCLE}'
        await msg.add_reaction(emoji1)
        await msg.add_reaction(emoji2)
        await msg.add_reaction(emoji3)
        await msg.add_reaction(emoji4)
        # emoji = '\N{LARGE GREEN CIRCLE}'
    
    @commands.Cog.listener()

    async def on_message(self,msg):
        if msg.content == '~food':
            print(msg.id)


    async def on_reaction_add(self,reaction,user):
        print(reaction)
        print(user)
        if str(reaction) == '\N{LARGE GREEN CIRCLE}':
            if user == '':
                print("A")




    # @commands.Cog.listener()
    # async def on_reaction_add(self,reaction,user):



def setup(bot):
    bot.add_cog(Food(bot))


