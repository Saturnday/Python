"""

https://pypi.org/project/requests/

json library documentation:
https://docs.python.org/3/library/json.html

pip install requests
JSON - javascript object notation 
"""

import requests
import sys
import json

if len(sys.argv)!=2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])

i = response.json()
for result in i["results"]:
    print(result["trackName"])


import requests

response = requests.get('https://www.google.com')
print(response.json)
