import discord, os, asyncio
import config
client = discord.Client()

@client.event
async def on_ready():
    print("Logged on as {0}!".format(client.user.name))

@client.event
async def on_connect():
    channel = client.get_channel(config.channel)
    while True:
        await channel.send("pls hunt")
        await asyncio.sleep(5)
        await channel.send("pls fish")
        await asyncio.sleep(9)
        await channel.send("pls beg")
        await asyncio.sleep(5)
        await channel.send("pls dig")
        await asyncio.sleep(1)
        await channel.send("pls dep all")
        await asyncio.sleep(15)
            
token = config.token
client.run(token, bot = False)
