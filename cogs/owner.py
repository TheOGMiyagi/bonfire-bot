"""
Description:
This Cog contains all the events and commands only the bot owner can utilize.
"""
# IMPORTS
#import [Module/Package]
from discord.ext import commands        # IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.


class OwnerCog(commands.Cog):
	"""Cog with commands only the bot owner can invoke."""
	def __init__(self, bot):
		self.bot = bot
    
    # Hidden means it won't show up on the default help.
	@commands.command(name='load', hidden=True)
	@commands.is_owner()
	async def load_cog(self, ctx, *, cog: str):
		"""Command which Loads a Module.
		Remember to use dot path. e.g: cogs.owner"""
		try:
			self.bot.load_extension(cog)
		except Exception as e:
			await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
		else:
			await ctx.send('**`SUCCESS`**')

	@commands.command(name='unload', hidden=True)
	@commands.is_owner()
	async def unload_cog(self, ctx, *, cog: str):
		"""Command which Unloads a Module.
		Remember to use dot path. e.g: cogs.owner"""
		try:
			self.bot.unload_extension(cog)
			await ctx.send('**`SUCCESS`**')
		except Exception as e:
			await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

	@commands.command(name='reload', hidden=True)
	@commands.is_owner()
	async def reload_cog(self, ctx, *, cog: str):
		"""Command which Reloads a Module.
		Remember to use dot path. e.g: cogs.owner"""
		try:
			self.bot.unload_extension(cog)
			self.bot.load_extension(cog)
			await ctx.send('**`SUCCESS`**')
		except Exception as e:
			await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')


def setup(bot):
    bot.add_cog(OwnerCog(bot))
