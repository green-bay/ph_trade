<template>
  <v-app>
    <v-toolbar>
    		<v-spacer></v-spacer>
    		<v-toolbar-items>
    			<v-btn flat>
	    	    	<router-link to="/">PH_TRADE</router-link>
	    	    </v-btn>
	    	    <v-btn flat>
	    	    	<router-link to="/board">Tablica Ogłoszeń</router-link>
	    	    </v-btn>
	    	    <v-btn flat>
					<router-link to="/api">Piaskownica</router-link>
				</v-btn>
				<v-btn flat>
					<router-link to="/login">Login</router-link>
				</v-btn>
			</v-toolbar-items>
	</v-toolbar>
    <!--<HelloWorld msg="Welcome to Your Vue.js App"/>-->
    <v-content>
    	<v-container>
    		<v-layout row wrap>
    			<v-flex>
			        <v-card>
			          <v-card-text><router-view /></v-card-text>
			        </v-card>
			    </v-flex>    			
    		</v-layout>
    	</v-container>
    </v-content>
    <v-footer class="pa-3">
	    <v-spacer></v-spacer>
	    <div>PH_TRADE &copy; {{ new Date().getFullYear() }}</div>
	  </v-footer>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'app',
  components: {
    HelloWorld
  }
}
</script>
