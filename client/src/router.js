import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/home/Home.vue';
import Login from './views/home/Login.vue';
import AdminHome from './views/admin/AdminHome.vue';
import Register from './views/home/Register.vue';
import AdminLogin from './views/admin/Login.vue';
import TagList from './views/admin/TagList.vue';
import PreviewList from './views/admin/PreviewList.vue';
import MovieList from './views/admin/MovieList.vue';
import AuthList from './views/admin/AuthList.vue';
import RoleList from './views/admin/RoleList.vue';
import AdminList from './views/admin/AdminList.vue';
import AdminLoginLog from './views/admin/LoginLog.vue';
import AdminOpLog from './views/admin/OpLog.vue';

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
      path: '/register',
      name: 'register',
      component: Register,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
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
      path: '/admin/register',
      name: 'admin-register',
      component: AdminHome,
    },
    {
      path: '/admin/login',
      name: 'admin-login',
      component: AdminLogin,
    },
    {
      path: '/admin/tag/list',
      name: 'tag-list',
      component: TagList,
    },
    {
      path: '/admin/preview/list',
      name: 'preview-list',
      component: PreviewList,
    },
    {
      path: '/admin/movie/list',
      name: 'movie-list',
      component: MovieList,
    },
    {
      path: '/admin/auth/list',
      name: 'auth-list',
      component: AuthList,
    },
    {
      path: '/admin/role/list',
      name: 'role-list',
      component: RoleList,
    },
    {
      path: '/admin/admin/list',
      name: 'admin-list',
      component: AdminList,
    },
    {
      path: '/admin/log/admin',
      name: 'log-admin',
      component: AdminLoginLog,
    },
    {
      path: '/admin/log/op',
      name: 'log-op',
      component: AdminOpLog,
    },
  ],
});
