fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words_list = line.rstrip().split()
    for element in words_list:
        if element in lst:
            continue
        else:
            lst.append(element)
lst.sort()
print(lst)
