import Vue from 'vue';
import ElementUI from 'element-ui';
// import VueAxios from 'vue-axios';
import BootstrapVue from 'bootstrap-vue';
import axios from './httpconfigs/http';
import App from './App.vue';
import router from './router';
import 'element-ui/lib/theme-chalk/index.css';

Vue.prototype.$axios = axios;
Vue.config.productionTip = false;
Vue.use(ElementUI);
// Vue.use(VueAxios, Vue.$axios);
Vue.use(BootstrapVue);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
