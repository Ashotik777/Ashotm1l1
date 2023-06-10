import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="&", intents=intents )

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

  
@bot.command()
async def hello(ctx):
    await ctx.send(f'Privet! Ya bot ecolog {bot.user}!')
  

@bot.command()
async def eco(ctx):
   print('Сделать компанию по производству очищающего порошка. Собрать группу людей и арендовать катер для сбора мусора в водоёмах')

bot.run()
