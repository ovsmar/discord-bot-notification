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


async def SendMessage():
    message = str("⚠️ ATTENTION ⚠️ \n Pensez à signer!")
    await bot.wait_until_ready()
    channelID = bot.get_channel(905038240141156355)
    M1 = await channelID.send(message)
    await asyncio.sleep(28800)
    await M1.delete()
    
async def weekend():
    message2 = str("Bon week-end !")
    await bot.wait_until_ready()
    channelID = bot.get_channel(905038240141156355)
    M2 = await channelID.send(message2)
    await asyncio.sleep(10800)
    await M2.delete()
    
async def Bonappetit():
    message3 = str("Bon appétit !")
    await bot.wait_until_ready()
    channelID = bot.get_channel(905038240141156355)
    M3 = await channelID.send(message3)
    await asyncio.sleep(600)
    await M3.delete()
    

@bot.event
async def on_ready():
    print("Ready")
    scheduler = AsyncIOScheduler()

    scheduler.add_job(SendMessage, CronTrigger(hour="10, 14", minute="03", second="0",day_of_week ="mon,tue,wed,thu,fri"))
    scheduler.add_job(weekend, CronTrigger(hour="16", minute="55", second="0",day_of_week ="fri"))
    scheduler.add_job(Bonappetit, CronTrigger(hour="12", minute="30", second="0",day_of_week ="mon,tue,wed,thu,fri" )) 
    

    
     
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
