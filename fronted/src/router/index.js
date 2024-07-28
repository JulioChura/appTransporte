import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import RegisterCliente from '../components/RegisterCliente.vue';
import SeleccionDestino from '../views/SeleccionDestino.vue';
import PerfilUsuario from '../views/PerfilUsuario.vue';
import Contacto from '../views/Contacto.vue';
import temporalPago
 from '../views/temporalPago.vue';
import SobreNosotros from '../views/SobreNosotros.vue';
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
  },
  {
    path: '/perfil', // Nueva ruta para PerfilUsuario.vue
    name: 'PerfilUsuario',
    component: PerfilUsuario
  },
  {
    path: "/contacto",
    name: "contacto",
    component: Contacto
  },

  // probar lo de la confirmacion de pago
  {
    path: "/registrado",
    name: "registradoViaje",
    component: temporalPago
  },

  // va a la rama principal
  {
    path: "/sobreNosotros",
    name: "SobreNosotros",
    component: SobreNosotros
  }
];

// Crear y exportar el enrutador
const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;


