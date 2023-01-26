import sqlite3
db = sqlite3.connect('26_3.db')

c = db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS user (
name text,
title text,
view integer,
nick text
)''')
# c.execute("INSERT INTO user VALUES ('NAZIRA', 'STUDENT', 200, 'DEV-ANGELUS')")
# c.execute("INSERT INTO user VALUES ('ELDIYAR', 'GAZETA', 100, 'EDIK')")
# c.execute("SELECT * FROM user")

# c.execute("SELECT * FROM user ORDER BY title DESC")
# c.execute("SELECT * FROM user ORDER BY name DESC")
# c.execute("SELECT rowid, * FROM user ORDER BY view DESC")
c.execute("DELETE FROM user WHERE rowid <15")
c.execute("UPDATE user SET nick = 'maxim' WHERE rowid = 1")
# c.execute("SELECT FROM user WHERE nick <> '0' ")
# c.execute("SELECT rowid, * FROM user ORDER BY rowid DESC")


# c.execute("SELECT nick FROM user")
# print(c.fetchall()) #all in tuple
# print(c.fetchmany(2)) #concrete data
# print(c.fetchone())

item = c.fetchall()
for elements in item:
    print(elements)

db.commit()
db.close()
