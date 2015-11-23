#Finds the first place id from a geolocation

import urllib.request
import urllib.parse
import json

def geojson_firstid(address):
    #address = input('Enter location: ')
    #if len(address) < 1 : return false
    
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode("UTF-8")
    print('Retrieved',len(data),'characters')

    js = json.loads(str(data))

    return(js["results"][0]["place_id"])

#Tests
address = "MSU"
assert(geojson_firstid(address)) == "ChIJ94cTgAb2jw0R93FrXChdBDU"

address = "University of Michigan"
assert(geojson_firstid(address)) == "ChIJvVDvkDiuPIgRyEqOjFheWyM"
