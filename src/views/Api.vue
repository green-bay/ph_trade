<template>
  <div class="about">
    <h1>Backend api demo ssuf</h1>
    <p>Click to get data</p>
    <v-btn @click.prevent="fetchResource">Fetch Data</v-btn><br />
    <a href="" @click.prevent="fetchSecureResource">Fetch Secured Resource</a>
    <h4>Results</h4>
    <p v-for="r in resources" :key="r.timestamp">
      Server Timestamp: {{ r.timestamp }}
    </p>
    <p>{{ error }}</p>
  </div>
</template>

<script>
import $backend from "../backend";

export default {
  name: "about",
  data() {
    return {
      resources: [],
      error: ""
    };
  },
  methods: {
    fetchResource() {
      $backend
        .fetchResource()
        .then(responseData => {
          this.resources.push(responseData);
        })
        .catch(error => {
          this.error = error.message;
        });
    },
    fetchSecureResource() {
      $backend
        .fetchSecureResource()
        .then(responseData => {
          this.resources.push(responseData);
        })
        .catch(error => {
          this.error = error.message;
        });
    }
  }
};
</script>
