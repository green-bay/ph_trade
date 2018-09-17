import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueUi from '@vue/ui'

Vue.config.productionTip = false

Vue.use(VueUi)

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
