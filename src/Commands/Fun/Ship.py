import discord
import random
from discord.ext import commands
from discord.ext.commands import clean_content

class Ship(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ship cog loaded-----')

    @commands.command()
    async def ship(self, ctx, name1: clean_content, name2: clean_content):
        ship_number = random.randint(0, 100)
        status = self.get_status(ship_number)
        ship_color = self.get_color(ship_number)
        embed = self.create_embed(name1, name2, ship_number, status, ship_color)
        await ctx.send(embed=embed)

    def get_status(self, ship_number):
        random.seed(ship_number) 

        if ship_number <= 10:
            return "Really low! " + random.choice([
                "Friendzone ;(", 'Just "friends"', '"Friends"', "Little to no love ;(", "There's barely any love ;("
            ])
        elif ship_number <= 20:
            return "Low! " + random.choice([
                "Still in the friendzone", "Still in that friendzone ;(", "There's not a lot of love there... ;("
            ])
        elif ship_number <= 30:
            return "Poor! " + random.choice([
                "But there's a small sense of romance from one person!", "But there's a small bit of love somewhere",
                "I sense a small bit of love!", "But someone has a bit of love for someone..."
            ])
        elif ship_number <= 40:
            return "Fair! " + random.choice([
                "There's a bit of love there!", "There is a bit of love there...", "A small bit of love is in the air..."
            ])
        elif ship_number <= 60:
            return "Moderate! " + random.choice([
                "But it's very one-sided OwO", "It appears one sided!", "There's some potential!",
                "I sense a bit of potential!", "There's a bit of romance going on here!",
                "I feel like there's some romance progressing!", "The love is getting there..."
            ])
        elif ship_number <= 70:
            return "Good! " + random.choice([
                "I feel the romance progressing!", "There's some love in the air!", "I'm starting to feel some love!"
            ])
        elif ship_number <= 80:
            return "Great! " + random.choice([
                "There is definitely love somewhere!", "I can see the love is there! Somewhere...",
                "I definitely can see that love is in the air"
            ])
        elif ship_number <= 90:
            return "Over average! " + random.choice([
                "Love is in the air!", "I can definitely feel the love", "I feel the love! There's a sign of a match!",
                "There's a sign of a match!", "I sense a match!", "A few things can be improved to make this a match made in heaven!"
            ])
        else:
            return "True love! " + random.choice([
                "It's a match!", "There's a match made in heaven!", "It's definitely a match!", "Love is truly in the air!",
                "Love is most definitely in the air!"
            ])

    def get_color(self, ship_number):
        if ship_number <= 33:
            return 0xE80303
        elif ship_number < 66:
            return 0xff6600
        else:
            return 0x3be801

    def create_embed(self, name1, name2, ship_number, status, ship_color):
        embed = discord.Embed(
            color=ship_color,
            title="Love test for:",
            description=f"**{name1}** and **{name2}** {random.choice([
                ':sparkling_heart:', ':heart_decoration:', ':heart_exclamation:', ':heartbeat:', ':heartpulse:',
                ':hearts:', ':blue_heart:', ':green_heart:', ':purple_heart:', ':revolving_hearts:',
                ':yellow_heart:', ':two_hearts:'])}"
        )
        embed.add_field(name="Results:", value=f"{ship_number}%", inline=True)
        embed.add_field(name="Status:", value=status, inline=False)
        embed.set_author(name="Shipping", icon_url="http://moziru.com/images/kopel-clipart-heart-6.png")
        return embed

async def setup(client):
    await client.add_cog(Ship(client))