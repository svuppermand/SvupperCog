import discord
from discord.ext import commands

class summon:
    """summon command"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def summon(self,channel):
        """This does stuff!"""

        #Your code will go here
        self.bot.join_voice_channel(channel)
        await self.bot.say("I can do stuff!")

def setup(bot):
    bot.add_cog(summon(bot))
