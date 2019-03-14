<template>
  <v-layout>
    <v-flex xs12>
      <v-layout align-space-around fill-height>
        <v-flex md2>
          <v-card height="100%">
            <div class="text-xs-center">
              <v-btn round outline @click.native.prevent="addAd = true"
                >Dodaj Ogłoszenie</v-btn
              >
            </div>
          </v-card>
        </v-flex>
        <v-flex md10>
          <h1>Some title</h1>
          <ClassifiedForm v-on:ad-posted="ads.push($event)" />
          <Classifiedad v-for="(ad, ix) in ads" :key="ix" v-bind:ad="ad" />
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>

<script>
import Classifiedad from "../components/ClassifiedAd";
import ClassifiedForm from "../components/ClassifiedForm";
import $backend from "../backend";

export default {
  name: "board",
  components: {
    Classifiedad,
    ClassifiedForm
  },
  data: function() {
    return {
      ads: []
    };
  },
  methods: {
    getAds: function() {
      $backend
        .fetchAds()
        .then(adsData => {
          this.ads = adsData;
        })
        .catch(error => {
          this.error = error;
        });
    },
    postAd: function() {
      $backend
        .postAd(payload)
        .then(ad => {
          this.ads.push(ad);
        })
        .catch(error => {
          this.error = error;
        });
    }
  },
  created: function() {
    return this.getAds();
  }
};
</script>
