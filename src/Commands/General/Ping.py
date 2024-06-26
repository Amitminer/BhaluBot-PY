from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.client.latency * 1000)}ms')


async def setup(client):
    await client.add_cog(ping(client))