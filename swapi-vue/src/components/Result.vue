<template>
  <div id="show-result">
    <h1>Star Wars {{ title }} Search</h1>
    <input type="text" v-model="search" placeholder="Search">
    <div class="object" v-for="single in result">
      <h2 v-rainbow>{{ single._source.name }}</h2>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';

  export default{
    props:{
      title:{
        type: String
      }
    },
    data(){
      return{
        result: [],
        search: '',
      }
    },
    methods:{

    },
    watch:{
      search(val, oldVal){
        axios.post('http://localhost:9200/swapi/'+this.title.toLowerCase()+'/_search',
        {
        	"query":{
        		"match_phrase_prefix":{
        			"name": val
        		}
        	}
        }).then((response) => {
          return response.data;
        }).then((data) => {
          this.result = data.hits.hits;
        });
      }
    },
    directives:{
      'rainbow':{
        bind(el, binding, vnode){
          el.style.color = '#' + Math.random().toString().slice(2,8);
        }
      }
    }
  }
</script>

<style scoped>
  #show-result{
    max-width: 800px;
    margin: 0 auto;
    margin-bottom: 40px;
  }
  .object{
    padding: 5px 20px 5px 20px;
    margin: 20px 0;
    box-sizing: border-box;
    background: #eee;
  }
  #show-result a{
    color: #444;
    text-decoration: none;
  }
  .object h4{
    cursor: pointer;
    display: inline;
    float: right;
  }
</style>
