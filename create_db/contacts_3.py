import sqlite3

conn = sqlite3.connect("contacts.sqlite")

username = input("Please enter a name\n")
# for row in conn.execute("SELECT * FROM contacts WHERE name = ?", (username,)):
for row in conn.execute("SELECT * FROM contacts WHERE name like ?", (username,)):
    print(row)

conn.close()