<template>
    <div>
	<h1>Login</h1>
	<form class="login" @submit.prevent="login">
	    <p v-if="error" class='error'>{{ error }}</p>
	    <VueFormField title="email" placeholder="email">
		<VueInput v-model="email" />
	    </VueFormField>
	    <VueFormField title="Hasło" placeholder="Hasło">
		<VueInput v-model="password" 
			  icon-right="lock"
			  type="password" />
	    </VueFormField>
	    <VueButton class="big" label="Sign In" type="submit" />
	</form>
    </div>
</template>

<script>
import $backend from '../backend'

export default {
    name: 'loginForm',
    data: function(){
	return {
	    error: '',
	    email: '',
	    password: '',
	}
    },
    methods: {
	login: function() {
	    const {email, password} = this;
	    $backend.loginUser({email,password})
		.then(resp => {
		    this.$router.push('/account')
		}).catch(err => {
		    console.log(err);
		  if(err.response.status === 404){
		    this.error = 'User or login incorrect. Try again'
		  }else{
		    console.log(err);
		  }
	       })
	}
    }
}
</script>

<style scoped lang='scss'>
.login {
    width: 60%;
    margin: 0 auto;
}
.error {
    color: red;
}
</style>
