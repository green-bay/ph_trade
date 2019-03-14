<template>
  <v-app>
    <v-toolbar>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn flat to="/">PH_TRADE </v-btn>
        <v-btn flat to="/board">Tablica Ogłoszeń</v-btn>
        <v-btn to="/api" flat>Piaskownica </v-btn>
        <v-btn flat to="/login">Login</v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <!--<HelloWorld msg="Welcome to Your Vue.js App"/>-->
    <v-content>
      <router-view />
    </v-content>
    <v-footer class="pa-3">
      <v-spacer></v-spacer>
      <div>PH_TRADE &copy; {{ new Date().getFullYear() }}</div>
    </v-footer>
  </v-app>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";

export default {
  name: "app",
  components: {
    HelloWorld
  }
};
</script>
