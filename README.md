![Image](/swapi.png)
<h1 align="center">SWAPI</h1>

<p align="center">Ultimate Star Wars Search using ElasticSearch and Vue JS</p>

### Requirements

<ul>
  <li>Elastic Search</li>
  <li>Python 3</li>
  <li>Vue JS</li>
</ul>

### ES Config
Allow http access through Vue code by adding the following configs to /config/elasticsearch.yml file in ES directory.

     http.cors.enabled : true
     http.cors.allow-origin: "*"
     http.cors.allow-methods: OPTIONS, HEAD, GET, POST, PUT, DELETE
     http.cors.allow-headers: X-Requested-With,X-Auth-Token,Content-Type,Content-Length
     http.cors.allow-credentials: true

Now run elasticsearch. It should be up on port 9200.

### Python Config
Installing requirements for python

     pip install -r requirements.txt

Change directory into `src/` and run

      python automate.py

After a few seconds, you should see `done indexing`. Go to [People Search](http://localhost:9200/swapi/people/_search) . All the json files inside [src directory](https://github.com/VinayakBagaria/SWAPI/tree/master/src) get indexed into ES.

### Vue Config

Now go to `swapi-vue/` and run

      npm install

Now run

      npm run dev
Voila...!! Type in a name in the search box and your result is the filtered names.

### Future Improvements

UI for sure<br>
More detailed content and referencing<br>
Navigation

### Credits

Hosted [API](https://www.swapi.co)<br>
Django REST [Source Code](https://github.com/phalt/swapi) for the API
