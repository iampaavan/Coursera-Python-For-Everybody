from urllib.request import urlopen
import json

URL = 'http://py4e-data.dr-chuck.net/comments_42.json'
html = urlopen(URL).read().decode()
# http://py4e-data.dr-chuck.net/comments_187239.json
data = json.loads(html)
data = data['comments']

my_list = []

for item in data:
	my_list.append(int(item['count']))
	
print(sum(my_list))


	

