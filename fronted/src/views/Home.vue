<script setup>
import { ref } from 'vue';
import Carrusel from '../components/Carrusel.vue';
import Valores from '../components/Valores.vue';
import Header from '../components/Header.vue';
import FooterVue from '../components/Footer.vue';

</script>

<template>
  <Header />
  <hr>
  <div class="container">
    <h2>¡Visita los lugares más fascinantes del Perú!</h2>
    <Carrusel />
  </div>
  <div class="container">
    <Valores />
  </div>
  <FooterVue />  
</template>
  
  
<style scoped>
   
</style>

