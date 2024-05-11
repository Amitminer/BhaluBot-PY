from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def say(self, ctx, *, text=''):
        if text == '':
            await ctx.send("You need to say something")
        else:
            await ctx.send(text)
            await ctx.message.delete()  # Delete the command message

async def setup(client):
    await client.add_cog(Say(client))
