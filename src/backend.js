import axios from 'axios'

let $axios = axios.create({
    baseURL: '/api/',
    timeout: 5000,
    headers: {'Content-Type': 'application/json'}
})

$axios.interceptors.request.use(function(config){
    return config
})
/*
$axios.interceptors.response.use(function(response){
    return response
}, function(err){
    if (err.response.status === 401 && err.config && err.config.__isRertyRequest){
	window.location = '/login';
    } else {
    	return Promise.reject(err)
    }
})*/

export default {
    fetchAds(){
	return $axios.get('ads')
	    .then(response => response.data)
    },
    postAd(payload){
	return $axios.post('ads', payload)
	    .then(response => response.data)
    },
    fetchResource(){
	return $axios.get('resource/xxx')
	   .then(response => response.data)
    },

    fetchSecureResource(){
	return $axios.get('secure-resource/zzz')
	   .then(response => response.data)
    },
    loginUser(payload){
	return $axios.post('login', payload)
	   .then(response => {
	        return response.data;
	    })
	   .catch(err => {
	       return Promise.reject(err);
	   })
    },
    isAuthenticated(){
	return $axios.get('user/is_authenticated')
	   .then(response => {
	   	return Promise.resolve(true);
	   })
	   .catch(err => {
		return Promise.reject(false);
	   })
    },
    logoutUser(){
	return $axios.get('logout')
	   .then(response => {
	       Promise.resolve(response);
	   })
    }
}
