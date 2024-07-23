<template>
    <div class="carrusel">
      <div class="carrusel-imagenes" :style="{ transform: `translateX(-${indiceActual * 100}%)` }">
        <div
          v-for="(imagen, index) in imagenes"
          :key="index"
          class="carrusel-imagen"
        >
          <img :src="imagen" alt="" />
        </div>
      </div>
    </div>
</template>
  
<script>
  import { ref, onMounted, onBeforeUnmount } from 'vue';
  
  export default {
    setup() {
      const indiceActual = ref(0);
      const imagenes = ref([
        '../../public/carrusel/1.jpg',
        '../../public/carrusel/2.jpg',
        '../../public/carrusel/3.jpg',
        '../../public/carrusel/4.jpg',
        '../../public/carrusel/5.jpg',
        '../../public/carrusel/6.jpg',
        '../../public/carrusel/7.jpg',
        '../../public/carrusel/8.jpg',
        '../../public/carrusel/9.jpg',
      ]);
  
      const siguiente = () => {
        indiceActual.value = (indiceActual.value + 1) % imagenes.value.length;
      };
  
      let intervalId = null;
  
      onMounted(() => {
        intervalId = setInterval(siguiente, 2000);
      });
  
      onBeforeUnmount(() => {
        clearInterval(intervalId);
      });
  
      return {
        indiceActual,
        imagenes,
      };
    },
  };
</script>
  
<style scoped>
.carrusel {
  width: 100%;
  max-width: 100%;
  height: 600px; 
  overflow: hidden;
  position: relative;
  margin: 0 auto;
  border-radius: 10px;
}

.carrusel-imagenes {
  display: flex;
  transition: transform 0.5s ease;
}

.carrusel-imagen {
  min-width: 100%;
  height: 100%; 
  box-sizing: border-box;
  overflow: hidden;
}

.carrusel-imagen img {
  width: 100%;
  height: 100%;
  object-position: center;
}
</style>