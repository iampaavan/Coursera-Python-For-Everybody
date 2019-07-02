from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_187236.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

spans = soup('span')
my_list = []

for span in spans:
	my_list.append(int(span.string))

print(sum(my_list))
