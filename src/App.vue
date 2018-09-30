<template>
  <div id="app">
    <div id="nav">
	<router-link to="/">Tablica Ogłoszeń</router-link>
	<span> | </span>
	<router-link to="/api">Piaskownica</router-link>
	<span> | </span>
	<router-link to="/login">Login</router-link>
    </div>
    <!--<HelloWorld msg="Welcome to Your Vue.js App"/>-->
    <router-view />
  </div><!-- app -->
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import '@vue/ui/dist/vue-ui.css'

export default {
  name: 'app',
  components: {
    HelloWorld
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
