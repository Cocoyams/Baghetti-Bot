import discord

BOT_TOKEN_FILE = "bot_token.txt"    # Should only have one token

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

try:
    with open(BOT_TOKEN_FILE) as f:
        client = MyClient()
        client.run(f.read())
except:
    print("Baghetti bot failed to run!")
