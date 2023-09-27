import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.reply('Hello!', mention_author=True)


client.run('MTE1MjU3MTQ5ODQ5MDUwMzIzMA.GCQ3ie.xfmLdlnOfkzh4RXzTTExKYa7j70D5Lv365dK44')
