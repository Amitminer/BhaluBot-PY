"""
This module defines the BhaluBot class for interacting with the Discord API.
"""

import asyncio
import logging
from dotenv import load_dotenv
from Initializers.BotInitializer import BotInitializer

class BhaluBot:
    """
    Represents the Bhalu Discord bot.
    Handles connecting and disconnecting the bot to the Discord server.
    """

    def __init__(self):
        """
        Initialize the BhaluBot by setting up and loading environment variables.
        """
        load_dotenv()
        self.bhalu_init = BotInitializer()
        # Setting up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    async def run(self, connect: bool) -> None:
        """
        Run the Bhalu bot either connecting or disconnecting it.

        Parameters:
        connect (bool): If True, connect the bot. If False, disconnect the bot.
        """
        try:
            if connect:
                self.logger.info("Connecting the bot...")
                await self.bhalu_init.connect()
                self.logger.info("Bot connected successfully.")
            else:
                self.logger.info("Disconnecting the bot...")
                await self.bhalu_init.close()
                self.logger.info("Bot disconnected successfully.")
        except (ConnectionError, TimeoutError) as e:  # Catch specific exceptions
            self.logger.error("An error occurred: %s", e, exc_info=True)

if __name__ == "__main__":
    bot = BhaluBot()
    asyncio.run(bot.run(connect=True))  # Pass `True` to connect, `False` to disconnect
