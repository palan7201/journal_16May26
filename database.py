#journal_16May26/database.py

import sqlite3
import subprocess

connection = sqlite3.connect ("journal.db")
print ("Database connection successful")

cursor = connection.cursor ()

schema = """CREATE TABLE entries IF NOT EXISTS (
              journalid int primary key,
              journal_date text,
              journal_text text,
              created_at text,
              updated_at text)"""

try :
  cursor.execute (schema)

except :
  pass

finally:
  print ("Table created successfully")


subprocess.call(['nano', 'temp.txt'])
