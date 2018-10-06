<template>
    <div>
	<h1>ph_trade</h1>
	<ClassifiedForm
	    v-on:ad-posted='ads.push($event)'
	/>
	<Classifiedad 
	    v-for='(ad, ix) in ads'
	    :key='ix'
	    v-bind:ad='ad' />
    </div>
</template>

<script>
import Classifiedad from '../components/ClassifiedAd'
import ClassifiedForm from '../components/ClassifiedForm'
import $backend from '../backend'

export default {
    name: 'board',
    components: {
	Classifiedad,
	ClassifiedForm
    },
    data: function() {
	return {
	    ads: []
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
	},
	postAd: function() {
	    $backend.postAd(payload)
	    	.then(ad => {
		    this.ads.push(ad)
		}).catch(error => {
		    this.error = error
		})
	},
    },
    created: function() {
	return this.getAds()
    }

}
</script>
