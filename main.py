"""# RPG Cog
This Discord Bot is made to handle commands that are useful in playing The Unofficial Dark Souls TTRPG via Discord.
The RPG: https://i.4pcdn.org/tg/1528730920492.pdf

Required 3RD-Party PyPi Packages:
	- d20
    - discord
"""
import os

import discord
from discord.ext import commands


PREFIXES = ["bfire!", "bf!"]
try:
    TOKEN = os.environ['DISCORD_BOT_TOKEN']
except KeyError:
    #with open('TOKEN.txt', 'r') as file:
        #TOKEN = file.read()
    TOKEN = 'YOUR-TOKEN-HERE'
#* Instantiates An Instance Of The Bot() Class.
bot = commands.Bot(command_prefix=PREFIXES,
	intents=discord.Intents.all())


#* Loads cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'Cog: {filename[:-3].title().replace("_", "")} loaded.')
    elif filename.endswith('_cogs') or filename == "__pycache__":
        continue
    else:
        print(f'Cog: Unable to load {filename[:-3]}')


#* Module Code
def main():
    """Main Method
    """
    bot.run(str(TOKEN))


#? Driver Code
if __name__ == "__main__":
    main()
else:
    print(f"{__name__} was successfully imported") #! MUST have Python 3.x for use of f-strings!
