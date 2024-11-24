import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Mist_2024%$',
    )

#prepare cursor object

cursor = database.cursor()

#create database


cursor.execute("CREATE DATABASE hms")

print("All done")

