import sqlite3 as sdb

with sdb.connect("testra.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE users (name TEXT PRIMARY KEY,surn TEXT NOT NULL,age INTEGER)""")