<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';

const route = useRoute();
const username = ref(route.params.username);
const viajes = ref([]);
const selectedViaje = ref(null); // Para almacenar el viaje seleccionado
const message = ref(''); // Para el mensaje de selección

onMounted(async () => {
  try {
    const response = await axios.get('/api/viajes');
    viajes.value = response.data;
  } catch (error) {
    console.error('Error fetching viajes:', error);
  }
});

const selectDestination = async (viaje) => {
  selectedViaje.value = viaje; // Guarda el viaje seleccionado
  message.value = `Has elegido el viaje de ${viaje.startingPlace} a ${viaje.destinationPlace}`; 

  try {
    // Enviar datos al backend
    const userId = 'user-id-placeholder'; // id de usuario
    await axios.post('/api/seleccionar-viaje', {
      viajeId: viaje.id,
      userId: userId
    });
  } catch (error) {
    console.error('Error sending viaje selection:', error);
  }
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
      <p v-if="message" class="selection-message">{{ message }}</p>
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
.selection-message {
  margin-top: 20px;
  font-size: 1.2rem;
  color: #333;
}
</style>