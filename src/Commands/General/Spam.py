from discord.ext import commands

class Spam(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def spam(self, ctx, count: int, *, message: str):
        if count <= 0 or count > 2:
            await ctx.send('Count must be a positive number and smaller than or equal to 10.')
            return

        if len(message) > 2000:
            await ctx.send('Message length must not exceed 2000 characters.')
            return

        try:
            for _ in range(count):
                await ctx.send(message)
            #  await ctx.message.delete()
        except Exception as e:
            print(f"An error occurred while sending messages: {e}")
            await ctx.send('An error occurred while sending messages. Please try again later.')

async def setup(bot):
    await bot.add_cog(Spam(bot))

