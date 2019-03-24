<template>
  <v-layout>
    <v-flex xs12>
      <v-layout align-space-around fill-height>
        <v-flex md2>
          <v-card height="100%">
            <v-list>
              <v-list-group
                v-for="bmenu in backendMenus"
                :key="bmenu.name"
                v-model="bmenu.active"
              >
                <v-list-tile slot="activator">
                  <v-list-tile-content>
                    <v-list-tile-title>{{ bmenu.name }}</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>

                <v-list-tile
                  v-for="item in bmenu.items"
                  :key="item.name"
                  @click=""
                >
                  <v-list-tile-content>
                    <v-list-tile-title>{{ item.name }}</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
              </v-list-group>
            </v-list>
            <v-btn round outline @click="logout">Logout</v-btn>
          </v-card>
        </v-flex>
        <v-flex md10>
          <v-card height="100%">
            <h1>Backend</h1>
          </v-card>
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>

<script>
import $backend from "../backend";

export default {
  name: "userAccount",
  data: function() {
    return {
      backendMenus: [
        {
          name: "Models",
          items: [{ name: "Ads" }, { name: "Categories" }, { name: "Users" }]
        }
      ]
    };
  },
  methods: {
    logout: function() {
      $backend.logoutUser().then(this.$router.push("/"));
    }
  }
};
</script>
