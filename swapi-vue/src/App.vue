<template>
  <div id="app">
    <app-result v-bind:title="people"></app-result>
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
      people: 'Planets'
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
