import discord, os
import asyncio
client = discord.Client()

@client.event
async def on_ready():
    print("Logged on as {0}!".format(client.user.name))

@client.event
async def on_connect():
    channel = client.get_channel(752051281950015570)
    while True:
        await channel.send("pls hunt")
        asyncio.sleep(5)
        await channel.send("pls search")
        asyncio.sleep(5)
        await channel.send("pls fish")
        asyncio.sleep(9)
        await channel.send("pls beg")
        asyncio.sleep(20)
        await channel.send("pls pm")
        asyncio.sleep(5)
        await channel.send("pls beg")
        asyncio.sleep(5)
        await channel.send("pls dep all")
        asyncio.sleep(15)
            
token = os.getenv('DISCORD_BOT_TOKEN')
client.run(token, bot = False)
