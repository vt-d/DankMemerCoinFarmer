import discord, time, os

class MyClient(discord.Client):

    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))
        channel = client.get_channel(751276567463854120)
        while True:
            await channel.send("pls hunt")
            print("Sent -> pls hunt")
            time.sleep(5)
            await channel.send("pls search")
            time.sleep(5)
            await channel.send("pls fish")
            print("Sent -> pls fish")
            time.sleep(9)
            await channel.send("pls beg")
            print("Sent -> pls beg")
            time.sleep(20)
            #await channel.send("pls search")
            time.sleep(5)
            
            await channel.send("pls pm")
            time.sleep(1)
            memeType = random.choice("f","r","i","c","k")
            time.sleep(3)
            print("Sent -> pls pm\nMeme Type: ",memeType)
            await.channel.send(memeType)
            time.sleep(8)
            
            await channel.send("pls beg")
            print("Sent -> pls beg")
            time.sleep(5)
            await channel.send("pls dep all")
            print("Sent -> pls dep all")
            time.sleep(15)
            
client = MyClient()
client.run("ENTER TOKEN", bot = False)
