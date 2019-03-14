<template>
  <v-app>
    <v-toolbar>
      <v-toolbar-title style="width: 300px" class="ml-0 pl-3">
        <!--add icon here-->
        <span class="hidden-sm-and-down">PH_TRADE</span>
      </v-toolbar-title>
      <v-text-field
        flat
        solo-inverted
        prepend-icon="search"
        label="Search"
        class="hidden-sm-and-down"
      ></v-text-field>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn flat to="/">PH_TRADE </v-btn>
        <v-btn flat to="/board">Tablica Ogłoszeń</v-btn>
        <v-btn to="/api" flat>Piaskownica </v-btn>
        <v-btn flat to="/login">Login</v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <v-content>
      <v-container fluid fill-height>
        <router-view />
      </v-container>
    </v-content>
    <v-footer class="pa-3">
      <v-spacer></v-spacer>
      <div>PH_TRADE &copy; {{ new Date().getFullYear() }}</div>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "app",
  components: {}
};
</script>
