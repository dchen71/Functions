#Parses json and finds the total sum in the count 

import json
import urllib.request

def add_json(url):
  total = 0
  uh = urllib.request.urlopen(url)
  data = str(uh.read().decode("UTF-8"))

  js = json.loads(data)
  for entries in js["comments"]:
    total += entries["count"]

  return total

#Testing cases
url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.json"
assert(add_json(url)) == 2553

url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_169151.json"
assert(add_json(url)) == 2832