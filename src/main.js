import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import "babel-polyfill";
import Vuetify from "vuetify/lib";
import "vuetify/src/stylus/app.styl";
import "material-design-icons-iconfont/dist/material-design-icons.css";

Vue.config.productionTip = false;

Vue.use(Vuetify, {
  iconfont: "md", // 'md' || 'mdi' || 'fa' || 'fa4',
  theme: {
    primary: "#228B22"
  }
});

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
