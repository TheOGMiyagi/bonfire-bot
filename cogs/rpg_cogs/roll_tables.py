"""This Cog contains all the events & commands related to the Unofficial Dark Souls TTRPG.
"""
# IMPORTS
import discord
from discord.ext import commands

from src.rpg.roll_tables import *


class RollTables(commands.Cog):
    def __init__(self, bot):
        """Initializes the cog, passing in a bot to associate itself with.

        Args:
            bot (Obj): The instance of commands.Bot()
        """
        self.bot = bot
    
    # <--- Roll Tables Command Group --->
    @commands.group(name="roll_table",
        pass_context=True,
        invoke_without_command=True,
        aliases=["Roll_Table",
            "roll_tables",
            "Roll_Tables",
            "rtable",
            "RTable",
            "rtables",
            "RTables",
            "r_table",
            "R_Table",
            "r_tables",
            "R_Tables"])
    async def roll_table(self, ctx):
        """Default command, acting as a command-specific help command.

        Args:
            ctx (Obj): Context in which the command was invoked.
        """
        embed = discord.Embed(title="bfire![roll_table(s) | rtable(s) | r_table(s)] <table-type>",
            description="This command provides access to various roll tables found in UDS TTRPG.",
            color=0x0072ff)
        _table_types = ('character_names',
            'covenant_names',
            'homeland_names',
            'land_names',
            'locations_info',
            'lords_info',
            'shards_of_memory',
            'lords_count')
        embed.add_field(name='Name Categories',
            value='\n'.join(_table_types))
        embed.set_footer(text="Bonfire Bot by TheOGMiyagi")
        await ctx.message.channel.send(embed=embed)
    # <--- Character Names Command Sub-Group --->
    @roll_table.group(name='character_name',
        pass_context=True,
        invoke_without_command=True,
        aliases=['Character_Name',
            'character_names',
            'Character_Names'])
    async def rt_character_names(self, ctx):
        embed = discord.Embed(title="bfire![roll_table(s) | rtable(s) | r_table(s)] character_names <gender>",
            description="This command provides simple name generation based on the category you input.",
            color=0x0072ff)
        _gender_categories = ('neutral', 'male', 'female')
        embed.add_field(name='Table Types',
            value='\n'.join(_gender_categories))
        embed.set_footer(text="Bonfire Bot by TheOGMiyagi")
        await ctx.message.channel.send(embed=embed)
    
    # <--- Neutral Name Sub-Command --->
    @rt_character_names.command(name='neutral',
        pass_context=True,
        invoke_without_command=True,
        aliases=['Neutral',
            'non-binary',
            'Non-binary',
            'Non-Binary'])
    async def rt_neutral_name(self, ctx):
        embed = discord.Embed(description="Rolling for a neutral name...",
            color=0x0072ff)
        embed.add_field(name='Rolled Name',
            value=neutral_name())
        embed.set_footer(text="Bonfire Bot by TheOGMiyagi")
        await ctx.message.channel.send(embed=embed)
    # <--- Male Name Sub-Command --->
    @rt_character_names.command(name='male',
        pass_context=True,
        invoke_without_command=True,
        aliases=['Male',
            'man',
            'Man',
            'boy',
            'Boy'])
    async def rt_male_name(self, ctx):
        embed = discord.Embed(description="Rolling for a male name...",
            color=0x0072ff)
        embed.add_field(name='Rolled Name',
            value=male_name())
        embed.set_footer(text="Bonfire Bot by TheOGMiyagi")
        await ctx.message.channel.send(embed=embed)
    # <--- Female Name Sub-Command --->
    @rt_character_names.command(name='female',
        pass_context=True,
        invoke_without_command=True,
        aliases=['Female',
            'woman',
            'Woman',
            'girl',
            'Girl'])
    async def rt_female_name(self, ctx):
        embed = discord.Embed(description="Rolling for a female name...",
            color=0x0072ff)
        embed.add_field(name='Rolled Name',
            value=female_name())
        embed.set_footer(text="Bonfire Bot by TheOGMiyagi")
        await ctx.message.channel.send(embed=embed)
    
    # <--- Random Class Sub-Command --->
    @roll_table.command(name='classes',
        pass_context=True,
        invoke_without_command=True,
        aliases=['Classes'])
    async def rt_lord_count(self, ctx):
        embed = discord.Embed(description="Rolling for a random player class...",
            color=0x0072ff)
        embed.add_field(name='Rolled Class',
            value=classes())
        embed.set_footer(text="Bonfire Bot by TheOGMiyagi")
        await ctx.message.channel.send(embed=embed)
    
    # <--- Covenant Name Sub-Command --->
    @roll_table.command(name='covenant_name',
        pass_context=True,
        invoke_without_command=True,
        aliases=['Covenant_Name',
            'covenant_names',
            'Covenant_Names'])
    async def rt_covenant_name(self, ctx):
        embed = discord.Embed(description="Rolling for a Covenant name...",
            color=0x0072ff)
        embed.add_field(name='Rolled Name',
            value=covenant_name())
        embed.set_footer(text="Bonfire Bot by TheOGMiyagi")
        await ctx.message.channel.send(embed=embed)
    
    # <--- Homeland Name Sub-Command --->
    @roll_table.command(name='homeland_name',
        pass_context=True,
        invoke_without_command=True,
        aliases=['Homeland_Name',
            'homeland_names',
            'Homeland_Names'])
    async def rt_homeland_name(self, ctx):
        embed = discord.Embed(description="Rolling for a homeland...",
            color=0x0072ff)
        embed.add_field(name='Rolled Homeland',
            value=homeland_name())
        embed.set_footer(text="Bonfire Bot by TheOGMiyagi")
        await ctx.message.channel.send(embed=embed)
    
    # <--- Land Name Sub-Command --->
    @roll_table.command(name='land_names',
        pass_context=True,
        invoke_without_command=True,
        aliases=['Land_Names',
            'land_name',
            'Land_Name'])
    async def rt_land_name(self, ctx):
        embed = discord.Embed(description="Rolling for a land name...",
            color=0x0072ff)
        embed.add_field(name='Rolled Name',
            value=land_name())
        embed.set_footer(text="Bonfire Bot by TheOGMiyagi")
        await ctx.message.channel.send(embed=embed)

    # <--- Location Info Sub-Command --->
    @roll_table.command(name='location_info',
        pass_context=True,
        invoke_without_command=True,
        aliases=['Location_Info'])
    async def rt_location_info(self, ctx):
        embed = discord.Embed(description="Rolling for a land name...",
            color=0x0072ff)
        embed.add_field(name=f'Rolled Location Information',
            value=location_info())
        embed.set_footer(text="Bonfire Bot by TheOGMiyagi")
        await ctx.message.channel.send(embed=embed)
    
    # <--- Lord Info Sub-Command --->
    @roll_table.command(name='lord_info',
        pass_context=True,
        invoke_without_command=True,
        aliases=['Lord_Info'])
    async def rt_lord_info(self, ctx):
        embed = discord.Embed(description="Rolling for Lord details...",
            color=0x0072ff)
        embed.add_field(name='Rolled Lord Information',
            value=lord_info(return_type='string'))
        embed.set_footer(text="Bonfire Bot by TheOGMiyagi")
        await ctx.message.channel.send(embed=embed)
    
    # <--- Lord Count Sub-Command --->
    @roll_table.command(name='lord_count',
        pass_context=True,
        invoke_without_command=True,
        aliases=['Lord_Count'])
    async def rt_lord_count(self, ctx):
        embed = discord.Embed(description="Rolling for the number of Lords...",
            color=0x0072ff)
        embed.add_field(name='Rolled Lord Count',
            value=number_of_lords())
        embed.set_footer(text="Bonfire Bot by TheOGMiyagi")
        await ctx.message.channel.send(embed=embed)
    
    # <--- Shard Of Memory Sub-Command --->
    @roll_table.command(name='shard_of_memory',
        pass_context=True,
        invoke_without_command=True,
        aliases=['shards_of_memory',
            'Shard_of_Memory',
            'Shard_Of_Memory'])
    async def rt_shard_of_memory(self, ctx):
        _shard_emotion, _shard_text = shard_of_memory()
        embed = discord.Embed(description="Rolling for a Shard Of Memory...",
            color=0x0072ff)
        embed.add_field(name=f'Shard Emotion: {_shard_emotion}',
            value=_shard_text)
        embed.set_footer(text="Bonfire Bot by TheOGMiyagi")
        await ctx.message.channel.send(embed=embed)