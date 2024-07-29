<template>
  <div>
    <h1>Checkout Pro </h1>
    <!-- contenedor para el botón de pago -->
    <div id="wallet_container"></div>
  </div>
</template>

<script setup>
import { defineProps, onMounted, ref } from 'vue';
import { inject } from 'vue'

const props = defineProps({
  message: {
    type: String,
    default: ''
  }
});

const userData = inject('userData')

const precio = parseFloat(userData.cost);
const ruta_name = String(userData.origen + " a "+ userData.destino);
const ruta_id = parseInt(userData.ruta_id);
const user_id = parseInt(userData.cliente_id);

let mp;

onMounted(() => {
  mp = new window.MercadoPago('APP_USR-db370930-9f78-4e51-8862-eb6c8634b1ad');
  createPaymentButton();
});

function createPaymentButton() {
    
  const url = `http://localhost:8000/api/create_preference/${precio}/${ruta_name}/${ruta_id}/${user_id}/`;

  fetch(url)  // aquí va la ruta definida en el backend 
    .then(response => response.json())
    .then(preference => {
      // inicializar el botón de pago
      mp.bricks().create('wallet', 'wallet_container', {
        initialization: {
          preferenceId: preference.id,  // Usa el ID de la preferencia
        },
        customization: {
          texts: {
            valueProp: 'smart_option',
          },
        },
      });
    })
    .catch(error => console.error('Error:', error));
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap');

h1 {
  font-family: 'Roboto Mono', monospace;
}
</style>
