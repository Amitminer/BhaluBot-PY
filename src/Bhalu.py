import asyncio
from dotenv import load_dotenv
from Initializers.BotInitializer import BotInitializer

class BhaluBot:
    """
    Represents the Bhalu Discord bot.
    """

    @staticmethod
    async def run(on_or_off: bool) -> None:
        """
        Run the Bhalu bot either connecting or disconnecting it.
        """
        bhalu_init = BotInitializer()
        load_dotenv()

        try:
            if on_or_off:
                await bhalu_init.connect()
                print("Bot connected!")
            else:
                await bhalu_init.close()
                print("Bot closed.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    BOT = BhaluBot()
    asyncio.run(BOT.run(True))
