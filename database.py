#journal_16May26/database.py

import sqlite3
import subprocess
from datetime import datetime

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


subprocess.call (['touch', 'temp.txt'])

header = datetime.now().strftime("%B %-d, %Y") #December 7, 2025
header += "\n" + datetime.now().strftime("%A") #Tuesday
header += "\n" + datetime.now().strftime("%I:%M:%S %p") + "\n\n" #07:09:12 PM

try:
    file = open('temp.txt','w')

except:
    pass

finally:
    pass

file.write (header)

try: #TODO : find ways to seperate the closes and capture catches more than one errors
    file.close()
    cursor.close()
except:
  pass

finally:
  pass



subprocess.call (['nano', file.name])
