import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/home/Home.vue';
import Login from './views/home/Login.vue';
import Register from './views/home/Register.vue';
import AdminHome from './views/admin/AdminHome.vue';
import TagList from './views/admin/TagList.vue';
import AdminTagAdd from './views/admin/AdminTagAdd.vue';
import TagEdit from './views/admin/TagEdit.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
    },
    {
      path: '/admin',
      name: 'admin',
      component: AdminHome,
    },
    {
      path: '/admin/tag/list',
      name: 'tag-list',
      component: TagList,
    },
    {
      path: '/admin/tag/add',
      name: 'tag-add',
      component: AdminTagAdd,
    },
    {
      path: '/admin/tag/edit',
      name: 'tag-edit',
      component: TagEdit,
    },
  ],
});
