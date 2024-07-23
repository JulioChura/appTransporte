<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import Voucher from '../components/Voucher.vue'; // Importa el componente Voucher

const username = ref(''); // Se obtiene el nombre de usuario de la ruta o de alguna otra manera
const user = ref(null); // Datos del usuario
const viajes = ref([]);
const voucherData = ref(null); // Datos del voucher
const message = ref('');
const showModal = ref(false); // Estado para mostrar el modal

// Función para obtener los datos del usuario y los viajes
onMounted(async () => {
  try {
    // Obtener información del usuario
    const storedUser = JSON.parse(localStorage.getItem('user'));
    if (storedUser) {
      user.value = storedUser.cliente;
      username.value = `${user.value.Name} ${user.value.LastName}`; // Nombre completo del cliente
    }

    // Obtener los viajes
    const response = await axios.get('http://localhost:8000/api/rutas/');
    viajes.value = response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
});

// Función para seleccionar un destino
const selectDestination = async (viaje) => {
  let cost = parseFloat(viaje.cost);
  console.log(cost);
  try {
    const userId = user.value?.id; // Recupera el id del usuario

    if (!userId) {
      console.error('User ID not found');
      return;
    }
    const response = await axios.post('http://localhost:8000/api/registrar_viaje/', {
      cliente_id: userId,
      ruta_id: viaje.id,
      cost: cost
    });

    voucherData.value = response.data.voucher;
    message.value = response.data.message;
    showModal.value = true; // Muestra el modal

  } catch (error) {
    console.error('Error sending viaje selection:', error);
    message.value = 'Error selecting destination: ' + (error.response ? error.response.data.error : error.message);
  }
};

// Función para cerrar el modal
const closeModal = () => {
  showModal.value = false; // Cierra el modal
};

// Función para obtener las iniciales del nombre del cliente
const getInitials = (firstName, lastName) => {
  if (!firstName || !lastName) return '';
  return firstName.charAt(0) + lastName.charAt(0);
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

  <div class="profile-section">
    <div class="profile-info">
      <div class="profile-avatar">
        <span class="avatar-initials">{{ getInitials(user?.Name, user?.LastName) }}</span> <!-- Muestra las iniciales del nombre del cliente -->
      </div>
      <h2>Bienvenido, {{ username }}</h2>
      <p>Correo: {{ user?.email }}</p>
      <p>Teléfono: {{ user?.Cellphone }}</p>
      <p>DNI: {{ user?.DNI }}</p> <!-- Datos adicionales del cliente -->
      <!-- Botón para redirigir a PerfilUsuario.vue -->
      <router-link to="/perfil">
        <button>Perfil</button>
      </router-link>
    </div>

    <div class="travel-selection">
      <h1>Selecciona tu destino de viaje</h1>
      <div class="destinations">
        <div 
          v-for="viaje in viajes" 
          :key="viaje.id" 
          class="destination-card"
        >
          <div class="destination-info">
            <h2>{{ viaje.startingPlace }} - {{ viaje.destinationPlace }}</h2>
            <p>Distancia: {{ viaje.distance }} km</p>
            <p>Paradas: {{ viaje.stops }}</p>
            <p>Horario: {{ viaje.horario }}</p>
            <p>Fecha: {{ viaje.fecha }}</p>
            <p>Precio: S/{{ viaje.cost }}</p> <!-- Muestra el precio de la ruta -->
          </div>
          <button @click="selectDestination(viaje)">Reservar</button> <!-- Botón para seleccionar -->
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

/* Diseño para perfil y viajes */
.profile-section {
  display: flex;
  justify-content: space-between;
  padding: 20px;
}

.profile-info {
  flex: 1;
  max-width: 300px;
}

.profile-avatar {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #007bff;
  color: white;
  border-radius: 50%;
  width: 80px;
  height: 80px;
  font-size: 24px;
  margin-bottom: 10px;
}

.avatar-initials {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  font-weight: bold;
}

.travel-selection {
  flex: 2;
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
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.destination-card:hover {
  background-color: #eaeaea;
}

.destination-info {
  color: #333;
}

/* Estilos del botón */
button {
  background-color: #007bff;
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 10px 0;
  cursor: pointer;
  border-radius: 5px;
}

button:hover {
  background-color: #0056b3;
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
