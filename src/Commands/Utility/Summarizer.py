from discord.ext import commands
import aiohttp
from bs4 import BeautifulSoup
from Manager.ChatManager import ChatManager

class Summarizer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def summarize(self, ctx, *, content):
        """Summarizes the given URL content or paragraph and replies with the summary."""
        if not content:
            await ctx.message.reply("You need to give me a website link or a paragraph to summarize it.")
            return

        try:
            await ctx.channel.typing()
            if content.startswith("http://") or content.startswith("https://"):
                # Handle URL
                summarized_text = await self.summarize_url(content)
            else:
                summarized_text = await ChatManager().ask_gemini_ai(f"summarize this paragraph \"{content}\'")

            await ctx.message.reply(summarized_text)
        except Exception as e:
            print(e)
            await ctx.send(f"An error occurred: {e}", delete_after=10)

    async def summarize_url(self, url):
        """Fetches the content of the URL, extracts the text, and summarizes it."""
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise Exception(f"Failed to retrieve the webpage. Status code: {response.status}")
                html_content = await response.text()

        # Extract the text from the HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        paragraphs = soup.find_all('p')
        text_content = ' '.join([para.get_text() for para in paragraphs])

        # Call the summarization API (using ChatManager)
        summarized_text = await ChatManager().ask_gemini_ai(f"summarize this paragraph/blog: \"{text_content}\"")
        
        if not summarized_text:
            raise Exception("Failed to summarize the text. The summarization response was empty.")

        return summarized_text

async def setup(bot):
    """Sets up the Summarizer cog."""
    await bot.add_cog(Summarizer(bot))

