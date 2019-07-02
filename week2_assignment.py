import sqlite3, os

os.chdir('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder')

conn = sqlite3.connect('assignment_emaildb.sqlite')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS Counts')

cursor.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter the file name: ')

if len(fname) < 1:
    fname = 'mbox.txt'

email_list = []

fh = open(fname)

for line in fh:
    if not line.startswith('From: '):
        continue

    pieces = line.split()
    emails = pieces[1]
    email_name, organization = emails.split('@')
    email_list.append(emails)
    cursor.execute('SELECT count FROM Counts WHERE org=?', (organization, ))
    row = cursor.fetchone()

    if row is None:
        cursor.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (organization, ))

    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE org=?', (organization, ))

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cursor.execute(sqlstr):
    print(str(row[0]), row[1])

cursor.close()