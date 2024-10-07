import discord
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, text: str = None):
        try:
            if text is None:
                await ctx.send("You need to provide a message for me to say.")
                return

            if len(text) > 2000:
                await ctx.send("The message is too long. Please keep it under 2000 characters.")
                return

            await ctx.message.delete()  # Delete the command message
            await ctx.send(text)
        except discord.errors.Forbidden:
            await ctx.send("I don't have permission to delete messages or send messages in this channel.")
        except Exception as e:
            await ctx.send(f"An error occurred while processing the command: {str(e)}")

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to use this command.")

async def setup(client):
    await client.add_cog(Say(client))