<template>
  <div id="show-result">
    <h1>Star Wars {{ value }} Search</h1>
    <input type="text" v-model="search" placeholder="Search">
    <div class="object" v-for="single in result">
      <h2 v-rainbow>{{ single._source[keyData] }}</h2>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';

  export default{
    props:{
      keyData:{
        type: String
      },
      value:{
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
        let search = this.keyData;
        let url = 'http://localhost:9200/swapi/'+this.value.toLowerCase()+'/_search'
        axios.post(url,
        {
        	"query":{
        		"match_phrase_prefix":{
        			   [search] : val
        		}
        	}
        }).then((response) => {
          console.log(response)
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

<style>
  #show-result{
    max-width: 800px;
    margin: 0px auto;
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
</style>
