import discord
from discord.ext import commands
import random
import mysql.connector
from mysql.connector import Error
from functions import *

import PlayerCommands
import MiscCommands
import DMCommands


# gets bot token
File_object = open("BOT_TOKEN.txt", "r")
BOT_TOKEN = File_object.readline()

# gets sql password
File_object = open("SQL_PASSWORD.txt", "r")
SQL_PASSWORD = File_object.readline()

# sets up MySQL database connection parameters
db_config = {
    'host': 'localhost',
    'database': 'character_directory',
    'user': 'root',
    'password': SQL_PASSWORD,
}

# handles discords "intents"
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# sets up the bot
bot = commands.Bot(command_prefix='!', intents=intents)


# confirms that the bot starts correctly
@bot.event
async def on_ready():
    await bot.add_cog(PlayerCommands.Commands())
    await bot.add_cog(MiscCommands.Miscellaneous())
    await bot.add_cog(DMCommands.DMOnly())
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


bot.run(BOT_TOKEN)
