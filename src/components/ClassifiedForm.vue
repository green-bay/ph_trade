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
        categories_set: [],
        publisher: "",
        image: "",
        errors: []
      }
    };
  },
  created: function() {
    return this.getAttrs();
  },
  methods: {
    getAttrs: function() {
      $backend
        .getAdAttrs()
        .then(res => {
          let cats = res.cats.map(cat => {
            return cat.name;
          });
          this.addAdForm.categories_set = cats;
        })
        .catch(error => {
          this.error = error;
        });
    },
    postAd: function() {
      let payload = {
        name: this.addAdForm.name,
        description: this.addAdForm.desc,
        categories: this.addAdForm.categories,
        publisher: "anonymous" //we will get it from user
      };
      $backend
        .postAd(payload)
        .then(ad => {
          this.$emit("ad-posted", ad);
        })
        .catch(error => {
          this.error = error;
        });
      this.close();
    },
    close: function() {
      this.$emit("ad-post-cancel");
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
