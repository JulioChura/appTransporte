<script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  
  // Props y emits
  const props = defineProps({
    isVisible: {
      type: Boolean,
      default: false
    }
  });
  const emit = defineEmits(['cerrarModal']);
  
  // Estado reactivo
  const name = ref('');
  const lastName = ref('');
  const dni = ref('');
  const cellphone = ref('');
  const email = ref('');
  const password = ref('');
  const error = ref('');
  const message = ref('');
  
  // Función para cerrar el modal
  const closeModal = () => {
    emit('cerrarModal');
  };
  
  // Función para enviar datos
  const registerUser = async () => {
    try {
      // Envía una solicitud POST al backend con los datos 
      const response = await axios.post('http://localhost:8000/api/register/', {
        email: email.value,
        password: password.value,
        Name: name.value,
        LastName: lastName.value,
        DNI: dni.value,
        Cellphone: cellphone.value,
        id_company: 1
        
      });
  
      // Procesa la respuesta
      message.value = 'Registration successful!';
      error.value = '';
      // Se puede redirigir a login o realiza otras acciones
      // router.push('/login'); // importar y usar el router para redirigir
    } catch (err) {
      error.value = 'Registration failed: ' + (err.response ? err.response.data.error : err.message);
      message.value = '';
    }
  };
</script>

<template>
    <div class="modal" v-if="isVisible">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <h2>Register</h2>
        
        <form @submit.prevent="registerUser">
          <div class="form-group">
            <label for="name">Name</label>
            <input v-model="name" type="text" class="form-control" id="name" placeholder="Enter name">
          </div>
          <div class="form-group">
            <label for="lastName">Last Name</label>
            <input v-model="lastName" type="text" class="form-control" id="lastName" placeholder="Enter last name">
          </div>
          <div class="form-group">
            <label for="dni">DNI</label>
            <input v-model="dni" type="text" class="form-control" id="dni" placeholder="Enter DNI">
          </div>
          <div class="form-group">
            <label for="cellphone">Cellphone</label>
            <input v-model="cellphone" type="text" class="form-control" id="cellphone" placeholder="Enter cellphone number">
          </div>
          <div class="form-group">
            <label for="email">Email address</label>
            <input v-model="email" type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Enter email">
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input v-model="password" type="password" class="form-control" id="password" placeholder="Password">
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
        <p v-if="message">{{ message }}</p>
        <p v-if="error" class="text-danger">{{ error }}</p>
      </div>
    </div>
  </template>
  
  <style scoped>
  /* Estilos para el modal */
  .modal {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
  }
  
  .modal-content {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    width: 80%;
    max-width: 500px;
  }
  
  .close {
    position: absolute;
    top: 10px;
    right: 10px;
    cursor: pointer;
    font-size: 24px;
  }
  </style>