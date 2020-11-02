import sqlite3

conn = sqlite3.connect('database.db')
print("connected successfully")

conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print("created successfully")
conn.close()

