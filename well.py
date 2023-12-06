import discord 
import os 
import asyncio
from discord.ext import commands
import random

client = discord.Client()
bot = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('>salaam'):
    await message.channel.send('walekumassalaam patthey')
  

@client.event
async def arfan(ctx):
  if ctx.message.content == "hello":
    if ctx.message.author.id == ('368058579657293824'):
      choicesa = ('get away', 'dont greet me', 'youre wasting my time', 'Hallo', 'oh god its you', '....' , 'dude go away' , 'WHAT DO YOU WANT' , 'HIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII' , 'i dont talk to degenerates')
    await bot.say(random.choice(choicesa))


    

client.run(os.environ['key'])
              
