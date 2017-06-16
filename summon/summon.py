import discord
from discord.ext import commands

class summon:
    """summon command"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def summon(self, channel, author, voice_channel):
       """
        Usage:
            {command_prefix}summon
        Call the bot to the summoner's voice channel.
        """

        if not author.voice_channel:
            raise exceptions.CommandError('You are not in a voice channel!')

        voice_client = self.the_voice_clients.get(channel.server.id, None)
        if voice_client and voice_client.channel.server == author.voice_channel.server:
            await self.move_voice_client(author.voice_channel)
            await self.bot.say("channel joined !")
            return

        

def setup(bot):
    bot.add_cog(summon(bot))
