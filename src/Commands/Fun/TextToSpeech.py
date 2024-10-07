import discord
from discord.ext import commands
from gtts import gTTS
import os
import random
import string
import aiofiles
import aiofiles.os
from typing import Tuple, Optional

class TTS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.supported_languages = {'en', 'in', 'fr', 'es', 'de', 'it', 'ja', 'ko', 'zh-cn'}

    @commands.command()
    async def tts(self, ctx, *, args: str = None):
        """
        Generates a TTS audio file from the given text and sends it in the channel.

        Usage:
        - ++tts "hello guys"
        - ++tts en "hello guys"
        - ++tts en "hello guys" -f "filename"
        """
        if not args:
            await ctx.send("You must provide text to convert to speech. Usage: `++tts [lang] \"text\" [-f filename]`")
            return

        try:
            lang, text, file_name = await self.parse_args(args)
            file_path = await self.create_tts_file(ctx, text, lang, file_name)
            if file_path:
                await self.send_tts_file(ctx, file_path)
                await self.cleanup_file(file_path)
        except ValueError as e:
            await ctx.send(str(e))

    async def parse_args(self, args: str) -> Tuple[str, str, Optional[str]]:
        parts = args.split(maxsplit=1)
        
        if len(parts) == 1:
            return 'en', parts[0], None

        if parts[0].lower() in self.supported_languages:
            lang = parts[0].lower()
            rest = parts[1]
        else:
            lang = 'en'
            rest = args

        if '"' in rest:
            text, *rest = rest.split('"')[1:]
            text = text.strip()
        else:
            text, *rest = rest.split(maxsplit=1)

        file_name = None
        if rest and rest[0].startswith('-f'):
            file_name = rest[0].split('-f', 1)[1].strip()
            if not file_name:
                raise ValueError("Filename cannot be empty when using -f flag.")

        if not text:
            raise ValueError("Text to convert to speech cannot be empty.")

        return lang, text, file_name

    def generate_random_filename(self):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

    async def create_tts_file(self, ctx, text: str, lang: str, file_name: str):
        try:
            output_dir = "./.temp"
            await aiofiles.os.makedirs(output_dir, exist_ok=True)
            file_name = file_name or self.generate_random_filename()
            file_path = os.path.join(output_dir, f"{file_name}.mp3")

            tts = gTTS(text=text, lang=lang)
            tts.save(file_path)
            return file_path

        except ValueError:
            raise ValueError(f"Invalid language '{lang}'. Supported languages are: {', '.join(self.supported_languages)}")
        except Exception as e:
            raise ValueError(f"An error occurred during TTS generation: {str(e)}")

    async def send_tts_file(self, ctx, file_path: str):
        try:
            await ctx.message.reply(file=discord.File(file_path))
        except Exception as e:
            raise ValueError(f"An error occurred while sending the file: {str(e)}")

    async def cleanup_file(self, file_path: str):
        try:
            await aiofiles.os.remove(file_path)
        except Exception as e:
            print(f"Failed to delete the file {file_path}: {e}")

async def setup(bot):
    await bot.add_cog(TTS(bot))