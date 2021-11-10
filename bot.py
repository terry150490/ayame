import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix='~')
#目前要做的 先把簡單的東西丟進去 想辦法把撥歌也放進去 想想伺服器需要做些什麼東東

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

@bot.event
async def on_ready():
    print(">>bot is online<<")


@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')


if __name__ == "__main__":
    bot.run(jdata['TOKEN'])

