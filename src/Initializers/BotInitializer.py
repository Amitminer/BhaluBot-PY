import discord
from discord.ext import commands
from Manager.ConfigManager import ConfigManager
from Manager.CommandManager import CommandManager
from Utils.colors import Colors
from VersionInfo import VersionInfo


class BotInitializer(Colors, VersionInfo):
    """
    Initializes and manages the Discord bot.
    """

    def __init__(self):
        super().__init__()
        self.discord = None

    def init(self):
        """
        Initialize the Discord bot.
        """
        # Get bot token from environment variables
        prefix = ConfigManager.get_prefix()

        # Define intents for the Discord client
        intents = discord.Intents.default()
        intents.message_content = True

        # Initialize Discord bot with defined intents
        self.discord = commands.Bot(
            command_prefix=prefix,
            help_command=None,
            case_insensitive=True,
            self_bot=False,
            intents=intents,
        )

        @self.discord.event
        async def on_ready():
            # Register all commands when the bot is ready
            await CommandManager.register_all(self.discord)
            await self.discord.change_presence(
                status=discord.Status.dnd,
                activity=discord.Activity(
                    name="github.com/Amitminer", type=discord.ActivityType.watching
                ),
            )
            await self.send_login_message()

        @self.discord.event
        async def on_command_error(ctx, error):
            if isinstance(error, commands.CommandNotFound):
                await ctx.message.reply(
                    f"Command not found. Use `{prefix}help` to see available commands."
                )
            else:
                # For any other errors, raise the error to allow default handling
                raise error

    async def send_login_message(self):
        """
        Send a login message to the console.
        """
        green = self.GREEN
        yellow = self.YELLOW
        blue = self.BLUE
        reset = self.RESET

        # Print login message to console
        print(green + "Bot is Now Online!")
        print(green + "Version:", VersionInfo.get_version())
        print(green + "Logged in as " + yellow + self.discord.user.name + reset)
        print(blue + "Made by AmitxD" + reset)

    async def connect(self):
        """
        Connect the bot to Discord.
        """
        # Initialize and start the bot
        token = ConfigManager.get_bot_token()
        self.init()
        await self.discord.start(token)

    async def close(self):
        """
        Close the bot.
        """
        # Close the bot
        await self.discord.close()


if __name__ == "__main__":
    # Create BotInitializer instance and connect the bot
    bot_init = BotInitializer()
    bot_init.connect()
