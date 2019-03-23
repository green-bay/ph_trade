<!--ClassifiedForm Component-->
<template>
  <div>
    <p>Nowe Ogłoszenie</p>
    <v-form>
      <v-layout row wrap>
        <v-flex md8 sm12 pa-2>
          <v-text-field
            v-model="addAdForm.name"
            label="Tytuł"
            required
          ></v-text-field>
          <v-textarea
            v-model="addAdForm.desc"
            label="Opis"
            required
          ></v-textarea>
        </v-flex>
        <v-flex md4 sm12 pa-2>
          <v-combobox
            v-model="addAdForm.categories"
            :items="addAdForm.categories_set"
            label="Kategorie"
            chips
            clearable
            solo
            multiple
          >
            <template v-slot:selection="data">
              <v-chip close @input="removeCat(data.item)">
                <strong>{{ data.item }}</strong>
              </v-chip>
            </template>
          </v-combobox>
          <v-text-field clearable solo label="Obrazek"> </v-text-field>
        </v-flex>
      </v-layout>
    </v-form>
    <v-btn round outline @click.native.prevent="postAd()">Wyślij</v-btn>
    <v-btn round outline @click.native.prevent="close()">Anuluj</v-btn>
  </div>
</template>

<script>
import $backend from "../backend";

export default {
  name: "ClassifiedForm",
  data: function() {
    return {
      error: "",
      addAd: false,
      addAdForm: {
        name: "",
        desc: "",
        category: "",
        categories: [],
        categories_set: ["susz", "wiecha", "ziarno", "cbd"],
        publisher: "",
        image: "",
        errors: []
      }
    };
  },
  methods: {
    postAd: function() {
      $backend
        .postAd(this.addAdForm)
        .then(ad => {
          this.$emit("ad-posted", ad);
        })
        .catch(error => {
          this.error = error;
        });
      this.close();
    },
    close: function() {
      this.$emit("ad-posted");
    },
    checkForm: function(e) {
      e.preventDefault();
      const valid = true;
      this.addAd = false;
      if (valid) {
        const payload = {
          name: this.addAdForm.name,
          category: this.addAdForm.category,
          publisher: this.addAdForm.publisher,
          description: this.addAdForm.desc
        };
        this.postAd(payload);
      }
    },
    removeCat: function(item) {
      this.addAdForm.categories.splice(
        this.addAdForm.categories.indexOf(item),
        1
      );
      this.addAdForm.categories = [...this.addAdForm.categories];
    }
  }
};
</script>
