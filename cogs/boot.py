"""
Description:
This Cog contains all the events and commands related to operations at boot-time.
"""
# IMPORTS
#import [Module/Package]
from discord.ext import commands        # IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.

class Boot(commands.Cog):
    """Cog for boot-time events."""
    def __init__(self, bot):
        """Initializes the cog, passing in a bot to associate itself with."""
        self.bot = bot
    
    # <--- on_ready Event --->
    #? This prints all of the servers the bot is a member in to the output window.
    @commands.Cog.listener()
    async def on_ready(self):
        """on_ready Event Listener"""
        print(f'\n{self.bot.user} is connected to the following guilds:')
        for guild in self.bot.guilds:
            print(f'- {guild.name} (id: {guild.id})')
    
def setup(bot):
    """Adds The Cog To The Client."""
    bot.add_cog(Boot(bot))
