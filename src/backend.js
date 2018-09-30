import axios from 'axios'

let $axios = axios.create({
    baseURL: '/api/',
    timeout: 5000,
    headers: {'Content-Type': 'application/json'}
})

$axios.interceptors.request.use(function(config){
    config.headers['Authorization'] = 'Bearer: ' + localStorage.getItem('user-token');
    return config
})

$axios.interceptors.response.use(function(response){
    return response
}, function(err){
    if (err.status === 401 && err.config && err.config.__isRertyRequest){
	localStorage.removeItem('user-token');
	window.location = '/login';
    } else {
    	//console.log(err)
    	return Promise.reject(err)
    }
})

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
		const auth_token = response.data.auth_token;
		localStorage.setItem('user-token', auth_token);
	        return response.data;
	    })
	   .catch(err => {
	       localStorage.removeItem('user-token');
	       return Promise.reject(err);
	   })
    },
    logoutUser(){
	return $axios.post('logout')
	   .then(response => {
	       localStorage.removeItem('user-token');
	       Promise.resolve(response);
	   })
    }
}
