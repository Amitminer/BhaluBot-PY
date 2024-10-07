import discord
from discord.ext import commands
import aiofiles
from Manager.ImageManager import ImageManager

class Imagine(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def imagine(self, ctx: commands.Context, *, text: str):
        if not text:
            await ctx.reply("Please provide a query to generate an image.")
            return
        
        await ctx.reply("Generating image... Please wait...", delete_after=5)

        try:
            image_path = await ImageManager.generate_image(text)

            if image_path:
                await ctx.reply("Here is your generated image:", file=discord.File(image_path))
                await aiofiles.os.remove(image_path)
            else:
                await ctx.reply("Failed to generate image. Please try again later.")
        except Exception as e:
            await ctx.reply(f"An error occurred: {str(e)}")

async def setup(bot):
    await bot.add_cog(Imagine(bot))