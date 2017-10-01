from elasticsearch import Elasticsearch
import requests
import json

es=Elasticsearch([
    {
        'host':'localhost',
        'port':9200
    }
])

r=requests.get('http://localhost:9200')

if r.status_code == 200:
    i = 1
else:
    i = 90

j = 1
for i in range(89):
    r =  requests.get('http://swapi.co/api/people/'+str(i))
    if r.status_code == 200:
        es.index(index='sw',doc_type='people',id=j,body=json.loads(r.content.decode('utf-8')))
        j = j + 1
    i = i + 1

print(i)
