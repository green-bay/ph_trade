import Vue from 'vue'
import Router from 'vue-router'
//import Board from './views/Board.vue'
import Api from './views/Api.vue'
//import Sandbox from './views/Sandbox.vue'

Vue.use(Router)

export default new Router({
    routes: [
/*	{
	    path: '/',
	    name: 'board',
	    component: Board
	},
*/	{
	    path: '/api',
	    name: 'api',
	    component: Api
	},
/*	{
	    path: '/sandbox',
	    name: 'sandbox',
	    component Sandbox
	}
*/    ]
})
