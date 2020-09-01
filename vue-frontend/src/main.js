// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import App from "./App";
import router from "./router";

import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
// Install BootstrapVue
Vue.use(BootstrapVue);
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin);

//ScrollTo
const VueScrollTo = require("vue-scrollto");
Vue.use(VueScrollTo);
Vue.config.productionTip = false;

// import 'jsmind'
import jm from "vue-jsmind";
Vue.use(jm);

// var editor = require('./editor.vue');
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
// use
Vue.use(mavonEditor)

import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)
Vue.prototype.$axios = axios;

// Vue.filter("marked", function(input) {
//   return marked(input);
// });

// import myUpload from "vue-image-crop-upload/upload-1.vue";
// Vue.use(myUpload);

/* eslint-disable no-new */
new Vue({
  el: "#app",
  // render: h => h(editor),
  router,
  components: { App },
  template: "<App/>"
});
