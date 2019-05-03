<template>
  <v-flex md3 mx-2>
    <v-card v-on:click="show_ad" class="classified-ad">
      <img class="classified-img" :src="ad.image" />
      <div class="classified-ad-details">
        <h4 class="ad-category">{{ ad.category }}</h4>
        <h3 class="ad-title">{{ ad.name }}</h3>
        <p class="ad-description">{{ ad.description }}</p>
        <p class="ad-publisher">{{ ad.created_at }}, {{ ad.publisher }}</p>
      </div>
    </v-card>
  </v-flex>
</template>

<script>
import $backend from "../backend.js";

export default {
  name: "Classifiedad",
  props: ["ad"],
  methods: {
    show_ad: function(ev) {
      alert("Hello " + this.ad.name + "!");
      if (ev) {
        alert(ev.target.tagName);
      }
    }
  }
};
</script>
