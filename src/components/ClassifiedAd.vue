<template>
    <div v-on:click='show_ad' class='classified-ad'>
	<img class='classified-img' :src="ad.image" />
	<div class='classified-ad-details'>
	    <h4 class='ad-category'>{{ ad.category }}</h4>
	    <h3 class='ad-title'>{{ ad.name }}</h3>
	    <p class='ad-description'>{{ ad.desc }}</p>
	    <p class='ad-publisher'>{{ ad.publisher }}</p>
	</div>
    </div>
</template>

<script>
import $backend from '../backend.js';

export default {
    name: 'Classifiedad',
    props: ['ad'],
    methods: {
	show_ad: function(ev){
	    alert('Hello ' + this.ad.name + '!')
	    if (ev){
		alert(ev.target.tagName)
	    }
	}
    }
}
</script>

<style scoped lang='scss'>
.classified-ad {
    display: flex;
    flex-direction: row;
    background: #fff;
    box-shaddow: 0 0.1875rem 1.5rem #000;
    border-radius: 0.375rem;
    overflow: hidden;
    border: 1px solid;
    width: 400px;
    height: 200px;
    margin: 1em auto;

    &:hover {
	cursor: pointer;
    }

    .classified-img {
	width: 35%;
    }

    .classified-ad-details {
	width: 65%;
    }
}
</style>
