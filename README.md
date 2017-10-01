![Image](/swapi.png)
<h1 align="center">SWAPI</h1>

Ultimate Star Wars Search using ElasticSearch and Vue JS

### Requirements

<ul>
  <li>Elastic Search</li>
  <li>Python 3</li>
  <li>Vue JS</li>
</ul>

### Setup
<ol>
<li> Allow http access through Vue code by adding the following configs to `<path_to_elasticsearch>/config/elasticsearch.yml` file

     http.cors.enabled : true
     http.cors.allow-origin: "*"
     http.cors.allow-methods: OPTIONS, HEAD, GET, POST, PUT, DELETE
     http.cors.allow-headers: X-Requested-With,X-Auth-Token,Content-Type,Content-Length
     http.cors.allow-credentials: true

Now run elasticsearch. It should be up on port 9200. </li>
<li> Installing requirements for python

     pip install -r requirements.txt
</li>
<li>  Change directory into source and run

      python automate.py

A open file dialog selector should open. Select your json file. "done indexing" should be the output in the console.
Do this step for all the json files, one by one.

      Beware: Don't re-select a file already indexed (double data).
</li>
<li> Now go to swapi-vue directory and run

      npm install
</li>
<li>  Now run

      npm run dev
Voila...!! Type in a name in the search box and your result is the filtered names. </li>
</ol>

### Credits

[SWAPI](https://github.com/phalt/swapi) Django REST files hosted on https://www.swapi.co
