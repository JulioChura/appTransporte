import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import RegisterCliente from '../components/RegisterCliente.vue';
import SeleccionDestino from '../views/SeleccionDestino.vue';

// Definir las rutas
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
  }
];

// Crear y exportar el enrutador
const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;


