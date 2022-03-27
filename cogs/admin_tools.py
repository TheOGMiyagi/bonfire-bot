"""
Description:
This Cog contains all the events and commands related to administration and administrator tools.
"""
# IMPORTS
#import [Module/Package]
import discord                          # IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
from discord.ext import commands        # IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.

class AdminTools(commands.Cog):
	"""Cog for admin-level commands."""
	def __init__(self, bot):
		"""Initializes the cog, passing in a bot to associate itself with."""
		self.bot = bot

	# <--- Userinfo Command --->
	@commands.command(name="userInfo", aliases=["uInfo", "Uinfo"])
	@commands.guild_only()
	@commands.has_permissions(administrator=True)
	async def userinfo(self, ctx, user: discord.Member):
		"""Allows user data retrieval from within the Discord client."""
		embed = discord.Embed(title="{}'s Info".format(user.name),
			description="Here's What I could Find in Discord's Database!",
			color=0x0072ff)
		embed.add_field(name="Name", value=user.name)
		embed.add_field(name="ID", value=user.id, inline=True)
		embed.add_field(name="Status", value=user.status, inline=True)
		embed.add_field(name="Role", value=user.top_role, inline=True)
		embed.add_field(name="Joined At", value=user.joined_at, inline=True)
		embed.set_thumbnail(url=user.avatar_url)
		embed.set_footer(text="HGRE Bot by TheOGMiyagi")
		await ctx.message.channel.send(embed=embed)
	
	@commands.command(name="list_members", aliases=["list", "List", "members", "Members"])
	@commands.guild_only()
	@commands.has_permissions(administrator=True)
	async def list_members(self, ctx):
		"""Returns the list of memebers in the server."""
		members_list = []
		for member in ctx.guild.members:
			members_list.append(member.display_name)
		members_list.sort()
		message = "\n".join(members_list)
		await ctx.send(message)


def setup(bot):
	"""Adds The Cog To The Client."""
	bot.add_cog(AdminTools(bot))
