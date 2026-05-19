#journal_15May26/database.py

import sqlite3
import subprocess
from datetime import datetime
import sys
import os
import tempfile
import getopt
import tkinter as tk

#Gui - tkinter
screen = tk.Tk()
screen.title("Journal")
screen.geometry('600x400+150+100')
screen.resizable(True, True)

#icon = tk.PhotoImage(file = './journal_icon.png')
#screen.iconphoto(False, icon)

frame = tk.Frame()
frame.pack()

label = tk.Label(master = "frame", text = 'Wow, hello world GUI', bg = 'black', fg = 'white')
label.pack()

label = tk.Label(text = 'Wow, hello world GUI', bg = 'black', fg = 'white')
label.pack()

screen.mainloop()

#Database connection - schema creation (if not exists)
connection = sqlite3.connect("journal.db")
print("Database connection successful", file = sys.stderr)

cursor = connection.cursor()

schema = """CREATE TABLE IF NOT EXISTS entries (
              journal_date text primary key,
              journal_text text,
              created_at text,
              updated_at text null);
         """

cursor.execute(schema)
j_file = tempfile.NamedTemporaryFile(mode = 'w', delete = False)

# getting system (local) date & request date
request_date = datetime.now().strftime("%d-%m-%Y")
if (len(sys.argv)>1):
    request_date = sys.argv[1]

print("Requested date : %s" %request_date, file = sys.stderr)

#Processing command-line arguments
db_file = cursor.execute("""select journal_text from entries where journal_date = '%s';""" %request_date)
db_file = cursor.fetchone()
j_header = ''

#find if the journal should be created or updated - database
if(db_file is not None):
    #reading query result - journal_text
    j_file.write(db_file[0])
    modified = True
else:
    # Writing file header
    j_header = datetime.now().strftime("%B %-d, %Y\n") #December 7, 2025
    j_header += datetime.now().strftime("%A\n") #Tuesday
    j_header += datetime.now().strftime("%I:%M:%S %p\n\n") #07:09:12 PM
    j_file.write(j_header)
    modified = False

#Calling the editor for editing journal file
j_file.close()
time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") # journal opening time

subprocess.run([os.getenv("EDITOR", "nano"), "--", j_file.name])

# fetch journal file data for update and insert query
j_file = open(j_file.name, 'r')
journal_text = j_file.read()
print("\nThe content read from the journal file is : \n%s" %journal_text, file = sys.stderr)

#writing to database
if(modified):
    update = """update entries set journal_text= ?, updated_at=? where journal_date = ?"""
    cursor.execute(update, (journal_text, time, request_date))
    print("Updated the journal", file = sys.stderr)
else:
    insert = """insert into entries(journal_date, journal_text, created_at, updated_at) values (?, ?, ?, null)"""
    cursor.execute(insert, (request_date, journal_text, time))
    print("Inserted into the journal", file = sys.stderr)

#closing the connections
connection.commit()
j_file.close()
cursor.close()
