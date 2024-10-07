from discord.ext import commands
from Utils.colors import Colors
class CommandManager:

    COMMANDS = {
        "General": ["Ping", "Say", "Spam", "Help"],
        "Fun": ["Ask", "Imagine", "Ship", "Hack", "Food", "TextToSpeech"],
        "Utility": ["SearchImage", "Summarizer", "Currency"],
        "Admin": ["Shutdown", "Ban"],
    }

    def __init__(self):
        pass

    @staticmethod
    async def register_all(client: commands.Bot) -> None:
        """
        Register all commands with the provided client.
        """
        for category, commands_list in CommandManager.COMMANDS.items():
            for command_name in commands_list:
                cog_name = f"Commands.{category}.{command_name}"
                try:
                    await client.load_extension(cog_name)
                    print(f"{Colors.GREEN} + {command_name} command loaded in {category} category.")
                except Exception as e:
                    print(f"{Colors.RED} Failed to load {command_name} command in {category} category: {e}")
