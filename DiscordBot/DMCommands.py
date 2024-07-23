import discord
from discord.ext import commands
from functions import *


class DMOnly(commands.Cog):
    """Commands which can only be used by a user with the DM role"""

    @commands.command()
    @commands.has_role('DM')
    async def kill(self, ctx, character_id):
        """kills a character based on their id"""

        if updateCharacter("UPDATE characters SET status = 'dead' WHERE id = " + str(character_id)):
            response = "Killed Character"
        else:
            response = "Failed To Kill Character"

        await ctx.send(response)

    @commands.command()
    @commands.has_role('DM')
    async def revive(self, ctx, character_id):
        """revives a character based on their id"""

        if updateCharacter("UPDATE characters SET status = 'alive' WHERE id = " + str(character_id)):
            response = "Revived Character"
        else:
            response = "Failed To Revive Character"

        await ctx.send(response)

    @commands.command()
    @commands.has_role('DM')
    async def delete(self, ctx, character_id):
        """deletes a character based on their id"""

        if updateCharacter("DELETE FROM characters WHERE id = " + character_id):
            response = "Deleted Character"
        else:
            response = "Failed To Delete Character"

        await ctx.send(response)

    @commands.command()
    @commands.has_role('DM')
    async def info(self, ctx, id):
        """tells information about a character"""
        info = getCharacterInfo(id)

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

    @commands.command()
    @commands.has_role('DM')
    async def updatecharacter(self, ctx, character_id=None, stat=None, new_info=None):
        """updates information about a character"""
        if character_id and stat and new_info:
            if updateCharacter("UPDATE characters SET " + str(stat) + " = '" + str(new_info) + "' WHERE id = " + str(
                    character_id)):
                response = "Successfully Updated Character"
            else:
                response = "Failed To Update Character"
        else:
            response = ("Incorrect use of command \n"
                        "Use !updatecharacter [ID] [Stat You'd Like To Update] [New Info]")
        await ctx.send(response)

    @commands.command()
    @commands.has_role('DM')
    async def completequest(self, ctx, questLevel=None, *ids: int):
        """gives players XP based on completed quest"""

        # makes sure all parameters exist
        if questLevel and ids:

            response = "Quest Completed"
            for id in ids:
                info = getCharacterInfo(id)
                charLevel = info[5]
                XP = info[8]
                givenXP = (int(questLevel) - charLevel) / 2 + 1
                newXP = XP + givenXP
                if newXP >= charLevel + 1:
                    charLevel += 1
                    newXP = 0
                    userID = findUserFromCharacter(id)
                    discordID = findDiscordID(userID)
                    response += "\n <@" + str(discordID) + ">, " + info[0] + " has leveled up, and is now level " + str(charLevel)
                questsCompleted = getCharacterInfo(id)[7] + 1
                if not updateCharacter("UPDATE characters SET XP = " + str(newXP) + ", quests_completed = " + str(
                        questsCompleted) + ", lvl = " + str(charLevel) + " WHERE id = " + str(id)):
                    response = "Failed to Complete Quest"
        else:
            response = "Usage: !completequest [Quest Level] [IDs of characters]"

        await ctx.send(response)
