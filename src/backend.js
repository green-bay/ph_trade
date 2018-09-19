import axios from 'axios'

let $axios = axios.create({
    baseURL: '/api/',
    timeout: 5000,
    headers: {'Content-Type': 'application/json'}
})

$axios.interceptors.request.use(function(config){
    config.headers['Authorization'] = 'Fake Token'
    return config
})

$axios.interceptors.response.use(function(response){
    return response
}, function(error){
    console.log(error)
    return Promise.reject(error)
})

export default {
    fetchAds(){
	return $axios.get('ads').
	    then(response => response.data)
    },

    fetchResource(){
	return $axios.get('resource/xxx')
	   .then(response => response.data)
    },

    fetchSecureResource(){
	return $axios.get('secure-resource/zzz')
	   .then(response => response.data)
    }
}
