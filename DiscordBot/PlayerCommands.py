import discord
from discord.ext import commands
from functions import *


class Commands(commands.Cog):
    """All player commands which can be used"""

    # testing fetching user id and username
    @commands.command()
    async def me(self, ctx):
        """tells you information about yourself"""
        user = ctx.author
        await ctx.send("Your Username is: " + user.global_name + "\nYour ID is: " + str(user.id))

    @commands.command()
    async def mycharacter(self, ctx):
        """tells you information about your character"""
        user_id = findUser(ctx.author.id)
        char_id = findCurrentCharacter(user_id)
        info = getCharacterInfo(char_id)

        # builds response
        response = "ID: " + str(info[1]) + "\nName: " + info[0] + "\nClass: " + info[3] + " " + info[2] + "\nRace: " + \
                   info[4] + "\nLevel: " + str(info[5]) + "\nXP: "
        # reformats XP
        if info[8].is_integer():
            response = response + str(int(info[8]))
        else:
            response = response + str(info[8])
        response = response + "/" + str(info[5] + 1) + "\nQuests Completed: " + str(info[7]) + "\nBalance: " + str(
            info[6]) + " GP"
        await ctx.send(response)

    @commands.group()
    async def list(self, ctx):
        """lists all currently living characters"""

        # only runs the base command if no sub command is run
        if ctx.invoked_subcommand is None:

            characters = getList("SELECT name FROM characters WHERE status = 'alive'")

            if characters:
                response = "All current characters:\n"
                for i in characters:
                    response = response + i[0] + "\n"
            else:
                response = "No current characters"

            await ctx.send(response)

    @list.group()
    async def all(self, ctx):
        """lists all characters, living and dead"""

        # only runs the base command if no sub command is run
        if ctx.invoked_subcommand is None:
            characters = getList("SELECT name FROM characters")

            if characters:
                response = "All characters:\n"
                for i in characters:
                    response = response + i[0] + "\n"
            else:
                response = "No current characters"

            await ctx.send(response)

    @list.command()
    async def id(self, ctx):
        """lists the name and id of all living characters"""

        characters = getList("SELECT name, id FROM characters WHERE status = 'alive'")

        if characters:
            response = "All current characters (Name, ID):\n"
            for i in characters:
                response = response + i[0] + ", " + str(i[1]) + "\n"
        else:
            response = "No current characters"

        await ctx.send(response)

    @all.command(name='id')
    async def allid(self, ctx):
        """lists the name and id of all characters"""

        characters = getList("SELECT name, id FROM characters")

        if characters:
            response = "All characters (Name, ID):\n"
            for i in characters:
                response = response + i[0] + ", " + str(i[1]) + "\n"
        else:
            response = "No current characters"

        await ctx.send(response)

    @list.command()
    async def level(self, ctx):
        """lists the name and level of all living characters"""

        characters = getList("SELECT name, lvl FROM characters WHERE status = 'alive' ORDER BY lvl DESC")

        if characters:
            response = "All current characters (Name, Level):\n"
            for i in characters:
                response = response + i[0] + ", " + str(i[1]) + "\n"
        else:
            response = "No current characters"

        await ctx.send(response)

    @list.command()
    async def users(self, ctx):
        """lists all users on the server"""

        characters = getList("SELECT name, id FROM users")

        if characters:
            response = "All users (Name, ID):\n"
            for i in characters:
                response = response + i[0] + ", " + str(i[1]) + "\n"
        else:
            response = "No current users"

        await ctx.send(response)

    @commands.command()
    async def graveyard(self, ctx):
        """lists all characters in the graveyard"""
        characters = getList("SELECT name FROM characters WHERE status = 'dead'")

        if characters:
            response = "Graveyard:\n"
            for i in characters:
                response = response + i[0] + "\n"
        else:
            response = "No characters in the graveyard"

        await ctx.send(response)

    @commands.command()
    async def createcharacter(self, ctx, name=None, clas=None, subclass=None, race=None):
        """creates a character"""
        # makes sure all parameters exist
        if name and clas and subclass and race:

            # find the user id of caller
            userid = findUser(ctx.author.id)
            if userid == 0:
                # user id not found, make one
                createUser(ctx.author.global_name, ctx.author.id)
                userid = findUser(ctx.author.id)

            # check if they already have a character, and they don't have the role for it
            if (findCurrentCharacter(userid) != 0) and not (ctx.author.get_role(1263240555840667682)):  # TODO: replace the id with something more dynamic (like have a get role by name run when the bot starts)
                response = "You already have a living character. Use !mycharacter to see them."
            else:
                # make character
                if createCharacter(userid, name, clas, subclass, race):
                    response = "Created Character"
                else:
                    response = "Failed To Create Character"
        else:
            response = ("Incorrect use of command \n"
                        "Use !createcharacter [Name] [Class] [Subclass] [Race] \n"
                        "Use quotations for multiple words, ex: \"Mountain Dwarf\" ")

        await ctx.send(response)

    @commands.command()
    async def createuser(self, ctx):
        """makes a user"""

        if createUser(ctx.author.global_name, ctx.author.id):
            response = "Created User"
        else:
            response = "Failed To Create User"

        await ctx.send(response)
