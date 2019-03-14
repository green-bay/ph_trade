<template>
  <div>
    <v-dialog title="Nowe ogłoszenie" @close="addAd = false">
      <p>Dialog</p>
    </v-dialog>
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
      $backend
        .postAd(payload)
        .then(ad => {
          this.$emit("ad-posted", ad);
        })
        .catch(error => {
          this.error = error;
        });
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
