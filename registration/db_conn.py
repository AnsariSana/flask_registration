import sqlite3

conn = sqlite3.connect('database.db')
print("Connected successfully.")
conn.execute('CREATE TABLE User (username TEXT PRIMARY KEY, password TEXT)')
print("Created table successfully.")
conn.close()