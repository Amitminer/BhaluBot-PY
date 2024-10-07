from discord.ext import commands
import discord


class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Fake Ban a user from the server xD."""
        try:
            await ctx.send(f"{member} has been banned. Reason: {reason}")
        except Exception as e:
            await ctx.send(f"Error banning user: {e}")


async def setup(client):
    await client.add_cog(Ban(client))
