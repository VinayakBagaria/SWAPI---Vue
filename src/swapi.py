import json
import requests
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
r = requests.get('http://localhost:9200')
i = 1
while r.status_code == 200:
    r = requests.get('http://swapi.co/api/people/'+ str(i))
    x=es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content.decode('utf-8')))
    print(x)
    i=i+1
print(i)

print(es.get(index='sw', doc_type='people', id=65))
