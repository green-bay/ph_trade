<template>
  <div>
    <h1>Restricted Area</h1>
    <h2>User account vue; not implemented yet</h2>
    <v-btn label="Logout" @click="logout" />
  </div>
</template>

<script>
import $backend from "../backend";

export default {
  name: "userAccount",
  methods: {
    logout: function() {
      $backend.logoutUser().then(this.$router.push("/"));
    }
  }
};
</script>
