#Create a SQLite3 database and table

import sqlite3

#create a new database if it does not exist
conn = sqlite3.connect("new.db")
nuconn = sqlite3.connect("cars.db")
#get a cursor object to execute SQL commands
cursor = conn.cursor()
curs2 = nuconn.cursor()

#create a table
cursor.execute("""CREATE TABLE population
                (city TEXT,state TEXT, population INT)
                """)
curs2.execute("""CREATE TABLE inventory
                (make TEXT, Model TEXT, Quantity INT)
                """)
#close connection
conn.close()
nuconn.close()

