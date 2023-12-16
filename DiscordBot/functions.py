import discord
from discord.ext import commands
import random
import mysql.connector
from mysql.connector import Error

db_config = {
    'host': 'localhost',
    'database': 'character_directory',
    'user': 'root',
    'password': 'Asdfkmkm1!',
}


def createUser(name, discord_id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "INSERT INTO users (name, discord_id) VALUES (%s, %s)"
        cursor.execute(query, (name, str(discord_id)))
        connection.commit()
        cursor.close()
        return True
    except:
        return False


def createCharacter(user_id, name, clas, subclass, race):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "INSERT INTO characters (name, user, class, subclass, race) VALUES (%s, %s, %s, %s, %s)"
        character_data = (name, user_id, clas, subclass, race)
        cursor.execute(query, character_data)
        connection.commit()
        cursor.close()
        return True
    except Exception as E:
        print("Error: " + str(E))
        return False


def findUser(discord_id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "SELECT id FROM users WHERE discord_id = " + str(discord_id)
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result[0]
    except:
        return 0


def findCharacter(id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "SELECT name FROM characters WHERE id = " + str(id)
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result[0]
    except:
        return 0


def updateCharacter(query):
    try:
        # establishes connection and starts curser
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # runs query
        cursor.execute(query)
        connection.commit()
        cursor.close()

        return 1
    except:
        return 0


def getList(query):
    try:
        # establishes connection and starts curser
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # runs and retrieves query
        cursor.execute(query)
        result = cursor.fetchall()

        cursor.close()
        return result
    except:
        return 0


def getCharacterInfo(user_id):
    try:
        # establishes connection and starts curser
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # runs and retrieves query
        cursor.execute("SELECT name, id, class, subclass, race, lvl, balance, quests_completed, XP FROM characters WHERE status = 'alive' AND user = " + str(user_id))
        result = cursor.fetchall()

        cursor.close()
        return result[0]
    except:
        return 0


