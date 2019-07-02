from bs4 import BeautifulSoup
import requests

url = 'http://py4e-data.dr-chuck.net/comments_42.html'
content = requests.get(url).text
soup = BeautifulSoup(content, "html.parser")

spans = soup('span')
my_list = []

for span in spans:
    my_list.append(int(span.string))
    
print(sum(my_list))
