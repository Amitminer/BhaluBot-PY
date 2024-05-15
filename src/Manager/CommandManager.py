from discord import Client
from Utils.colors import Colors

class CommandManager:
    """
    Manages the registration of commands in the bot.
    """
    # List of available commands
    COMMANDS = [
        "Ping",
        "Say",
        "SearchImage",
        "Spam",
        "Ask"
    ]

    def __init__(self):
        pass

    @staticmethod
    async def register_all(client: Client) -> None:
        """
        Register all commands with the provided client.
        """
        for command_name in CommandManager.COMMANDS:
            cog_name = f"Commands.{command_name}"
            try:
                green = Colors.GREEN
                await client.load_extension(cog_name)
                print(f"{green} + {command_name} command loaded.")
            except Exception as e:
                red = Colors.RED
                print(f"{red} + Failed to load {command_name} command: {e}")
