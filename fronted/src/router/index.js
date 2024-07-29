import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import RegisterCliente from '../components/RegisterCliente.vue';
import SeleccionDestino from '../views/SeleccionDestino.vue';
import PerfilUsuario from '../views/PerfilUsuario.vue';
import Contacto from '../views/Contacto.vue';
import temporalPago from '../views/temporalPago.vue';
import SobreNosotros from '../views/SobreNosotros.vue';
import { getCurrentUser } from '../services/authService';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/register',
    name: 'RegisterCliente',
    component: RegisterCliente
  },
  {
    path: '/destinos', 
    name: 'SeleccionDestino',
    component: SeleccionDestino
  },
  {
    path: '/perfil',
    name: 'PerfilUsuario',
    component: PerfilUsuario
  },
  {
    path: "/contacto",
    name: "contacto",
    component: Contacto
  },
  {
    path: "/registrado",
    name: "registradoViaje",
    component: temporalPago
  },
  {
    path: "/sobreNosotros",
    name: "SobreNosotros",
    component: SobreNosotros
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  const publicPages = ['/', '/login', '/register', '/contacto', '/sobreNosotros'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = getCurrentUser();

  if (authRequired && !loggedIn) {
    return next('/');
  }

  next();
});

export default router;


