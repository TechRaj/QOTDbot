import discord
import os
import json
import requests
import aiocron

my_secret = os.environ['TOKEN']
channel_id = 1234

client = discord.Client()

def get_question():
    response = requests.get('https://api.api-ninjas.com/v1/trivia?category=general', headers={'X-Api-Key': 'MY_API_KEY'})
    json_data = json.loads(response.text)
    question = json_data[0]['question'] + "?"
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
    return(question)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@aiocron.crontab('14 11 * * *')
async def cronjob1():
    channel = client.get_channel(channel_id)
    question = get_question()
    await channel.send(question)
    return

client.run(my_secret)
