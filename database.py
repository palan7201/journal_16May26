#journal_16May26/database.py

import sqlite3
import subprocess
from datetime import datetime

connection = sqlite3.connect ("journal.db")
print ("Database connection successful")

cursor = connection.cursor ()

schema = """CREATE TABLE IF NOT EXISTS entries (
              journal_id int primary key,
              journal_date text,
              journal_text text,
              created_at text,
              updated_at text)"""

cursor.execute (schema)

subprocess.call (['touch', 'temp.txt'])

header = datetime.now().strftime("%B %-d, %Y") #December 7, 2025
header += "\n" + datetime.now().strftime("%A") #Tuesday
header += "\n" + datetime.now().strftime("%I:%M:%S %p") + "\n\n" #07:09:12 PM

file = open('temp.txt','w')

file.write (header)

 #TODO : find ways to seperate the closes and capture catches more than one errors
file.close()
cursor.close()

subprocess.call (['nano', file.name])
