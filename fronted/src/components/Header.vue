<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import LoginCliente from "../components/LoginCliente.vue";
import RegisterCliente from "../components/RegisterCliente.vue";
import { getCurrentUser, logout } from '../services/authService';

const router = useRouter();
const showModalLogin = ref(false);
const showModalRegister = ref(false);
const user = ref(null);

onMounted(() => {
  user.value = getCurrentUser();
});

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

const cerrarSesion = () => {
    logout();
    user.value = null;
    router.push('/');
};
</script>

<template>
    <header class="header">
        <div class="header__nav">
            <h1 class="header__nav-titulo">
                <router-link to="/" class="nombre">AQPTransporte</router-link>
            </h1>
            <div class="header__nav__enlaces">
                <!-- <router-link :to="{ name: 'SeleccionDestino' }" class="nav-button">Seleccionar Destino</router-link>
                <router-link :to="{ name: 'PerfilUsuario' }" class="nav-button">Perfil Usuario</router-link> -->
                <router-link :to="{ name: 'SobreNosotros' }" class="nombre"><span
                        class="material-symbols-outlined icons call">info</span></router-link>
                <router-link :to="{ name: 'contacto' }"> <span
                        class="material-symbols-outlined icons">call</span></router-link>

                <span v-if="!user" class="material-symbols-outlined icons" @click="mostrarModalLogin">
                    account_circle
                </span>
                <div v-else class="user-info">
                    
                    <router-link :to="{ name: 'PerfilUsuario', params: { id: user.cliente.id } }" class="usuario-link">
                        <span class="usuario-name">{{ user.cliente.Name }}</span>
                    </router-link>

                    <button @click="cerrarSesion" class="cerrar">Cerrar sesión</button>
                </div>
            </div>
        </div>
        <div class="header__descripcion">
            <div class="header__descripcion-texto">
                <h1 class="header__descripcion-titulo">"Conectamos destinos, unimos caminos"</h1>
                <p class="header__descripcion-mensaje">
                    Nos dedicamos a proporcionar soluciones de transporte seguras, eficientes y confiables para cada uno
                    de nuestros clientes
                </p>
            </div>
        </div>
        <LoginCliente :isVisible="showModalLogin" @cerrarModal="cerrarModalLogin"
            @mostrarRegister="mostrarModalRegister" />
        <RegisterCliente :isVisible="showModalRegister" @cerrarModal="cerrarModalRegister" />
    </header>
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

.cerrar {
    margin-left: 10px;
    margin-right: 10px; 
    background-color: transparent;
    border: 1px solid white;
    color: white;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
}

.usuario-link {
    text-decoration: none;
    color: white;
    font-size: 20px;
    margin-right: 10px;
}

.usuario-name {
    font-size: 20px;
    font-weight: bold;
}

</style>
