from discord import Client

class CommandManager:
    """
    Manages the registration of commands in the bot.
    """
    # List of available commands
    COMMANDS = [
        "Ping",
        "Say",
        "RandomImage",
        "Spam"
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
                await client.load_extension(cog_name)
                print(f"{command_name} command loaded.")
            except Exception as e:
                print(f"Failed to load {command_name} command: {e}")
