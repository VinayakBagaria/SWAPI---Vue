import requests
import json


i = 1

r = requests.get('http://swapi.co/api/planets/' + str(i), verify='certificate.pem')
print(i)
if r.status_code == 200:
    json = json.loads(r.content.decode('utf-8'))
    print(json)
else:
    print('Nothing')
