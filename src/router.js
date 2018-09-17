import Vue from 'vue'
import Router from 'vue-router'
//import Board from './views/Board.vue'
const routeOptions = [
	{ path: '/', component: 'Board' },
	{ path: '/api', component: 'Api' }
]

const routes = routeOptions.map( route => {
    return {
	...route,
	component: () => import(`@/views/${route.component}.vue`)
    }
})

Vue.use(Router)

export default new Router({
    routes,
    mode: 'history'
})
