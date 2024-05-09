from discord.ext import commands
from Manager.ImageManager import ImageManager

class RandomImage(commands.Cog):
    
    def __init__(self, client):
        self.client = client
           

    @commands.command()
    async def random(self, ctx, *, query: str):
        try:
            await ctx.channel.typing()
            
            for _ in range(5):  # Loop five times to send 5 URLs
                image_url = await ImageManager.get_random_image(query)
                await ctx.message.reply(image_url)
      
        except Exception as e:
            await ctx.channel.typing()
            await ctx.message.reply(f"An error occurred: {e}. Please try again later.")

async def setup(client):
    await client.add_cog(RandomImage(client))
