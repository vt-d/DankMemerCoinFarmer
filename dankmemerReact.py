import discord, time

class MyClient(discord.Client):

    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        #if message.author == client.user:
        #    return
        channel = client.get_channel(ENTER CHANNEL ID)
        if message.author.id == 270904126974590976 and message.channel.id == ENTER CHANNEL ID:
            #print("Message from {0.author}: {0.content}".format(message))
            if "christmas tree" in message.content:
                time.sleep(1)
                await channel.send("christmas tree")
            elif "north pole" in message.content:
                time.sleep(1)
                await channel.send("north pole")
            elif "christmas card" in message.content:
                time.sleep(1)
                await channel.send("christmas card")
            elif "big bait catches big fish" in message.content:
                time.sleep(1)
                await channel.send("big bait catches big fish")
            elif "What type of meme do you want to post?" in message.content:
                time.sleep(1)
                await channel.send("k")
            elif "yes please" in message.content:
                time.sleep(1)
                await channel.send("yes please")
            elif "oh look a dragon" in message.content:
                time.sleep(1)
                await channel.send("oh look a dragon")
            elif "oh frick a dragon" in message.content:
                time.sleep(1)
                await channel.send("oh frick a dragon")
            elif "make snow angel" in message.content:
                time.sleep(1)
                await channel.send("make snow angel")                                             
            elif "frick off" in message.content:
                time.sleep(1)
                await channel.send("frick off")
            elif "glub glub glub" in message.content:
                time.sleep(1)
                await channel.send("glub glub glub")
            elif "mistletoe" in message.content:
                time.sleep(1)
                await channel.send("mistletoe")
            elif "krampus is a nerd" in message.content:
                time.sleep(1)
                await channel.send("krampus is a nerd")
            elif "push" in message.content:
                time.sleep(1)
                await channel.send("push")
            
client = MyClient()
client.run("ENTER TOKEN", bot = False)
