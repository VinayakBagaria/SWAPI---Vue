import requests
import json
from pprint import pprint

i = 1

while True:
    r =  requests.get('https://anapioficeandfire.com/api/characters/' + str(i), verify = 'certificate.pem')
    print(r)
    if r.status_code == 200:
        json = json.loads(r.content.decode('utf-8'))
        i += 1
    else:
        break

print(i)



