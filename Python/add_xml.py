#Reads through an xml document and sums up all the numbers in this particular document

import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

def add_xml(url):
    total = 0
    uh = urllib.request.urlopen(url)
    data = uh.read()
    tree = ET.fromstring(data)

    #Parse out structure and add the number variables in count
    comments = tree.findall('./comments/comment')
    for comment in comments:
        total += int(comment.find('count').text)

    return total

#Test cases
url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.xml"
assert(add_xml(url)) == 2553

url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_169147.xml"
assert(add_xml(url)) == 2655