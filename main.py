import discord
import os
from discord.ext import commands, tasks
import asyncio
from discord.ext import commands, tasks
from datetime import datetime, timedelta

my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

def seconds_until_ten():
    now = datetime.now()
    target = (now + timedelta(days=1)).replace(hour=14, minute=00, second=0, microsecond=0)
    diff = (target - now).total_seconds()
    print(f"{target} - {now} = {diff}")
    return diff

@tasks.loop(seconds=1)
async def called_once_a_day_at_ten():
    await asyncio.sleep(seconds_until_ten())
    message_channel = client.get_channel(my_secret)
    print(f"Got channel {message_channel}")
    await message_channel.send("QOTD: blah blah blah")

@called_once_a_day_at_ten.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")

called_once_a_day_at_ten.start()
client.run(my_secret)
