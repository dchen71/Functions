# This will retreieve the last name for a series of links in tags
import urllib.request
from bs4 import BeautifulSoup

#Takes a url and returns the link from the position of x counts
def follow_links(url, count, position):	
	final = ""

	for i in range(count):
		#Reads the initial data from the url
		with urllib.request.urlopen(url) as repsonse:
			html = repsonse.read()

		#Beautitful soup parser
		soup = BeautifulSoup(html, "html.parser")

		# Retrieve all of the anchor tags
		tags = soup('a')

		url = tags[position - 1].get('href', None)

	final = tags[position - 1].get('href', None)
	return final

	
#Tests
url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html"
assert(follow_links(url,4,3)) == "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Anayah.html"

url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Naila.html"
assert(follow_links(url, 7, 18)) == "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Meko.html"