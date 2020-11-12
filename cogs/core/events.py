import discord
from discord.ext import commands


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Event triggered when the bot's cache is loaded"""

        print("\nONLINE\n")
        

def setup(bot):
    bot.add_cog(Events(bot))
