<template>
<div>
    <v-btn @click="addAd = true">Dodaj Ogłoszenie</v-btn>
    	<v-dialog persistent
	    	v-if="addAd"
            title="Nowe ogłoszenie"
	    	@close="addAd = false"
		>
			    <form 
				id="newAdForm"
				@submit="checkForm">
				<p v-if="addAdForm.errors.length"><b>Uzupełnij:</b>
				    <ul>
					<li v-for="e in addAdForm.errors">{{ e }}</li>
				    </ul>
				</p>
				<p>
				    <label for="addAdForm.name">Tytuł</label>
				    <input
			     		id="name"
					v-model="addAdForm.name"
		   			type="text"
		      			name="name"/>
				</p>
				<p>
				    <label for="category">Kategoria</label>
				    <select id="category" v-model="addAdForm.category" name="category">
					<option>nasiona</option>
					<option>susz</option>
				    </select>
				</p>
				<p>
				    <label for="desc">Treść</label>
				    <textarea
			     		id="desc"
					v-model="addAdForm.desc"
		      			name="desc"/>
				</p>
				<p>
				    <label for="publisher">Autor</label>
				    <input
			     		id="publisher"
					v-model="addAdForm.publisher"
		   			type="text"
		      			name="publisher">
				</p>
				<p>
				    <label for="image">URL obrazka</label>
				    <input
			     		id="image"
					v-model="addAdForm.image"
		   			type="url"
		      			name="image"/>
				</p>
				<p><input type="submit" value="Dodaj Ogłoszenie"/></p>
		    </form>
	</v-dialog>    
</div>
</template>

<script>
import $backend from '../backend'

export default {
    name: 'ClassifiedForm',
    data: function() {
	return {
	    error: '',
	    addAd: false,
	    addAdForm: {
		name: '',
		desc: '',
		category: '',
		publisher: '',
		image: '',
		errors: []
	    }
	}
    },
    methods: {
	postAd: function(payload) {
	    $backend.postAd(payload)
	    	.then(ad => {
		    this.$emit('ad-posted', ad)
		}).catch(error => {
		    this.error = error
		})
	},
	checkForm: function(e) {
	    e.preventDefault();
	    const valid = true;
	    if (!this.addAdForm.name){
		this.addAdForm.errors.push("Tytuł");
		valid = false
	    }
	    if (!this.addAdForm.publisher){
		this.addAdForm.errors.push("Autora");
		valid = false
	    }
	    this.addAd = false;
	    if(valid){
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
}
</script>
