import discord
from discord.ext import commands
import aiohttp


class Food(commands.Cog):
    """
    A Cog for fetching random food images and listing food categories.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="food")
    async def food(self, ctx, category: str = None):
        """
        Sends a random food image. Optionally, provide a category to get an image from that category.
        Usage: ++food [category]
        """
        base_url = "https://foodish-api.com/api/"
        url = f"{base_url}images/{category.lower()}" if category else f"{base_url}images/random"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        await ctx.send("Failed to retrieve food image. Please try again.")
                        return

                    data = await response.json()
                    image_url = data.get("image")

                    if not image_url:
                        await ctx.send("No image found. Please try again.")
                        return

                    embed = discord.Embed(
                        title="Here's a delicious food image for you!", color=0xFFA500
                    )
                    embed.set_image(url=image_url)

                    await ctx.message.reply(embed=embed)
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    @commands.command(name="foodlist")
    async def foodlist(self, ctx):
        """
        Sends a list of food categories and their respective counts.
        """
        food_categories = {
            "biryani": 81,
            "burger": 87,
            "butter-chicken": 22,
            "dessert": 36,
            "dosa": 83,
            "idly": 77,
            "pasta": 34,
            "pizza": 95,
            "rice": 35,
            "samosa": 22,
        }

        total_foodishes = sum(food_categories.values())
        description = "\n".join([f"{category}: {count}" for category, count in food_categories.items()])
        description += f"\n\nTotal Foodishes: {total_foodishes}"

        embed = discord.Embed(
            title="Food Categories and Counts", description=description, color=0x00FF00
        )
        await ctx.message.reply(embed=embed)

    @commands.command()
    async def geturl(self, ctx, emoji: discord.Emoji):
        """
        Sends the URL of the provided emoji.
        Usage: ++geturl <emoji>
        """
        await ctx.message.reply(f"URL: {emoji.url}")


async def setup(bot):
    await bot.add_cog(Food(bot))
