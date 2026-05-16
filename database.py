import sqlite3

connection = sqlite3.connect ("journal.db")

cursor = connection.cursor ()

cursor.execute ("CREATE TABLE if not exists")
