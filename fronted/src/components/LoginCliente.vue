<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

// Props y emits
const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  }
});
const emit = defineEmits(['cerrarModal', 'mostrarRegister']);

// Estado reactivo
const email = ref('');
const password = ref('');
const error = ref('');
const message = ref('');
const userLoggedIn = ref(false);

// Configuración del router
const router = useRouter();

// Función para cerrar el modal
const closeModal = () => {
  emit('cerrarModal');
};

// Función para enviar datos
const loginUser = async () => {
  try {
    // Envía una solicitud POST al backend con email y password
    const response = await axios.post('/api/login', {
      email: email.value,
      password: password.value
    });

    // Procesa la respuesta
    const { name } = response.data;
    userLoggedIn.value = true; // Marca al usuario como autenticado
    message.value = 'Login successful!';
    error.value = '';
    // Redirigir a la página de viajes con el nombre de usuario
    router.push({ name: 'SeleccionDestino', params: { username: name } });
  } catch (err) {
    error.value = 'Login failed: ' + (err.response ? err.response.data.error : err.message);
    message.value = '';
  }
};

// Función para mostrar el formulario de registro
const mostrarRegister = () => {
  emit('mostrarRegister');
  closeModal();
};
</script>

<template>
  <div class="modal" v-if="isVisible">
    <div class="modal-content">
      <span class="close" @click="closeModal">&times;</span>
      <h2>Login</h2>
      
      <form @submit.prevent="loginUser">
        <div class="form-group">
          <label for="exampleInputEmail1">Email address</label>
          <input v-model="email" type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
          <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
        </div>
        <div class="form-group">
          <label for="exampleInputPassword1">Password</label>
          <input v-model="password" type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
        </div>
        <div class="form-check">
          <input type="checkbox" class="form-check-input" id="exampleCheck1">
          <label class="form-check-label" for="exampleCheck1">Check me out</label>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
      <p v-if="message">{{ message }}</p>
      <p v-if="error" class="text-danger">{{ error }}</p>
      <p>¿No tienes una cuenta? <a href="#" @click="mostrarRegister">Regístrate aquí</a></p>
    </div>
  </div>
</template>

<style scoped>
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
  background-color: rgb(0,0,0);
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

.form-group {
  margin-bottom: 1rem;
}

.form-control {
  width: 100%;
  padding: 0.5rem;
  margin-top: 0.5rem;
}

.form-text {
  font-size: 0.875rem;
  color: #6c757d;
}

.text-danger {
  color: #dc3545;
}
</style>