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

    .header {
        margin: 0;
        padding: 0;
    }

    .header__nav {
        background-color: black;
        color: white;
        display: flex;
        justify-content: space-between
    }
    
    .header__nav-titulo 
    .nombre {
        text-decoration: none;
        margin-left: 3rem;
        font-size: 4rem;
        height: 5rem;
        color: white;
    }

    .header__nav__enlaces {
        width: 40rem;
        max-width: 100%;
        display: flex;
        justify-content: space-around;
        align-items: center;
    }

    .header__iconos {
        height: 50px;
    }
    .header__descripcion {
        height: 40rem;
        background-image: url("../../public/images/1.jpg");
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

    .user {
        font-size: 4rem;
        background-color: black;
        color: white;
        cursor:pointer;
    }
    .container {
      text-align: center;
      margin-top: 30px;
      margin-bottom: 30px;
    }

    .info-icon{
      font-size: 60px;
    }
   
</style>

