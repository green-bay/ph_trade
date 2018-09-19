<template>
    <div>
	<h1>The Board</h1>
	<VueButton @click="addAd = true">Dodaj Ogłoszenie</VueButton>
	<VueModal
	    v-if="addAd"
            title="Nowe ogłoszenie"
	    @close="addAd = false"
	>
	    <p>Tu na razie jest ściernisko ale będzie San Francisko</p>
	</VueModal>
	<Classifiedad 
	    v-for='(ad, ix) in ads'
	    :key='ix'
	    v-bind:ad='ad'>
	</Classifiedad>
    </div>
</template>

<script>
import Classifiedad from '../components/ClassifiedAd'
import $backend from '../backend'

export default {
    name: 'board',
    components: {
	Classifiedad
    },
    data: function() {
	return {
	    ads: [],
	    error: '',
	    addAd: false
	}
    },
    methods: {
	getAds: function() {
	    $backend.fetchAds()
	       .then(adsData => {
		   this.ads = adsData
	       }).catch(error => {
		   this.error = error
	       })
	}
    },
    created: function() {
	return this.getAds()
    }

}
</script>
