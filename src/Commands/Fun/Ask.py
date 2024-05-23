import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
from typing import Optional
from Manager.ChatManager import ChatManager
import aiohttp

class Ask(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
            
    @commands.command(aliases=["analyze", "searchImg", "chat"])
    @cooldown(1, 3, BucketType.user)
    async def ask(self, ctx: discord, *, question: Optional[str] = None):
        if not question and not ctx.message.attachments:
            await ctx.message.reply("You need to ask something or attach an image")
            return
        
        try:
            await ctx.channel.typing()
            
            if ctx.message.attachments:
                await self.process_image_attachments(ctx, question)
            else:
                response = await ChatManager().ask_gemini_ai(question)
                await self.send_split_message(ctx, response)
                
        except Exception as e:
            await ctx.send(f"An error occurred: {e}", delete_after=3)

    async def process_image_attachments(self, ctx, question: Optional[str] = None):
        for attachment in ctx.message.attachments:
             if await self.is_valid_image_extension(attachment.filename.lower()):
                image_data = await self.download_image(attachment.url)
                if image_data:
                    response_text = await ChatManager().generate_response_with_image_and_text(image_data, question)
                    if response_text:
                        await self.send_split_message(ctx, response_text)
                else:
                    await ctx.send('Unable to download the image.')

    async def is_valid_image_extension(self, filename: Optional[str] = None) -> bool:
        valid_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.webp']
        return any(filename.endswith(ext) for ext in valid_extensions)

    async def download_image(self, url: Optional[str] = None):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    return await resp.read()
                else:
                    return None

    async def send_split_message(self, ctx, response: Optional[str] = None):
        max_message_length = 1900
        
        if response is None:
            return
        
        if len(response) <= max_message_length:
            await ctx.message.reply(response)
        else:
            chunks = [response[i:i+max_message_length] for i in range(0, len(response), max_message_length)]
            for chunk in chunks:
                await ctx.message.reply(chunk)
                
    @commands.Cog.listener(name="on_message")
    async def on_mentions(self, message):
        if message.author == self.bot.user:
            return 
    
        if self.bot.user in message.mentions:
            ctx = await self.bot.get_context(message)
            await ctx.invoke(self.bot.get_command("ask"), question=message.content)

    
    @commands.command(aliases=["deletechat", "clearchat", "deletehistory"])
    async def clear(self, ctx):
        try:
            ChatManager().delete_data()
            await ctx.message.reply("Chat history deleted successfully.")
            await ctx.message.delete()
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
            
async def setup(bot):
    await bot.add_cog(Ask(bot))
