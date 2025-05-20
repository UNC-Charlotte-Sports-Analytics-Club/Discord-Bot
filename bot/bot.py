import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='test')
async def test(ctx, *, input: str):
    await ctx.send(input)

if __name__ == '__main__':
    token = os.getenv('DISCORD_BOT_TOKEN') # You all don't have this, but no worries, you can still commit changes
    if token is None:
        print("Token not found in environment variables.")
    else:
        bot.run(str(token))
