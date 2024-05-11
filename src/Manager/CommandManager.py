from discord import Client

class CommandManager:
    # Array of available commands
    Commands = [
        "Ping",
        "Say",
        "RandomImage"
    ]

    def __init__(self):
        pass

    @staticmethod
    async def register_all(client: Client) -> None:
        for command_name in CommandManager.Commands:
            cog_name = f"Commands.{command_name}"
            try:
                await client.load_extension(cog_name)
                print(f"{command_name} command loaded.")
            except Exception as e:
                print(f"Failed to load {command_name} command: {e}")
