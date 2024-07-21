<script setup>
  import { ref } from 'vue';
  import LoginCliente from "../components/LoginCliente.vue";
  import RegisterCliente from "../components/RegisterCliente.vue";
  
  const showModalLogin = ref(false);
  const showModalRegister = ref(false);
  
  const mostrarModalLogin = () => {
    showModalLogin.value = true;
  };

  const mostrarModalRegister = () => {
    showModalRegister.value = true;
  };
  
  const cerrarModalLogin = () => {
    showModalLogin.value = false;
  };

  const cerrarModalRegister = () => {
    showModalRegister.value = false;
  };
</script>

<template>
  <header class="header">
    <div class="header__nav">
      <h1 class="header__nav-titulo">
        <a href="#" class="nombre">AQPTransporte</a>
      </h1>
      <div class="header__nav__enlaces">
        <a href="#">
          <span class="material-symbols-outlined user" @click="mostrarModalLogin">
            account_circle
          </span>
        </a>
      </div>
    </div>

    <div class="header__descripcion">
      <div class="header__descripcion-texto">
        <h1 class="header__descripcion-titulo">"Conectamos destinos, unimos caminos"</h1>
        <p class="header__descripcion-mensaje">
          Nos dedicamos a proporcionar soluciones de transporte seguras, eficientes y confiables para cada uno de nuestros clientes
        </p>
      </div>
    </div>
  </header>

  <LoginCliente :isVisible="showModalLogin" @cerrarModal="cerrarModalLogin" @mostrarRegister="mostrarModalRegister" />
  <RegisterCliente :isVisible="showModalRegister" @cerrarModal="cerrarModalRegister" />

  <!-- Sección de Contacto -->
  <section class="contacto">
    <div class="contacto__contenido">
      <h2>Contáctanos</h2>
      <div class="contacto__item">
        <span class="material-symbols-outlined">location_on</span>
        <p>Av. Independencia, Arequipa, Perú</p>
      </div>
      <div class="contacto__item">
        <span class="material-symbols-outlined">phone</span>
        <p>(+51) 958 745 962</p>
      </div>
      <div class="contacto__item">
        <span class="material-symbols-outlined">email</span>
        <p>contacto@aqptransporte.com</p>
      </div>
    </div>
  </section>
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
        color: white
    }

    /* Sección de contacto */
    .contacto {
      padding: 2rem;
      background-color: #f9f9f9;
      text-align: center;
    }

    .contacto__contenido {
      max-width: 800px;
      margin: 0 auto;
    }

    .contacto__item {
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-bottom: 1rem;
    }

    .contacto__item span {
      font-size: 2rem;
      color: #007bff;
    }

    .contacto__item p {
      font-size: 1.2rem;
      margin: 0;
    }

</style>
