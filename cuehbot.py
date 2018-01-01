import discord

import settings

client = discord.Client()

@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    if message.content.startswith('!cueh'):
        msg = 'Cueh para ti, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg, tts=True)


@client.event
async def on_ready():
    print("Cueh v{} ready".format(settings.version))


client.run(settings.bot_token)