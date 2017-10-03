from elasticsearch import Elasticsearch
import json
import os
import requests

es = Elasticsearch([
    {
        'host': 'localhost',
        'port': 9200
    }
])

listOfFiles = [f for f in os.listdir() if os.path.isfile(f) if '.json' in f]

data = dict()

for file in listOfFiles:
    doc_name = file.split('.json')[0]

    with open(file) as json_data:
        d = json.load(json_data)

        for x in range(len(d)):
            data = d[x]['fields']
            data['pk'] = d[x]['pk']

            es.index(index='swapi', doc_type=doc_name, body=data)

print('done indexing')
