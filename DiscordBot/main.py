import discord
from discord.ext import commands
import random

BOT_TOKEN = "token"

# handles discords "intents"
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# sets up the bot
bot = commands.Bot(command_prefix='!', intents=intents)

# confirms that the bot starts correctly
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

# testing in taking in text and making the bot say text
@bot.command()
async def echo(ctx, *args):
    """makes the bot say what you just said"""
    await ctx.send(" ".join(args))

# testing fetching user id and username
@bot.command()
async def me(ctx):
    """tells you information about yourself"""
    user = ctx.author
    await ctx.send("Your Username is: " + user.global_name + "\nYour ID is: " + str(user.id))


bot.run(BOT_TOKEN)