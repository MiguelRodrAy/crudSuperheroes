import { createRouter, createWebHistory } from 'vue-router';
const Login = () => import('../views/Login.vue');
const MainMenu = () => import('../views/MainMenu.vue');
const Register = () => import('../views/Register.vue');

const routes = [
  { path: '/login', component: Login }, 
  { path: '/menu', component: MainMenu },
  { path: '/register', component: Register },
  {
    path: '/',
    redirect: () => {
      const token = localStorage.getItem('token');
      return token ? '/menu' : '/login';
    }
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to) => {
    const token = localStorage.getItem('token');
    if (to.path === '/menu' && !token) {
      return '/login';
    }
  });

export default router;
