<template>
  <div id="app">
    <app-people></app-people>
  </div>
</template>

<script>
import People from './components/People.vue'

export default {
  components:{
    'app-people': People
  },
  name: 'app',
  data () {
    return {
      
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
