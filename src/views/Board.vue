<!--Board View-->
<template>
  <v-layout>
    <v-flex xs12>
      <v-layout align-space-around fill-height row wrap>
        <v-flex md2>
          <v-card height="100%">
            <div class="text-xs-center">
              <v-btn round outline @click.native.prevent="addAd = true"
                >Dodaj Ogłoszenie</v-btn
              >
            </div>
          </v-card>
        </v-flex>
        <transition name="fade" mode="out-in">
          <v-flex md10 v-if="addAd">
            <v-card height="100%">
              <div class="text-xs-center">
                <ClassifiedForm v-on:ad-posted="postAd" />
              </div>
            </v-card>
          </v-flex>
          <v-flex md10 v-else>
            <v-card height="100%">
              <div class="text-xs-center">
                <h1>Some title</h1>
                <v-layout row wrap align-center justify-center>
                  <Classifiedad v-for="ad in ads" :key="ad.id" v-bind:ad="ad" />
                </v-layout>
              </div>
            </v-card>
          </v-flex>
        </transition>
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
      ads: [],
      addAd: false
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
    postAd: function(ad) {
      if (ad) this.ads.push(ad);
      this.addAd = false;
    }
  },
  created: function() {
    return this.getAds();
  }
};
</script>
