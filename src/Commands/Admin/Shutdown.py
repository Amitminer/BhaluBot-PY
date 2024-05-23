from discord.ext import commands
from Initializers.BotInitializer import BotInitializer
from Manager.ConfigManager import ConfigManager

class Shutdown(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
    def is_owner(ctx):
     return ctx.author.id in ConfigManager.get_authors()

    @commands.command(name='shutdown', hidden=True)
    @commands.is_owner()
    async def shutdown_bot(self, ctx):
        """
        Shuts down the bot
        """
        await ctx.send('Shutting down...')
        print("Shutting down bot...")
        await BotInitializer.close(self.client)

async def setup(client):
    await client.add_cog(Shutdown(client))
