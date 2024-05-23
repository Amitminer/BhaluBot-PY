import discord
from discord.ext import commands
import requests
import base64
import os
import aiofiles
import aiofiles.os
import asyncio
from concurrent.futures import ThreadPoolExecutor

class Imagine(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.engine_id = "stable-diffusion-v1-6"
        self.api_host = "https://api.stability.ai"
        self.api_key = "sk-noiyo2S3CmvptDLssOqe6uvdSrYRXj3B9XxcGC4C95GqDoBQ"
        self.executor = ThreadPoolExecutor(max_workers=3)

    @commands.command()
    async def imagine(self, ctx: commands.Context, *, text: str):
        if not text:
            await ctx.reply("Please provide a query to generate an image.")
            return
        await ctx.reply("Generating image... Please wait...", delete_after=5)

        try:
            response = await asyncio.get_event_loop().run_in_executor(
                self.executor,
                self.generate_image,
                text
            )

            if response.status_code != 200:
                raise Exception(f"Non-200 response: {response.text}")

            data = response.json()
            image_path = await self.save_image(data)
            
            if image_path:
                await ctx.reply("Here is your generated image:", file=discord.File(image_path))
                await aiofiles.os.remove(image_path)  # Delete the image file after sending it
            else:
                await ctx.reply("Failed to generate image. Please try again later.")
        except Exception as e:
            await ctx.reply(f"An error occurred: {str(e)}")

    def generate_image(self, text):
        return requests.post(
            f"{self.api_host}/v1/generation/{self.engine_id}/text-to-image",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
            json={
                "text_prompts": [{"text": text}],
                "cfg_scale": 7,
                "height": 512,  # Adjusted for faster generation
                "width": 512,   # Adjusted for faster generation
                "samples": 1,
                "steps": 30,
            },
        )

    async def save_image(self, data):
        output_dir = "./.temp"
        await aiofiles.os.makedirs(output_dir, exist_ok=True)
        
        for i, image in enumerate(data["artifacts"]):
            image_data = base64.b64decode(image["base64"])
            image_path = os.path.join(output_dir, f"img_{i}.png")
            async with aiofiles.open(image_path, "wb") as f:
                await f.write(image_data)
            # print(f"Saved image {i} to {image_path}")
            return image_path

async def setup(bot):
    await bot.add_cog(Imagine(bot))
