<template>
  <div class="container">
    <h1>Registro de Viaje</h1>
    <div v-if="message">{{ message }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();
const message = ref('');

// se capturan los parámetros de la URL
const rutaId = parseInt(route.query.ruta);
const userId = parseInt(route.query.user_id);
const cost = parseFloat(route.query.cost);

const voucherData = ref(null);

console.log("Parámetros recibidos:", rutaId, userId, cost);

onMounted(async () => {
  // se debe vrifcar si ya se ha registrado el viaje en esta sesión
  const registrationKey = `trip_${rutaId}_${userId}`;
  
  try {
    // Enviar los datos al back
    const response = await axios.post('http://localhost:8000/api/registrar_viaje/', {
      ruta_id: rutaId,
      cliente_id: userId,
      cost: cost
    });

    // Guardar la clave en el almacenamiento de la sesión
    sessionStorage.setItem(registrationKey, 'registered');

    // Manejar la respuesta del backend
    message.value = response.data.message;

    // mandar al cliente  a la página de perfil después del registro exitoso
    router.push({ name: 'PerfilUsuario' }).then(() => {
      // Reemplazar la entrada actual en el historial para evitar volver atrás
    history.replaceState(null, '', location.href);
    });

  } catch (error) {
    console.error('Error al registrar el viaje:', error);
    message.value = 'Error al registrar el viaje: ' + (error.response ? error.response.data.error : error.message);

    // Redirigir a la página de perfil en caso de credenciales incorrectas
    if (error.response && error.response.status === 401) {
      router.push({ name: 'PerfilUsuario' });
    }
  }
});
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
  border: 1px solid #ddd;
  border-radius: 8px;
}
</style>
