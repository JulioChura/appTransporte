<template>
    <header class="header">
        <!-- Barra de nav donde estan los iconos de sobreNosotros, Login, Contacto -->
        <div class="header__nav">
            <h1 class="header__nav-titulo">
                <router-link to="/" class="nombre">AQPTransporte</router-link>
            </h1>
            <div class="header__nav__enlaces">

                <router-link :to="{ name: 'SobreNosotros' }" class="nombre"><span
                        class="material-symbols-outlined icons call">info</span></router-link>
                <router-link :to="{ name: 'contacto' }"> <span
                        class="material-symbols-outlined icons">call</span></router-link>

                <span class="material-symbols-outlined icons" @click="mostrarModalLogin">
                        account_circle
                </span>
            </div>
        </div>
        <!-- Aqui comienza lo de la img de fondo y el mensaje de la empresa -->
        <div class="header__descripcion">
            <div class="header__descripcion-texto">
                <h1 class="header__descripcion-titulo">"Conectamos destinos, unimos caminos"</h1>
                <p class="header__descripcion-mensaje">
                    Nos dedicamos a proporcionar soluciones de transporte seguras, eficientes y confiables para cada uno
                    de nuestros clientes
                </p>
            </div>
        </div>
        <!-- Los modal tanto para el login como para el registro -->
        <LoginCliente :isVisible="showModalLogin" @cerrarModal="cerrarModalLogin"
            @mostrarRegister="mostrarModalRegister" />
        <RegisterCliente :isVisible="showModalRegister" @cerrarModal="cerrarModalRegister" />
    </header>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import LoginCliente from "../components/LoginCliente.vue";
import RegisterCliente from "../components/RegisterCliente.vue";

const router = useRouter();
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

// falta implementar la logica para borrar las credenciales del inicio de sesion
const cerrarSesion = () => {
    logout(); // Actualizar el estado de autenticación global
    router.push('/'); // Redirigir al inicio
};


</script>

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

.header__nav-titulo .nombre {
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

.icons {
    color: white;
    font-size: 4rem;
    background-color: black;

    cursor: pointer;

}

.container {
    text-align: center;
    margin-top: 30px;
    margin-bottom: 30px;
}

.info-icon {
    font-size: 60px;
}
</style>