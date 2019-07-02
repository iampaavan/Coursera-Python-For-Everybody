# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
add = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
	    continue
    line.strip()
    white_spaces = line.find(" ")
    number = line[white_spaces:]
    strip_white_spaces = number.lstrip()
    result = float(strip_white_spaces)
    add = add + result
    count += 1
    answer = round(float(add / count), 12)
    
# print(f'No of line {count}')
# print(f'Sum of numbers {add}')
print(f'Average spam confidence: {answer}')