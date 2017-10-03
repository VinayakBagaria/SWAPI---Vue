<template>
  <div id="app">
    <select v-model="text" @change="selected">
      <option v-for="option in options" v-bind:value="option.option">
        {{option.option}}
      </option>
    </select>
    <app-result v-bind:keyData="keyData" v-bind:value="text"></app-result> -->
  </div>
</template>

<script>
import Result from './components/Result.vue'

export default {
  components:{
    'app-result': Result
  },
  name: 'app',
  data () {
    return {
      keyData: 'name',
      text:'People',
      options: [
        {
          "value": "title",
          "option": "Films"
        },
        {
          "value": "name",
          "option": "People"
        },
        {
          "value": "name",
          "option": "Planets"
        },
        {
          "value": "name",
          "option": "Species"
        },
        {
          "value": "starship_class",
          "option": "Starships"
        },
        {
          "value": "name",
          "option": "Transport"
        },
        {
          "value": "vehicle_class",
          "option": "Vehicles"
        }
      ]
    }
  },
    methods: {
      selected: function () {
        var i = 0;
         for(i=0;i<this.options.length;i++)
         {
           var x = this.options[i];
           if (x['option'] == this.text)
           {
             this.keyData=this.options[i]['value'];
             break;
           }
         }
       }
    }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
