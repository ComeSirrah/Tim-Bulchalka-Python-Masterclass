import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6545678, 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@myemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())

# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# for name, number, email in cursor:
#     print(f"{name}| Phone number: {number}, Email: {email}")

cursor.close()
db.commit()
db.close()
