import discord
from discord.ext import commands
import time

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        try:
            start_time = time.time()
            message = await ctx.send("Pinging...")
            end_time = time.time()

            bot_latency = round(self.client.latency * 1000)
            api_latency = round((end_time - start_time) * 1000)

            embed = discord.Embed(title="Ping Results", color=discord.Color.green())
            embed.add_field(name="Bot Latency", value=f"{bot_latency}ms", inline=False)
            embed.add_field(name="API Latency", value=f"{api_latency}ms", inline=False)

            await message.edit(content=None, embed=embed)
        except Exception as e:
            await ctx.send(f"An error occurred while checking ping: {str(e)}")

async def setup(client):
    await client.add_cog(Ping(client))