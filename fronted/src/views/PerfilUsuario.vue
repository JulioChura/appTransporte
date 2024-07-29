<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import Header from '../components/Header.vue';
import Footer from '../components/Footer.vue'; 
import { getCurrentUser } from '../services/authService';
import Voucher from '../components/Voucher.vue';

const nombreUsuario = ref('');
const apellidoUsuario = ref('');
const dni = ref('');
const celular = ref('');
const correo = ref('');
const vouchers = ref([]);
const showModal = ref(false);
const selectedVoucher = ref(null);
const storedUser = ref(null);

const getInitials = (firstName, lastName) => {
  if (!firstName || !lastName) return '';
  return firstName.charAt(0) + lastName.charAt(0);
};

const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(dateString).toLocaleDateString(undefined, options);
};

onMounted(async () => {
  try {
    const currentUser = getCurrentUser();
    if (currentUser) {
      const userData = currentUser.cliente;
      nombreUsuario.value = userData.Name;
      apellidoUsuario.value = userData.LastName;
      dni.value = userData.DNI;
      celular.value = userData.Cellphone;
      correo.value = userData.email;

      storedUser.value = currentUser; // Inicializar storedUser aquí

      const vouchersResponse = await axios.get(`http://localhost:8000/api/clientes/${userData.id}/historial/`);
      vouchers.value = vouchersResponse.data.vouchers;
    }
  } catch (error) {
    console.error('Error fetching user data or vouchers:', error);
  }
});

const showVoucher = (voucher) => {
  selectedVoucher.value = voucher;
  showModal.value = true;
};

// Función para cerrar el modal
const closeModal = () => {
  showModal.value = false;
  selectedVoucher.value = null;
};
</script>

<template>
  <div class="container">
    <Header />
    <div class="perfil-contenedor">
      <div class="perfil-izquierda">
        <div class="perfil-info">
          <div class="profile-avatar">
            <span class="avatar-initials">{{ getInitials(nombreUsuario, apellidoUsuario) }}</span>
          </div>
          <h2>Hola, {{ nombreUsuario }}</h2>
          <p><strong>DNI:</strong> {{ dni }}</p>
          <p><strong>Celular:</strong> {{ celular }}</p>
          <p><strong>Correo:</strong> {{ correo }}</p>
        </div>
      </div>

      <div class="perfil-derecha">
        <h2>Mis viajes</h2>
        <div class="travel-selection">
          <div 
            v-for="voucher in vouchers" 
            :key="voucher.id" 
            class="destination-card"
          >
            <div class="destination-info">
              <h3>{{ voucher.ruta.startingPlace }} - {{ voucher.ruta.destinationPlace }}</h3>
              <p><strong>Distancia:</strong> {{ voucher.ruta.distance }} km</p>
              <p><strong>Paradas:</strong> {{ voucher.ruta.stops }}</p>
              <p><strong>Horario:</strong> {{ voucher.ruta.horario }}</p>
              <p><strong>Fecha:</strong> {{ formatDate(voucher.ruta.fecha) }}</p>
              <p><strong>Costo:</strong> ${{ voucher.cost }}</p>
              <p><strong>Creado:</strong> {{ formatDate(voucher.created_at) }}</p>
            </div>
            <button @click="showVoucher(voucher)" type="button">Mostrar Recibo</button>
          </div>
        </div>
      </div>
    </div>
    <Footer /> 
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <Voucher v-if="storedUser && storedUser.cliente" :voucher="selectedVoucher" :user="storedUser.cliente" />
      </div>
    </div>
  </div>
</template>


<style scoped>
.container {
  font-family: 'Arial', sans-serif;
  color: #333;
}

.perfil-contenedor {
  display: flex;
  padding: 20px;
  background-color: #f0f0f0;
  min-height: calc(100vh - 60px); /* Altura mínima restando la altura del header */
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

.perfil-info {
  text-align: center;
}

.profile-avatar {
  width: 80px;
  height: 80px;
  background-color: #0063d4;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  margin: 0 auto 10px;
}

.avatar-initials {
  font-size: 2rem;
  font-weight: bold;
}

h2 {
  margin-top: 0;
  color: #333;
}

p {
  margin: 10px 0;
}

.travel-selection {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.destination-card {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  transition: background-color 0.3s, box-shadow 0.3s;
}

.destination-card:hover {
  background-color: #eaeaea;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.destination-info {
  text-align: left;
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

  overflow: auto;
  background-color: rgba(0,0,0,0.4);
}

.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 40%;
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