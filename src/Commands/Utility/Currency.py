import discord
from discord.ext import commands
import requests
from datetime import datetime


class Currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.country_to_currency = {
            "india": "INR",
            "united states": "USD",
            "usa": "USD",
            "america": "USD",
            "europe": "EUR",
            "united kingdom": "GBP",
            "uk": "GBP",
            "japan": "JPY",
            "china": "CNY",
            "canada": "CAD",
            "australia": "AUD",
            "switzerland": "CHF",
            "south africa": "ZAR",
            "russia": "RUB",
            "brazil": "BRL",
            "mexico": "MXN",
            "new zealand": "NZD",
            "singapore": "SGD",
            "south korea": "KRW",
            "turkey": "TRY",
            "saudi arabia": "SAR",
            "argentina": "ARS",
            "nigeria": "NGN",
            "indonesia": "IDR",
            "thailand": "THB",
            "malaysia": "MYR",
        }

    def get_currency_code(self, country_name: str):
        """
        Get the currency code for a given country name.
        """
        currency_code = self.country_to_currency.get(country_name.lower())
        if not currency_code:
            similar_countries = ", ".join([c.title() for c in self.country_to_currency.keys()])
            return None, similar_countries
        return currency_code, None

    @commands.command(name="currency", aliases=["convert"])
    async def currency(self, ctx, from_country: str, to_country: str, amount: float):
        """
        Convert currency from one to another.
        Usage: !currency india america 100
        """
        from_currency, from_suggestions = self.get_currency_code(from_country)
        to_currency, to_suggestions = self.get_currency_code(to_country)

        if not from_currency:
            await ctx.send(
                f"Invalid country name '{from_country}' provided. Did you mean one of these: {from_suggestions}?"
            )
            return

        if not to_currency:
            await ctx.send(
                f"Invalid country name '{to_country}' provided. Did you mean one of these: {to_suggestions}?"
            )
            return

        url = f"https://api.fxratesapi.com/convert?from={from_currency}&to={to_currency}&amount={amount}&format=json"

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code != 200 or not data.get("success", False):
                await ctx.send(
                    f"Error fetching exchange rate: {data.get('error', 'Unknown error')}"
                )
                return

            # Extract relevant information from the response
            exchange_rate = data["info"]["rate"]
            converted_amount = data["result"]
            date = datetime.fromisoformat(data["date"].replace("Z", "+00:00")).strftime(
                "%Y-%m-%d %H:%M:%S UTC"
            )

            # Create an embed for better display in Discord
            embed = discord.Embed(title="Currency Conversion", color=0x00FF00)
            embed.add_field(name="From", value=f"{from_currency} ({from_country.title()})", inline=True)
            embed.add_field(name="To", value=f"{to_currency} ({to_country.title()})", inline=True)
            embed.add_field(name="Amount", value=f"{amount:,.2f}", inline=True)
            embed.add_field(name="Exchange Rate", value=f"{exchange_rate:,.4f}", inline=True)
            embed.add_field(name="Converted Amount", value=f"{converted_amount:,.2f}", inline=True)
            embed.set_footer(text=f"Date: {date}")

            await ctx.message.reply(embed=embed)
        except requests.RequestException as e:
            await ctx.message.reply(f"An error occurred while making the request: {e}")
        except KeyError as e:
            await ctx.message.reply(f"Unexpected response from the API: missing key {e}")
        except Exception as e:
            await ctx.message.reply(f"An unexpected error occurred: {e}")


async def setup(bot):
    await bot.add_cog(Currency(bot))
