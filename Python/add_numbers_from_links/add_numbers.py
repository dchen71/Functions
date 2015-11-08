# This will add up all the numbers on a specific page

import urllib.request
from bs4 import BeautifulSoup

url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.html"
with urllib.request.urlopen(url) as repsonse:
	html = repsonse.read()

soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup.find_all('a')
for tag in tags:
   # Look at the parts of a tag
   print('TAG:',tag)
   print('URL:',tag.get('href', None))
   print('Contents:',tag.contents[0])
   print('Attrs:',tag.attrs)