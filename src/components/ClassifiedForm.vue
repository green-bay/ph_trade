<!--ClassifiedForm Component-->
<template>
  <div>
    <p>Nowe Ogłoszenie</p>
    <v-btn round outline @click.native.prevent="postAd()">Zamknij</v-btn>
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
        publisher: "",
        image: "",
        errors: []
      }
    };
  },
  methods: {
    postAd: function(payload) {
      this.$emit("ad-posted", "lol");
      /*$backend
        .postAd(payload)
        .then(ad => {
          this.$emit("ad-posted", ad);
        })
        .catch(error => {
          this.error = error;
        });*/
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
    }
  }
};
</script>
