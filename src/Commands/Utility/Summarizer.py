import re
from discord.ext import commands
import aiohttp
from bs4 import BeautifulSoup
from Manager.ChatManager import ChatManager

class Summarizer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    @commands.command()
    async def summarize(self, ctx, *, content):
        """Summarizes the given URL content or paragraph and replies with the summary."""
        if not content:
            await ctx.reply("Please provide a website link or a paragraph to summarize.")
            return

        async with ctx.typing():
            try:
                if self.url_pattern.match(content):
                    summarized_text = await self.summarize_url(content)
                else:
                    summarized_text = await self.summarize_text(content)

                if len(summarized_text) > 2000:
                    chunks = [summarized_text[i:i+2000] for i in range(0, len(summarized_text), 2000)]
                    for chunk in chunks:
                        await ctx.reply(chunk)
                else:
                    await ctx.reply(summarized_text)

            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
                await ctx.reply(error_message)

    async def summarize_url(self, url):
        """Fetches the content of the URL, extracts the text, and summarizes it."""
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise Exception(f"Failed to retrieve the webpage. Status code: {response.status}")
                html_content = await response.text()

        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Try to get the main content, fallback to all paragraphs if not found
        main_content = soup.find('main') or soup.find('article') or soup
        paragraphs = main_content.find_all('p')
        
        text_content = ' '.join([para.get_text() for para in paragraphs])

        if len(text_content) < 100:
            raise Exception("The extracted content is too short to summarize.")

        return await self.summarize_text(text_content, is_url=True)

    async def summarize_text(self, content, is_url=False):
        """Summarizes the given text content."""
        prefix = "summarize this webpage content:" if is_url else "summarize this paragraph:"
        prompt = f"{prefix} \"{content}\""

        summarized_text = await ChatManager().ask_gemini_ai(prompt)
        
        if not summarized_text:
            raise Exception("Failed to generate a summary. The AI response was empty.")

        return summarized_text

async def setup(bot):
    """Sets up the Summarizer cog."""
    await bot.add_cog(Summarizer(bot))