import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS Counts')

cursor.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input('Enter the file name: ')

if len(fname) < 1:
    fname = 'mbox-short.txt'

email_list = []

fh = open(fname)

for line in fh:
    if not line.startswith('From: '):
        continue

    pieces = line.split()
    emails = pieces[1]
    email_list.append(emails)
    cursor.execute('SELECT count FROM Counts WHERE email=?', (emails, ))
    row = cursor.fetchone()

    if row is None:
        cursor.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (emails, ))

    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE email=?', (emails, ))

    conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC'

for row in cursor.execute(sqlstr):
    print(str(row[0]), row[1])

cursor.close()