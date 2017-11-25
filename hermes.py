import json
import discord

with open("client_data.json", "r") as f:
    clientdata = json.load(f)

myself = discord.Client()

@myself.event
async def on_message(message):
    if myself.user.mention in message.content and not message.author.bot and not message.channel.is_private:
        # Do stuff

myself.run(clientdata["token"])
