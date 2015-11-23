# This will add up all the numbers on a specific page

import urllib.request
from bs4 import BeautifulSoup

#Takes a url and returns the total of numbers between the spans
def add_numbers(url):
	total = 0
	
	#Reads the data from the url
	with urllib.request.urlopen(url) as repsonse:
		html = repsonse.read()

	#Beautitful soup parser
	soup = BeautifulSoup(html, "html.parser")

	# Retrieve all of the anchor tags
	spans = soup.find_all('span')
	for span in spans:
	   total += int(span.contents[0])
	
	return total


#Tests
url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.html"
assert(add_numbers(url)) == 2553

url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_169150.html"
assert(add_numbers(url)) == 2391