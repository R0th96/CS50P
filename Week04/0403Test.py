#How to install python packages and what are the two packages you installed during CS50? Try with examples. 
#pip install (Package name) 
#Cowsay
import cowsay
import sys

if len(sys.argv) < 2:
    print("Tow few arg")
else:
    cowsay.cow(sys.argv[1:])

#request
import requests
import json

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#print(json.dumps(response.json(), indent=2))

response = response.json()
for o in response["results"]:
    print(o["trackName"])

