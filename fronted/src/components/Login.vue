<script setup>
import { ref } from 'vue'
import Cabecera from "../Cabecera.vue"
defineProps({
  msg: String,
})

</script>

<template>
  <b-modal v-model="showModal" title="Iniciar sesión">
    <form @submit.prevent="login">
      <input type="email" v-model="email" placeholder="Correo electrónico" required>
      <input type="password" v-model="password" placeholder="Contraseña" required>
      <button type="submit">Iniciar sesión</button>
    </form>
  </b-modal>
</template>

<style scoped>

</style>
