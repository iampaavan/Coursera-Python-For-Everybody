import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cursor = conn.cursor()

# Do some setup
cursor.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Member;
    DROP TABLE IF EXISTS Course
''')

cursor.executescript('''
    
    CREATE TABLE User (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name   TEXT UNIQUE
);

    CREATE TABLE Course (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title  TEXT UNIQUE
);

    CREATE TABLE Member (
        user_id     INTEGER,
        course_id   INTEGER,
        role        INTEGER,
        PRIMARY KEY (user_id, course_id)
)

''')

fname = input('Enter the filename: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]

    print((name, title))

    cursor.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name, ))
    cursor.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cursor.fetchone()[0]

    cursor.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title, ))
    cursor.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cursor.fetchone()[0]

    cursor.execute('INSERT OR REPLACE INTO Member (user_id, course_id) VALUES (?, ?)', (user_id, course_id))

conn.commit()
conn.close()
