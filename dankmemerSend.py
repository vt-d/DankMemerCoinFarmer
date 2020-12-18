import discord, time, asyncio

class MyClient(discord.Client):

    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))
        channel = client.get_channel(751276567463854120)
        while True:
            await channel.send("pls hunt")
            time.sleep(5)
            await channel.send("pls search")
            time.sleep(5)
            await channel.send("pls fish")
            time.sleep(9)
            await channel.send("pls beg")
            time.sleep(20)
            await channel.send("pls search")
            time.sleep(5)
            await channel.send("pls pm")
            time.sleep(5)
            await channel.send("pls beg")
            time.sleep(5)
            await channel.send("pls dep all")
            time.sleep(15)
            
client = MyClient()
client.run("Mzc5NDcwMTg4NjY5ODI5MTIx.X6loFQ.8-TAOVT3HD7Wr0NyExRYK_wVXXw", bot = False)
#NzEzNTY3NjEyOTk0NDUzNTA0.X9qB6g.DVYlwTZhNbZsjgn0zmqPdNmaebY