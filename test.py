from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = input('Enter the URL: ')
html = urlopen(URL)
position = int(input(f'Enter the position: '))
count = int(input(f'Enter the count: '))
soup = BeautifulSoup(html, "html.parser")
hrefs = soup('a')

for href in hrefs:
	print(href.get('href'))

for i in range(count):
	content = hrefs[position - 1].get('href')
	print(hrefs[position - 1].contents[0])
	url = urlopen(content)
	my_soup = BeautifulSoup(url, "html.parser")
	hrefs = my_soup('a')