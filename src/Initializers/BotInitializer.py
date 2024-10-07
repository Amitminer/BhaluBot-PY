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
        self.discord = None  # The Discord client

    def init(self):
        """
        Initialize the Discord bot with appropriate configurations.
        """
        # Get bot command prefix from configuration
        prefix = ConfigManager.get_prefix()

        # Define intents for the Discord client
        intents = discord.Intents.default()
        intents.message_content = True

        # Initialize the bot with command prefix, no help command, and defined intents
        self.discord = commands.Bot(
            command_prefix=prefix,
            help_command=None,
            case_insensitive=True,
            self_bot=False,
            intents=intents,
        )

        # Register events when bot is ready
        @self.discord.event
        async def on_ready():
            await self._on_ready_handler()

        # Handle command errors
        @self.discord.event
        async def on_command_error(ctx, error):
            await self._on_command_error_handler(ctx, error)

    async def _on_ready_handler(self):
        """
        Handler function to be executed when the bot is ready.
        """
        await CommandManager.register_all(self.discord)
        await self.discord.change_presence(
            status=discord.Status.dnd,
            activity=discord.Activity(
                name="github.com/Amitminer", type=discord.ActivityType.watching
            ),
        )
        await self.send_login_message()

    async def _on_command_error_handler(self, ctx, error):
        """
        Handle command errors.

        Parameters:
        ctx: The context in which the command was invoked.
        error: The exception that was raised.
        """
        prefix = ConfigManager.get_prefix()
        if isinstance(error, commands.CommandNotFound):
            await ctx.message.reply(
                f"Command not found. Use `{prefix}help` to see available commands."
            )
        else:
            # Raise any unhandled exceptions to the default handler
            raise error

    async def send_login_message(self):
        """
        Display a login message in the console when the bot successfully logs in.
        """
        green = self.GREEN
        yellow = self.YELLOW
        blue = self.BLUE
        cyan = self.CYAN
        reset = self.RESET

        # Print bot login details to console
        print(f"{cyan}Bot is Now Online!")
        print(f"{green}Version: {VersionInfo.get_version()}")
        print(f"{green}Logged in as {yellow}{self.discord.user.name}{reset}")
        print(f"{blue}Made by AmitxD{reset}")

    async def connect(self):
        """
        Asynchronously connect the bot to Discord.
        """
        token = ConfigManager.get_bot_token()
        self.init()  # Initialize bot settings
        await self.discord.start(token)

    async def close(self):
        """
        Asynchronously close the bot connection to Discord.
        """
        await self.discord.close()

