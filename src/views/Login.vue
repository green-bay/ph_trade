<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md4>
        <v-card class="elevation-12">
          <v-toolbar dark color="primary">
            <v-toolbar-title>Login form</v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <p v-if="error" class="error">{{ error }}</p>
              <v-text-field
                prepend-icon="person"
                name="login"
                label="Login"
                type="text"
                v-model="email"
              />
              <v-text-field
                prepend-icon="lock"
                name="password"
                label="Hasło"
                id="password"
                type="password"
                v-model="password"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="login">Login</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import $backend from "../backend";

export default {
  name: "loginForm",
  data: function() {
    return {
      error: "",
      email: "",
      password: ""
    };
  },
  methods: {
    login: function() {
      const { email, password } = this;
      $backend
        .loginUser({ email, password })
        .then(resp => {
          this.$router.push("/account");
        })
        .catch(err => {
          console.log(err);
          if (err.response.status === 404) {
            this.error = "User or login incorrect. Try again";
          } else {
            console.log(err);
          }
        });
    }
  }
};
</script>
