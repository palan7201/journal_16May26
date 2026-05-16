import sqlite3

connection = sqlite3.connect ("journal.db")

cursor = connection.cursor ()

schema = """CREATE TABLE entries (
              journalid int primary key,
              journal_date text,
              journal_text text,
              created_at text,
              updated_at text)"""

if (cursor.execute (schema)):
  print ("Database connection successful")
