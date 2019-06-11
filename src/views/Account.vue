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
                  :to="{
                    name: 'modelRoute',
                    params: {
                      model: item.name.toLowerCase(),
                      form: item.form
                    }
                  }"
                >
                  <v-list-tile-content>
                    <v-list-tile-title>
                      {{ item.name }}
                    </v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
              </v-list-group>
            </v-list>
            <v-btn round outline @click="logout">Logout</v-btn>
          </v-card>
        </v-flex>
        <transition name="fade" mode="out-in">
          <v-flex md10 v-if="!showForm">
            <v-card height="100%">
              <h1>{{ $route.params.model }}</h1>
              <router-view @show-form="showMeForm"></router-view>
            </v-card>
          </v-flex>
          <v-flex md10 v-else>
            <v-card height="100%">
              <h1>{{ this.formName }}</h1>
              <AdCategoryForm
                v-if="formName == 'AdCategoryForm'"
                @cat-posted="postCat"
                @cat-post-cancel="postCat"
              />
            </v-card>
          </v-flex>
        </transition>
      </v-layout>
    </v-flex>
  </v-layout>
</template>

<script>
import AdCategoryForm from "../components/AdCategoryForm";
import $backend from "../backend";

export default {
  name: "userAccount",
  components: {
    AdCategoryForm
  },
  data: function() {
    return {
      backendMenus: [
        {
          name: "Models",
          items: [
            { name: "Ads" },
            { name: "Categories", form: "AdCategoryForm" },
            { name: "Users" }
          ]
        }
      ],
      showForm: false,
      formName: ""
    };
  },
  methods: {
    logout: function() {
      $backend.logoutUser().then(this.$router.push("/"));
    },
    showMeForm: function(formName) {
      this.showForm = true;
      this.formName = formName;
    },
    postCat: function() {
      this.showForm = false;
      this.formName = "Categories";
    }
  }
};
</script>
