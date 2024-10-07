from discord.ext import commands
from Manager.ImageManager import ImageManager

class SearchImage(commands.Cog):
    
    def __init__(self, client):
        self.client = client
           
    @commands.command()
    async def search(self, ctx, *, query: str):
        try:
            await ctx.channel.typing()
            
            # Split the query to check for an optional count at the beginning
            parts = query.split(maxsplit=1)
            
            if len(parts) > 1 and parts[0].isdigit():
                count = int(parts[0])
                query = parts[1]
            else:
                count = 1  # Default value
            
            if count < 5:
                for _ in range(count):
                    image_url = await ImageManager.get_image(query)
                    await ctx.message.reply(image_url)
            else:
                await ctx.message.reply("Bhai mat kar :/")
                
        except Exception as e:
            await ctx.channel.typing()
            await ctx.message.reply(f"An error occurred: {e}. Please try again later.")

async def setup(client):
    await client.add_cog(SearchImage(client))