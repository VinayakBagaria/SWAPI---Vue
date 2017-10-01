import requests
import json
from pprint import pprint

i = 1

r =  requests.get('https://anapioficeandfire.com/api/characters/' + str(i), verify = 'certificate.pem')
print(i)
if r.status_code == 200:
    json = json.loads(r.content.decode('utf-8'))
    pprint(json)
else:
    print('Nothing')



