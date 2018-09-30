import Vue from 'vue'
import Router from 'vue-router'

const ifAuthenticated = (to, from, next) => {
    if (localStorage.getItem('user-token')) {
	next();
	return
    }
    next('/login')
}

const ifNotAuthenticated = (to, from, next) => {
    if (!localStorage.getItem('user-token')) {
	next();
	return
    }
    next('/')
}

const routeOptions = [
	{ path: '/', component: 'Board' },
	{ path: '/api', component: 'Api' },
    	{ path: '/account', component: 'Account', beforeEnter: ifAuthenticated },
    	{ path: '/login', component: 'Login', beforeEnter: ifNotAuthenticated }
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
