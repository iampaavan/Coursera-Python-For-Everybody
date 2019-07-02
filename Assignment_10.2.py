fname = input("Enter file name: ")
if len(fname) < 1:
	fname = "mbox-short.txt"

fh = open(fname)
my_list = list()
dictionary = dict()

for line in fh:
	if not line.startswith("From "):
		continue
	lines = line.strip()
	split = lines.split()
	hour = split[5].split(":")
	my_list.append(hour[0])

for list_1 in my_list:
	dictionary[list_1] = dictionary.get(list_1, 0) + 1

for key, value in sorted(dictionary.items()):
	print(key, value)
