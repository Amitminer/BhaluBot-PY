import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, category=None):
        prefix = self.bot.command_prefix
        embed = discord.Embed(title="Bot Commands", color=discord.Color.blue())

        categories = {
            "admin": {
                "description": "Administrative commands",
                "commands": {
                    "ban": f"{prefix}ban @user1 @user2 [reason] - Simulates banning users (for fun)",
                    "shutdown": f"{prefix}shutdown - Shuts down the bot (owner only)"
                }
            },
            "fun": {
                "description": "Entertainment commands",
                "commands": {
                    "ask": f"{prefix}ask [question] - Ask the bot a question (AI-powered)",
                    "food": f"{prefix}food [category] - Get a random food image",
                    "foodlist": f"{prefix}foodlist - List all available food categories",
                    "hack": f"{prefix}hack @user - Simulate hacking a user (prank)",
                    "imagine": f"{prefix}imagine [prompt] - Generate an image based on prompt (AI-powered)",
                    "ship": f"{prefix}ship @user1 @user2 - Ship two users with a compatibility percentage",
                    "tts": f"{prefix}tts [language] [text] [-f filename] - Generate and send a TTS audio file"
                }
            },
            "general": {
                "description": "General purpose commands",
                "commands": {
                    "ping": f"{prefix}ping - Check bot's latency",
                    "say": f"{prefix}say [message] - Make the bot say a message",
                    "help": f"{prefix}help [category] - Show this help message"
                }
            },
            "utility": {
                "description": "Useful utility commands",
                "commands": {
                    "currency": f"{prefix}currency [from] [to] [amount] - Convert currency",
                    "search": f"{prefix}search [number] [query] - Search for images",
                    "summarize": f"{prefix}summarize [url/text] - Summarize content from a URL or text"
                }
            }
        }

        if category and category.lower() in categories:
            cat = categories[category.lower()]
            embed.description = cat["description"]
            for cmd, desc in cat["commands"].items():
                embed.add_field(name=cmd.capitalize(), value=desc, inline=False)
        else:
            embed.description = "Use `{}help [category]` for more details on each category.".format(prefix)
            for cat, data in categories.items():
                embed.add_field(name=cat.capitalize(), value=data["description"], inline=False)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))