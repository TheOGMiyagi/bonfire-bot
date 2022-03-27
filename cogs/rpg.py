"""This Cog contains all the events & commands related to the Unofficial Dark Souls TTRPG.
"""
# IMPORTS
from .rpg_cogs import Character, RollTables


def setup(bot):
    """Adds The Cogs To The Client.
    """
    bot.add_cog(Character(bot))
    bot.add_cog(RollTables(bot))
