import discord
from discord.ext import commands
import requests
import asyncio


class Hack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hack(self, ctx, member: discord.Member = None):
        """
        Simulates hacking and sends a fake hacking attempt log.
        """
        if member is None:
            member = ctx.author

        # Check if the provided member is a valid user
        if not isinstance(member, discord.Member):
            await ctx.send("Invalid user specified.")
            return

        # Fake hacking attempt log
        hacking_steps = [
            "Attempting to hack user...",
            "Getting user IP...",
            "Attempting to retrieve user account...",
            "Brute forcing user password...",
            "Accessing sensitive data...",
            "Downloading user history...",
            "Sending fake hack alert...",
            "Hacking complete. No suspicious activity found.",
        ]

        # Send the initial message and get its reference
        hacking_message = await ctx.message.reply("Hacking in progress...")

        # Send each step of the fake hacking attempt log by editing the initial message
        for step in hacking_steps:
            await hacking_message.edit(content=f"{step} @{member.display_name}")
            await asyncio.sleep(1)  # Delay for demonstration purposes

        # If the hacking attempt is successful, send fake user data
        if "complete" in hacking_steps[-1].lower():
            await self.send_fake_user_data(ctx, member)

    async def send_fake_user_data(self, ctx, member):
        """
        Simulates sending fake user data.
        """
        url = "https://randomuser.me/api/"
        try:
            response = requests.get(url)
            data = response.json()

            if "results" not in data or len(data["results"]) == 0:
                await ctx.send("Failed to retrieve user data.")
                return

            user_data = data["results"][0]

            embed = discord.Embed(
                title=f"Hacked {member.display_name} Data", color=0xFF0000
            )
            embed.add_field(
                name="Username", value=user_data["login"]["username"], inline=False
            )
            embed.add_field(name="Email", value=user_data["email"], inline=False)
            embed.add_field(name="Phone", value=user_data["phone"], inline=False)
            embed.add_field(
                name="Location",
                value=f"{user_data['location']['city']}, {user_data['location']['state']}, {user_data['location']['country']}",
                inline=False,
            )
            embed.add_field(
                name="Date of Birth", value=user_data["dob"]["date"], inline=False
            )
            embed.add_field(name="Age", value=user_data["dob"]["age"], inline=True)
            embed.add_field(name="Gender", value=user_data["gender"], inline=True)
            embed.set_thumbnail(url=user_data["picture"]["large"])

            await ctx.message.reply(embed=embed)

        except Exception as e:
            await ctx.send(f"An error occurred: {e}")


async def setup(bot):
    await bot.add_cog(Hack(bot))
