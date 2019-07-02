import re

x = 'My 2 favorite number are 19 and 42'
pattern = re.compile(r'[0-9]+')
matches = pattern.findall(x)

print(matches)

y = 'From stephen.marquard@uct.ac.za Sat Jun 5 09:14:16 2008drgdcy'
p = re.compile(r'[a-z0-9]')
m = p.findall(y)
print(m)
t = re.findall('@(\S+)', y)
print(t)