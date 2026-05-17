#journal_16May26/database.py

import sqlite3
import subprocess
from datetime import datetime
import sys
import os
import tempfile
import getopt

#Database connection - schema creation (if not exists)
connection = sqlite3.connect("journal.db")
print("Database connection successful", file = sys.stderr)

cursor = connection.cursor()

schema = """CREATE TABLE IF NOT EXISTS entries (
              journal_date text primary key,
              journal_text text,
              created_at text,
              updated_at text);
         """

cursor.execute(schema)
j_file = tempfile.NamedTemporaryFile(mode = 'w', delete = False)

# getting system (local) date & request date
current_date = datetime.now().strftime("%d-%m-%Y")
if (len(sys.argv)<1):
    request_date = sys.argv[1]
else:
    request_date = current_date

#Processing command-line arguments
#find if the journal should be created or updated - database
db_file = cursor.execute("""select journal_text from entries where journal_date = '%s';""" %request_date)
db_file = cursor.fetchone()

if(db_file is not None):
    j_file.write(db_file[0])

else:
    # Writing file header & TODO: new row - database
    j_header = datetime.now().strftime("%B %-d, %Y\n") #December 7, 2025
    j_header += datetime.now().strftime("%A\n") #Tuesday
    j_header += datetime.now().strftime("%I:%M:%S %p\n\n") #07:09:12 PM
    j_file.write(j_header)


#Calling the editor for editor
j_file.close()
subprocess.call([os.getenv("EDITOR", "nano"), "--", j_file.name])

# TODO: fetch journal file data & complete the query after thinking through
#cursor.execute("""insert into entries values ('%s', , ,'%s')""" %request_date %)

j_file.close()
cursor.close()

