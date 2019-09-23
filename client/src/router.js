import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/home/Home.vue';
import Login from './views/home/Login.vue';
import Register from './views/home/Register.vue';
import AdminHome from './views/admin/AdminHome.vue';
import TagList from './views/admin/TagList.vue';
import PreviewList from './views/admin/PreviewList.vue';
import MovieList from './views/admin/MovieList.vue';
import AuthList from './views/admin/AuthList.vue';
import RoleList from './views/admin/RoleList.vue';
import AdminList from './views/admin/AdminList';

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
      path: '/register',
      name: 'admin-register',
      component: AdminHome,
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
  ],
});
