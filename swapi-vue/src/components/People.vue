<template>
  <div id="show-people">
    <h1>Star Wars People Search</h1>
    <input type="text" v-model="search" placeholder="Search person">
    <div class="person" v-for="single in people">
      <h2 v-rainbow>{{ single._source.name }}</h2>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  import searchMixin from "../mixins/searchMixin.js";
  export default{
    data(){
      return{
        people: [],
        search: ''
      }
    },
    methods:{

    },
    watch:{
      search(val, oldVal){
        axios.post('http://localhost:9200/swapi/people/_search',
        {
        	"query":{
        		"match_phrase_prefix":{
        			"name": val
        		}
        	}
        }).then((response) => {
          return response.data;
        }).then((data) => {
          this.people = data.hits.hits;
        });
      }
    },
    directives:{
      'rainbow':{
        bind(el, binding, vnode){
          el.style.color = '#' + Math.random().toString().slice(2,8);
        }
      }
    },
    mixins:[searchMixin]
  }
</script>

<style scoped>
  #show-people{
    max-width: 800px;
    margin: 0 auto;
    margin-bottom: 40px;
  }
  .person{
    padding: 5px 20px 5px 20px;
    margin: 20px 0;
    box-sizing: border-box;
    background: #eee;
  }
  #show-people a{
    color: #444;
    text-decoration: none;
  }
  .person h4{
    cursor: pointer;
    display: inline;
    float: right;
  }
</style>
