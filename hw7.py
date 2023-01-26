# сделать бд студента
# с полями хобби,имя ,фамилия,год рождения, баллы за дз
# создать 10 студентов
# достать всех студентов у которых фамилия больше 10 символов
# изменить имена всех студентов у которых балл больше 10 на genius
# вывести всех genius
# удалить всех студентов у которых id четное

import sqlite3
db = sqlite3.connect('hw7.db')

students = db.cursor()

students.execute("DELETE FROM user") #(добавила чтоб после каждого запуска список обновлялся а не добавлял)

students.execute('''CREATE TABLE IF NOT EXISTS user (
name TEXT,
lastname TEXT,
year INTEGER,
hobby TEXT,
marks integer
)''')

students.execute("INSERT INTO user VALUES ('Nazira', 'Abdillaeva', 1989, 'reading', 10)")
students.execute("INSERT INTO user VALUES ('Mirlan', 'Aitbaev', 2006, 'football', 10)")
students.execute("INSERT INTO user VALUES ('Bektur', 'Rysbaev', 2004, 'volleybal', 9)")
students.execute("INSERT INTO user VALUES ('Eldiyar', 'Nurali', 2002, 'chess', 9)")
students.execute("INSERT INTO user VALUES ('Arzybek', 'Abdyrahmanov', 2001, 'driving', 10)")
students.execute("INSERT INTO user VALUES ('Alimbek', 'Akerov', 2005, 'swimming', 9)")
students.execute("INSERT INTO user VALUES ('Sergei', 'Beliaev', 1997, 'writing', 9)")
students.execute("INSERT INTO user VALUES ('Adilet', 'Jenishbekov', 2007, 'basketball', 9)")
students.execute("INSERT INTO user VALUES ('Abdulla', 'Manarov', 1999, 'running', 9)")
students.execute("INSERT INTO user VALUES ('Maxim', 'Evtushenko', 1995, 'music', 10)")
students.execute("INSERT INTO user VALUES ('Daniyar', 'Jyrgalbek', 1998, 'surfing', 9)")
students.execute("SELECT rowid FROM user")


students.execute("UPDATE user SET name = 'genius' WHERE marks >= 10")
students.execute("SELECT rowid, lastname, name FROM user ")

item = students.fetchall()
for elements in item:
    print(elements)

for i in item:
    lastname = i[1]
    if len(lastname) > 10:
        print(lastname)
    else:
        ...

students.execute("SELECT rowid, name FROM user WHERE name = 'genius'")
students.execute("DELETE FROM user WHERE rowid % 2 = 0")
print(students.fetchall())

db.commit()
db.close()
