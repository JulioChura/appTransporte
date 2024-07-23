 <script setup>
  import { ref } from 'vue'
  import Cabecera from '../components/Cabecera.vue';
  
  </script>
  
  <template>
  <Cabecera/>
  
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
  .container {
    margin: 0 auto;
    margin-top: 30px;
  }
  </style>
  