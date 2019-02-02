<template>
	<div>
	    <h1>Login</h1>
		<v-form class="login" @submit.prevent="login">
		    <p v-if="error" class='error'>{{ error }}</p>
		    <v-input v-model="email">Email</v-input>
		    <v-input v-model="password" 
				  icon-right="lock"
				  type="password">Hasło</v-input>
		    <v-btn class="big" label="Sign In" type="submit" />
		</v-form>
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
