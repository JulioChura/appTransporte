<script setup>
import FooterVue from '../components/Footer.vue';
import Header from '../components/Header.vue';

</script>

<template>
  <div>
    <Header />

    <!-- Aqui poner tgextoe imagenes referenciales -->
    <div class="container">
      Somos una empresa de transporte líder en Arequipa, comprometida con brindar soluciones de movilidad seguras, 
      eficientes y puntuales. Con una flota moderna y un equipo de profesionales capacitados, ofrecemos servicios de 
      transporte de carga y pasajeros a nivel local y nacional. Nuestro objetivo es satisfacer las necesidades de nuestros clientes,
      garantizando la integridad de sus bienes y la comodidad en sus viajes. Innovamos continuamente para ofrecer 
      la mejor experiencia en transporte, apoyándonos en tecnología avanzada y prácticas sostenibles. Confiabilidad, 
      responsabilidad y compromiso son los valores que nos distinguen en el mercado arequipeño.
    </div>
  </div>

  <FooterVue />
</template>


<style scoped>
.container {
  margin: 0 auto;
  font-size: 30px;
}
</style>
