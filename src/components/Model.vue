<template>
  <v-card>
    <div class="loading" v-if="loading">
      ...loading
    </div>
    <div class="error" v-if="error">
      {{ error }}
    </div>
    <div class="content" v-if="content">
      <p>The card of: {{ $route.params.model }}</p>
      <p>{{ content }}</p>
    </div>
  </v-card>
</template>

<script>
import $backend from "../backend";

export default {
  data() {
    return {
      loading: false,
      content: null,
      error: null
    };
  },
  created() {
    this.fetchData();
  },
  watch: {
    //fetch on route change
    $route: "fetchData"
  },
  methods: {
    fetchData() {
      this.error = this.content = null;
      this.loading = true;
      $backend
        .getModel(this.$route.params.model)
        .then(responseData => {
          this.loading = false;
          this.content = responseData.content;
        })
        .catch(error => {
          this.error = error.message;
        });
    }
  }
};
</script>
