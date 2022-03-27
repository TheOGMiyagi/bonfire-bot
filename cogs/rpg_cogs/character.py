"""This Cog contains all the events & commands related to the Unofficial Dark Souls TTRPG.
"""
# IMPORTS
import d20
import discord
from discord.ext import commands

from src.rpg.character import Character


class Character(commands.Cog):
    """Cog for admin-level commands.
    """
    def __init__(self, bot):
        """Initializes the cog, passing in a bot to associate itself with.

        Args:
            bot (Obj): The instance of commands.Bot()
        """
        self.bot = bot
    
    @commands.command(name="roll", aliases=["Roll", "r", "R"])
    async def roll(self, ctx, expression: str='1d6'):
        """Rolls some dice.

        Args:
            ctx (Obj): Context in which the command was invoked.
            expression (str, optional): Dice expression to be evaluated. Defaults to '1d6'.
        """
        embed = discord.Embed(title="{} is rolling some dice...".format(ctx.message.author.name),
            description="{}".format(d20.roll(expression)),
            color=0x0072ff)
        embed.set_footer(text="Bonfire Bot by TheOGMiyagi")
        await ctx.message.channel.send(embed=embed)

    # <--- Character Generation Command --->
    @commands.command(name="generate_character", aliases=["Generate_Character",
        "gen_char",
        "Gen_Char",
        "random_stats",
        "Random_Stats"])
    async def generate_character(self, ctx):
        """This command allows the user to generate stats for Unofficial Dark Souls TTRPG Characters.

        Args:
            ctx (Obj): Context in which the command was invoked.
        """
        _char = Character()
        _char.roll_stats()
        embed = discord.Embed(title="Generating Dark Souls TTRPG Character Stats...",
            description="Here's a list of randomized stats for you to use in your character sheet!",
            color=0x0072ff)
        embed.add_field(name="Attunement", value=f'{_char.attunement}\t({_char.attunement_bonus})')
        embed.add_field(name="Dexterity", value=f'{_char.dexterity}\t({_char.dexterity_bonus})', inline=True)
        embed.add_field(name="Endurance", value=f'{_char.endurance}\t({_char.endurance_bonus})', inline=True)
        embed.add_field(name="Faith", value=f'{_char.faith}\t({_char.faith_bonus})', inline=True)
        embed.add_field(name="Intelligence", value=f'{_char.intelligence}\t({_char.intelligence_bonus})', inline=True)
        embed.add_field(name="Strength", value=f'{_char.strength}\t({_char.strength_bonus})', inline=True)
        embed.add_field(name="Vitality", value=f'{_char.vitality}\t({_char.vitality_bonus})', inline=True)
        embed.set_footer(text="Bonfire Bot by TheOGMiyagi")
        await ctx.message.channel.send(embed=embed)
        del _char
