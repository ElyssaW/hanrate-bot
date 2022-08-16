#bot.py
import os
from discord.ext import commands
import random
import math
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

RUBY_TO_GOLD = 2
SAPH_TO_GOLD = 1/3
EMER_TO_GOLD = 1/24
SAPH_TO_RUBY = 1/6
EMER_TO_SAPH = 1/8
SILVER_TO_EMER = EMER_TO_GOLD * 10
COPPER_TO_EMER = SILVER_TO_EMER * 10

@bot.command(name='togold')
async def togold(context):

    request_list = context.message.content.replace(',', '').split()[1:]
    def calculate_total_gold(r, s, e):
            return (r * RUBY_TO_GOLD) + (s * SAPH_TO_GOLD) + (e * EMER_TO_GOLD)

    def make_change(money):
        return (money % 1) * 10

    ruby = 0
    saph = 0
    emer = 0
    gold = 0
    silver = 0
    copper = 0

    try:
        for item in request_list:
            if item.find('ru') != -1:
                ruby = int(item.replace('ru', ''))
            elif item.find('sa') != -1:
                saph = int(item.replace('sa', ''))
            elif item.find('em') != -1:
                emer = int(item.replace('em', ''))
            else:
                await context.send('Unknown item: ' + item)

    except:
        await context.send('Cannot parse input. Check your spaces!')

    else:
        total = calculate_total_gold(ruby, saph, emer)

        gold = math.floor(total)
  
        if not total.is_integer():
            silver = make_change(total)
  
            if silver.is_integer() is not True:
                copper = make_change(silver)
                copper = math.floor(copper)
  
            silver = math.floor(silver)
  
        response = "Exchange for " + str(gold) + " gold, " + str(silver) + " silver, and " + str(copper) + " copper"
        await context.send(response)
        
@bot.command(name='togems')
async def togold(context):

    request_list = context.message.content.replace(',', '').split()[1:]

    ruby = 0
    saph = 0
    emer = 0
    gold = 0
    silver = 0
    copper = 0
        
    try:
        for item in request_list:
            print(item)
            if item.find('gp') != -1:
                gold = int(item.replace('gp', ''))
            elif item.find('sp') != -1:
                silver = int(item.replace('sp', ''))
            elif item.find('cp') != -1:
                copper = int(item.replace('cp', ''))
            else:
                await context.send('Unknown item: ' + item)

    except:
        await context.send('Cannot parse input. Check your spaces!')

    else:
        emer = copper / COPPER_TO_EMER
        emer += silver / SILVER_TO_EMER
        emer += gold / EMER_TO_GOLD

        emer = math.floor(emer)

        saph = emer // 8
        emer = emer % 8
        ruby = saph // 6
        saph = saph % 6

        response = "You have " + str(ruby) + " rubies, " + str(saph) + " sapphires, and " + str(emer) + " emeralds."

        await context.send(response)
        
bot.run(TOKEN)