import json
from elasticsearch import Elasticsearch
import requests
import os

es = Elasticsearch([
    {
        'host': 'localhost',
        'port': 9200
    }
])

from tkinter.filedialog import askopenfilename
filename = askopenfilename()

data = dict()

base = os.path.basename(filename)
doc_type = os.path.splitext(base)[0]

print(doc_type)

with open(filename) as json_data:
    d = json.load(json_data)

    for x in range(len(d)):
        data = d[x]['fields']
        data['pk'] = d[x]['pk']

        es.index(index='swapi', doc_type=doc_type, body=data)

print('done indexing')
