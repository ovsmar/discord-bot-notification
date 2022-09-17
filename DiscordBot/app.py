import discord 
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import sys
import os
import asyncio

intents = discord.Intents.default() 
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents) 

message = str("⚠️ ATTENTION ⚠️ \n Pensez à signer!")
message2 = str("Bon week-end !") 


async def SendMessage():
    await bot.wait_until_ready()
    channelID = bot.get_channel(1020395232908546072)
    await channelID.send(message)
    
async def weekend():
    await bot.wait_until_ready()
    channelID = bot.get_channel(1020395232908546072)
    await channelID.send(message2)
    

@bot.event
async def on_ready():
    print("Ready")
    scheduler = AsyncIOScheduler()

    scheduler.add_job(SendMessage, CronTrigger(hour="10, 15", minute="30", second="0",day_of_week ="mon,tue,wed,thu,fri"))
    scheduler.add_job(weekend, CronTrigger(hour="16", minute="55", second="0",day_of_week ="fri"))
    
#TEST
    scheduler.add_job(SendMessage, CronTrigger(hour="22", minute="02", second="0",day_of_week ="sat" )) 
     
    scheduler.start()

@bot.command()
@commands.has_permissions(administrator=True)
async def close(ctx):
    response_close = f"Tu m'as tué... 😡 \n Désactivation du bot dans 5 secondes..."
    msgC= await ctx.send(response_close)
    await asyncio.sleep(5)
    await ctx.message.delete()
    await msgC.delete() 
    await bot.close()

     
@bot.command()
@commands.has_permissions(administrator=True)
async def restart(ctx):
  response_restart = f"Redémarrage du bot dans 5 secondes..."
  msgR = await ctx.send(response_restart)
  await asyncio.sleep(5)
  await ctx.message.delete() 
  await msgR.delete()
  os.system("clear")
  os.execv(sys.executable, ['python'] + sys.argv)
   
# @bot.command()
# @commands.has_permissions(administrator=True)
# async def run(ctx):
 
        

@bot.command()
async def about(ctx):
    await asyncio.sleep(0)
    await ctx.message.delete() 
    await ctx.send("Je suis un bot intelligent créé par une personne stupide..." ,file=discord.File('c00724125597bf8112ba89c72e9440c8.jpg'))

    
   

bot.run(os.environ["DISCORD_TOKEN"])
