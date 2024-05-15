from discord.ext import commands
from Manager.ChatManager import ChatManager
import aiohttp

class Ask(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ask(self, ctx, *, question=''):
        # Check if the message contains text or attachments
        if not question.strip() and not ctx.message.attachments:
            await ctx.send("You need to ask something or attach an image")
            return
        
        try:
            await ctx.channel.typing()  # Start typing indication
            
            if ctx.message.attachments:  # If message contains attachments
                await self.process_image_attachments(ctx, question)
            else:  # If no attachments, generate response based on text
                response = await ChatManager().ask_gemini_ai(question)
                await self.send_split_message(ctx, response)
                
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    async def process_image_attachments(self, ctx, question):
        """
        Process image attachments and generate a response.
        """
        for attachment in ctx.message.attachments:
            if any(attachment.filename.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp']):
                async with aiohttp.ClientSession() as session:
                    async with session.get(attachment.url) as resp:
                        if resp.status != 200:
                            await ctx.send('Unable to download the image.')
                            return
                        image_data = await resp.read()
                        response_text = await ChatManager().generate_response_with_image_and_text(image_data, question)
                        await self.send_split_message(ctx, response_text)

    async def send_split_message(self, ctx, response):
        """
        Split the response message into multiple messages if it exceeds Discord's message length limit.
        """
        max_message_length = 1900
        if len(response) <= max_message_length:
            await ctx.message.reply(response)
        else:
            chunks = [response[i:i+max_message_length] for i in range(0, len(response), max_message_length)]
            for chunk in chunks:
                await ctx.message.reply(chunk)
    
    @commands.command()
    async def deletechat(self, ctx):
        """
        Delete chat history and reset data.
        """
        try:
            ChatManager().delete_data()
            await ctx.send("Chat history deleted successfully.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
            
async def setup(bot):
    await bot.add_cog(Ask(bot))
