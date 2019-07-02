from urllib.request import urlopen
from lxml import etree

URL = 'http://py4e-data.dr-chuck.net/comments_187238.xml'
html = urlopen(URL).read()

tree = etree.fromstring(html)

lst = tree.findall('comments/comment')

print(f"Comment Count: {len( lst )}")

t = []

for l in lst:
	t.append(int(l.find('count').text))

print(sum(t))
