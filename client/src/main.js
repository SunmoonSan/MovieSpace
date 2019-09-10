import Vue from 'vue';
import ElementUI from 'element-ui';
import axios from 'axios';
import VueAxios from 'vue-axios';
import App from './App.vue';
import router from './router';
import './assets/base/css/bootstrap.css';
import './assets/base/css/bootstrap-movie.css';
import './assets/base/css/animate.css';
import 'element-ui/lib/theme-chalk/index.css';


Vue.config.productionTip = false;
Vue.use(ElementUI);
Vue.use(VueAxios, axios);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
