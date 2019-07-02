import re

with open('sample.txt', 'r') as file_reader:
	
	contents = file_reader.read()
	
	my_list = []
	
	numbers = (re.findall('[0-9]+', contents))
	
	print(numbers)
	
	for number in numbers:
		my_list.append(int(number))
		
	print(my_list)

print(sum(my_list))
