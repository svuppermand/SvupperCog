import discord
from discord.ext import commands

class summon:
    """summon command"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def summon(self,voice_channel):
        """This does stuff!"""

        #simple command
        self.bot.join_voice_channel(voice_channel)
        self.move_voice_client(voice_channel)
        await self.bot.say("channel joined !")

def setup(bot):
    bot.add_cog(summon(bot))
