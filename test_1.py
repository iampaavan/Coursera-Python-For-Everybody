fname = input('Enter the file name: ')

if len(fname) < 1:
    fname = 'mbox.txt'


fh = open(fname)

organization_list = []

for line in fh:
    if not line.startswith('From: '):
        continue

    pieces = line.split()
    emails = pieces[1]
    email_name, organization = emails.split('@')
    organization_list.append(organization)

print(organization_list)