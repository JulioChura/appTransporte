<script setup>
import { ref, onMounted, reactive, provide } from 'vue';
import axios from 'axios';
import Voucher from '../components/Voucher.vue'; 
import Footer from '../components/Footer.vue'; 
import MercadoPago from '../components/MercadoPago.vue';
import Header from '../components/Header.vue';
const username = ref(''); // Se obtiene el nombre de usuario de la ruta o de alguna otra manera
const user = ref(null); // Datos del usuario
const viajes = ref([]);
const message = ref('');
const showModal = ref(false); // Estado para mostrar el modal

const userData = reactive({
  cliente_id: null,
  ruta_id: null,
  cost: null,
  origen: null,
  destino: null
});

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
const showPay = (viaje) => {
  const userId = user.value?.id; // Recupera el id del usuario

  if (!userId) {
    console.error('User ID not found');
    return;
  }
  userData.cliente_id = userId;
  userData.ruta_id = viaje.id;
  userData.cost = viaje.cost;
  userData.origen = viaje.startingPlace;
  userData.destino = viaje.destinationPlace;
  
  showModal.value = true; // Muestra el modal
};

// Función para cerrar el modal
const closeModal = () => {
  showModal.value = false; // Cierra el modal
};

// Proveer datos del usuario para otros componentes
provide('userData', userData);

// Función para obtener las iniciales del nombre del cliente
const getInitials = (firstName, lastName) => {
  if (!firstName || !lastName) return '';
  return firstName.charAt(0) + lastName.charAt(0);
};
</script>



<template>
  
    <Header /> 

    <div class="perfil-contenedor">
      <div class="perfil-izquierda">
        <div class="profile-avatar">
          <span class="avatar-initials">{{ getInitials(user?.Name, user?.LastName) }}</span> <!-- Muestra las iniciales del nombre del cliente -->
        </div>
        <h2>Bienvenido, {{ username }}</h2>
        <p>Correo: {{ user?.email }}</p>
        <p>Teléfono: {{ user?.Cellphone }}</p>
        <p>DNI: {{ user?.DNI }}</p> <!-- Datos adicionales del cliente -->
        <!-- Botón para redirigir a PerfilUsuario.vue -->
        <router-link to="/perfil">
          <button class="btn-perfil">Ver historial de viajes</button>        </router-link>
      </div>

      <div class="travel-selection">
        <h1>Selecciona tu destino de viaje</h1>
        <div class="destinations">
          <div v-for="viaje in viajes" :key="viaje.id" class=" perfil-derecha">
            <div class="destination-info">
              <h2>{{ viaje.startingPlace }} - {{ viaje.destinationPlace }}</h2>
              <p>Distancia: {{ viaje.distance }} km</p>
              <p>Paradas: {{ viaje.stops }}</p>
              <p>Horario: {{ viaje.horario }}</p>
              <p>Fecha: {{ viaje.fecha }}</p>
              <p>Precio: S/{{ viaje.cost }}</p> <!-- Muestra el precio de la ruta -->
            </div>

            <button @click="showPay(viaje)" class="btn-viaje">Comprar</button> <!-- Botón para seleccionar -->
          </div>
        </div>

        <!-- Modal para mostrar los datos del voucher -->
        <div v-if="showModal" class="modal">
          <div class="modal-content">
            <span class="close" @click="closeModal">&times;</span>
            
            <MercadoPago :message="message" />

          </div>
        </div>
      </div>
    </div>
    
    <Footer />
</template>

<style scoped>
/* Estilo general de la página */
.page-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}



/* Diseño para perfil y viajes */
.profile-section {
  flex: 1;
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
.btn-perfil {
  background-color: #000; /* Negro */
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
  flex-direction: column;


  align-items: center;
}

.btn-perfil:hover {
  background-color: #333; /* Gris oscuro al pasar el cursor */
}

/* Estilo para el botón de viaje */
.btn-viaje {
  background-color: #28a745; /* Verde */
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

.btn-viaje:hover {
  background-color: #218838; /* Verde más oscuro al pasar el cursor */
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

/* Estilo del Footer */
footer {
  margin-top: auto;
}

.perfil-contenedor {
  margin: 30px;
  display: flex;
  padding: 20px;
  background-color: #f0f0f0;
  min-height: calc(100vh - 60px); 
}

.perfil-contenedor {
  display: flex;
  padding: 20px;
  background-color: #f0f0f0;
  min-height: calc(100vh - 60px); 
}

.perfil-izquierda {
  flex: 1;
  margin-right: 20px;
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.perfil-derecha {
  flex: 2;
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>