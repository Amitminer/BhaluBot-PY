from Initializers.BotInitializer import BotInitializer
from dotenv import load_dotenv
import asyncio

class BhaluBot:
    
    def __init__(self):
        pass

    @staticmethod
    async def run(on_or_off: bool) -> None: 
        bhalu_init = BotInitializer()
        load_dotenv()
        try:
            if on_or_off:
                await bhalu_init.connect()  # Await the connect method
                print("Bot connected!")
            else:
                await bhalu_init.close()  # Await the close method
                print("Bot closed.")
        except Exception as e:
            print("An error occurred:", e)
            

if __name__ == "__main__":
    bot = BhaluBot()
    asyncio.run(bot.run(True)) 
