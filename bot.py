import discord
from discord.ext import commands
import json
import os

bot = commands.Bot(command_prefix='~')
#目前要做的 先把簡單的東西丟進去 想辦法把撥歌也放進去 想想伺服器需要做些什麼東東

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

@bot.event
async def on_ready():
    print(">>bot is online<<")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un-Loaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re-Loaded {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])

