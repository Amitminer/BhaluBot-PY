from discord.ext import commands

class CommandManager:
    
    COMMANDS = {
        "General": ["Ping", "Say", "Spam", "Help"],
        "Fun": ["Ask", "Imagine", "Ship"],
        "Utility": ["SearchImage", "Summarizer"],
        "Admin": ["Shutdown"]
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
                    print(f"+ {command_name} command loaded in {category} category.")
                except Exception as e:
                    print(f"Failed to load {command_name} command in {category} category: {e}")
