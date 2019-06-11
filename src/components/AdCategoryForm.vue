<template>
  <div>
    <p>Nowa Kategoria</p>
    <v-form>
      <v-layout row wrap>
        <v-flex sm12>
          <v-text-field
            v-model="addCatForm.name"
            label="Nazwa"
            required
          ></v-text-field>
        </v-flex>
      </v-layout>
    </v-form>
    <v-btn round outline @click.native.prevent="postCat()">Zapisz</v-btn>
    <v-btn round outline @click.native.prevent="close()">Anuluj</v-btn>
  </div>
</template>

<script>
import $backend from "../backend";

export default {
  name: "AdCategoryForm",
  data: function() {
    return {
      addCat: false,
      addCatForm: {
        name: ""
      },
      error: false
    };
  },
  methods: {
    postCat: function() {
      let payload = {
        name: this.addCatForm.name
      };
      $backend
        .postCat(payload)
        .then(cat => {
          this.$emit("cat-posted", cat);
        })
        .catch(error => {
          this.error = error;
        });
      this.close();
    },
    close: function() {
      this.$emit("cat-post-cancel");
    }
  }
};
</script>
