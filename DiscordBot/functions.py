import discord
from discord.ext import commands
import random
import mysql.connector
from mysql.connector import Error

db_config = {
    'host': 'localhost',
    'database': 'character_directory',
    'user': 'root',
    'password': '***REMOVED***!',
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

