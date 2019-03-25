import Vue from "vue";
import Router from "vue-router";
import backend from "@/backend";

const ifAuthenticated = (to, from, next) => {
  var x = backend.isAuthenticated();
  x.then(function(resp) {
    next();
  }).catch(err => {
    next("/login");
  });
};

const ifNotAuthenticated = (to, from, next) => {
  var x = backend.isAuthenticated();
  x.then(resp => {
    next("/account");
  }).catch(err => {
    next();
  });
};

const routeOptions = [
  { path: "/", component: "Home" },
  { path: "/board", component: "Board" },
  { path: "/api", component: "Api" },
  {
    path: "/account",
    component: "Account",
    beforeEnter: ifAuthenticated,
    children: [
      {
        path: "/models/:model",
        component: () => import(`@/components/Model.vue`),
        name: "modelRoute"
      }
    ]
  },
  { path: "/login", component: "Login", beforeEnter: ifNotAuthenticated }
];

const routes = routeOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/views/${route.component}.vue`)
  };
});

Vue.use(Router);

export default new Router({
  routes,
  mode: "history"
});
