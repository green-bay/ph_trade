import Vue from 'vue'

var store = {
    state: {
	userLogged: false,
	userName: 'guest'
    }
}

store.install = function() {
  Object.defineProperty(Vue.prototype, '$ph_shared', {
      get () { return store }
  })
}

export default {
    store
}
