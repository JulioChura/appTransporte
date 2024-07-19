<script setup>
import { defineProps, defineEmits } from 'vue';
import axios from 'axios';

import { login, setToken } from '../services/authService';
import { ref } from 'vue';

export default {
  setup() {
    const email = ref('');
    const password = ref('');
    const error = ref('');
    const message = ref('');

    const loginUser = async () => {
      try {
        const response = await login(email.value, password.value);
        setToken(response.data.token); // Guarda el token en localStorage
        message.value = 'Login successful!';
        error.value = '';
        // Redirige a la página de inicio o a donde prefieras
        // router.push('/'); // Necesitas importar y usar el router
      } catch (err) {
        error.value = 'Login failed: ' + (err.response ? err.response.data.error : err.message);
        message.value = '';
      }
    };

    return {
      email,
      password,
      error,
      message,
      login: loginUser
    };
  }
};

const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  }
});

const emit = defineEmits(['cerrarModal']);

const closeModal = () => {
  emit('cerrarModal');
};
</script>

<template>
  <div class="modal" v-if="isVisible">
    <div class="modal-content">
      <span class="close" @click="closeModal">&times;</span>
      <h2>Login</h2>
      
      <form @submit.prevent="login">
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
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  background-color: #fefefe;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  max-width: 500px;
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
