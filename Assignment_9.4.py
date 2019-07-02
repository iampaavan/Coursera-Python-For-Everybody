fname = input("Enter file name: ")
if len(fname) < 1:
	fname = "mbox-short.txt"

fh = open(fname)
count = 0
list = list()
dictionary = dict()

for line in fh:
	if not line.startswith("From:"):
		continue
	lines = line.strip()
	split = lines.split(" ")
	# print(split[1])
	list.append(split[1])
	count += 1

# print(list)
for list_1 in list:
	dictionary[list_1] = dictionary.get(list_1, 0) + 1
	
# print(dictionary)
key_max = None
value_max = 0

for key, value in dictionary.items():
	if value > value_max:
		value_max = value
		key_max = key
	
print(key_max, value_max)