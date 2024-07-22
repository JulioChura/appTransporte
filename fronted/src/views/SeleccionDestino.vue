<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import Voucher from '../components/Voucher.vue'; // Importa el componente Voucher

const username = ref(''); // Obtén el nombre de usuario de la ruta o de alguna otra manera
const viajes = ref([]);
const voucherData = ref(null); // Datos del voucher
const message = ref('');
const showModal = ref(false); // Estado para mostrar el modal

// Función para obtener los viajes
onMounted(async () => {
  try {
    const response = await axios.get('/api/viajes');
    viajes.value = response.data;
  } catch (error) {
    console.error('Error fetching viajes:', error);
  }
});

// Función para seleccionar un destino
const selectDestination = async (viaje) => {
  try {
    const userId = 'user-id-placeholder'; // ID de usuario
    const response = await axios.post('/api/seleccionar-viaje', {
      viajeId: viaje.id,
      userId: userId
    });

    voucherData.value = response.data.voucher;
    message.value = response.data.message;
    showModal.value = true; // Muestra el modal

  } catch (error) {
    console.error('Error sending viaje selection:', error);
  }
};

// Función para cerrar el modal
const closeModal = () => {
  showModal.value = false; // Cierra el modal
};
</script>

<template>
  <header class="header">
    <div class="header__nav">
      <h1 class="header__nav-titulo">
        <a href="#" class="nombre">AQPTransporte</a>
      </h1>
    </div>

    <div class="header__descripcion">
      <div class="header__descripcion-texto">
        <h1 class="header__descripcion-titulo">Destinos</h1>
        <p class="header__descripcion-mensaje">
          Viaja con nosotros, Viaja seguro
        </p>
      </div>
    </div>
  </header>

  <div class="travel-selection">
    <h1>Selecciona tu destino de viaje, {{ username }}</h1>
    <div class="destinations">
      <div 
        v-for="viaje in viajes" 
        :key="viaje.id" 
        class="destination-card"
        @click="selectDestination(viaje)"
      >
        <div class="destination-info">
          <h2>{{ viaje.startingPlace }} - {{ viaje.destinationPlace }}</h2>
          <p>Distancia: {{ viaje.distance }} km</p>
          <p>Paradas: {{ viaje.stops }}</p>
          <p>Horario: {{ viaje.horario }}</p>
          <p>Fecha: {{ viaje.fecha }}</p>
        </div>
      </div>
    </div>

    <!-- Modal para mostrar los datos del voucher -->
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <Voucher :voucher="voucherData" :message="message" />
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Diseño de inicio */
.header {
    margin: 0;
    padding: 0;
}

.header__nav {
    background-color: black;
    color: white;
    display: flex;
    justify-content: space-between;
}

.header__nav-titulo .nombre {
    text-decoration: none;
    margin-left: 3rem;
    font-size: 4rem;
    height: 5rem;
    color: white;
}

.header__descripcion {
    height: 40rem;
    background-image: url("../../public/images/2.jpeg");
    background-repeat: no-repeat;
    background-size: cover;
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.header__descripcion-titulo {
    text-align: center;
    font-size: 3.5rem;    
    color: rgb(253, 253, 253);
}

.header__descripcion-texto {
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.8);
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.header__descripcion-mensaje {
    text-align: center;
    margin: 1rem;
    font-size: 3rem;
    color: wheat;
}

/* Diseño para destinos */
.travel-selection {
  padding: 20px;
}

.destinations {
  display: flex;
  flex-direction: column; /* Cambia la disposición a una lista vertical */
  gap: 20px;
}

.destination-card {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.destination-card:hover {
  background-color: #eaeaea;
}

.destination-info {
  color: #333;
}

/* Estilos del modal */
.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0,0,0,0.4);
}

.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
</style>