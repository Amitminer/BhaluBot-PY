import discord
from discord.ext import commands
from Manager.ConfigManager import ConfigManager


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        prefix = ConfigManager().get_prefix()

        embed = discord.Embed(title="Bot Commands", color=0x00FF00)

        general_commands = f"""
        **General:**
        - `{prefix}say "your message"`: Make the bot say something.
            - Example: `{prefix}say Hello!`
        - `{prefix}ping`: Check the bot's latency.
            - Example: `{prefix}ping`
        - `{prefix}spam {{count}} "your message to spam"`: Spam a message a certain number of times.
            - Example: `{prefix}spam 5 "Spamming message"`
        """
        fun_commands = f"""
        **Fun:**
        - `{prefix}ask "your question to ask ai!"`: Ask a question to the AI.
            - Example: `{prefix}ask What is the meaning of life?`
        - `{prefix}imagine "your query"`: Generate an AI-generated image based on the query.
            - Example: `{prefix}imagine sunset`
        - `{prefix}ship [user1] [user2]`: Ship two users together.
            - Example: `{prefix}ship @User1 @User2`
        """
        utility_commands = f"""
        **Utility:**
        - `{prefix}search count "your query"`: Get a random image related to your query.
            - Example: `{prefix}search count cat`
        - `{prefix}summarize "link or big paragraph"`: Summarize a link or a big paragraph.
            - Example: `{prefix}summarize "https://example.com"`
        """

        embed.add_field(name="General Commands", value=general_commands, inline=False)
        embed.add_field(name="Fun Commands", value=fun_commands, inline=False)
        embed.add_field(name="Utility Commands", value=utility_commands, inline=False)

        await ctx.message.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot))
