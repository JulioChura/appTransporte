<template>
    <div class="por-que-elegirnos">
      <h2>¿Por qué elegirnos?</h2>
      <div class="razones">
        <div class="razon" v-for="(razon, index) in razones" :key="index">
            <span class="material-symbols-outlined"> {{ razon.icono }}  </span>
          <h3>{{ razon.titulo }}</h3>
          <p>{{ razon.descripcion }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'PorQueElegirnos',
    data() {
      return {
        razones: [
        {
          icono: "timer",
          titulo: 'Puntualidad',
          descripcion: 'Garantizamos llegadas y salidas a tiempo para que llegues a tu destino sin retrasos.'
        },
        {
          icono: 'verified_user',
          titulo: 'Seguridad',
          descripcion: 'Contamos con un sistema de seguridad avanzado para proteger a nuestros pasajeros y sus pertenencias.'
        },
        {
          icono: 'full_coverage',
          titulo: 'Cobertura Amplia',
          descripcion: 'Ofrecemos rutas que cubren una amplia gama de destinos para tu conveniencia.'
        },
        {
          icono: 'directions_bus',
          titulo: 'Tecnología Avanzada',
          descripcion: 'Nuestros vehículos están equipados con la última tecnología para un viaje cómodo y seguro.'
        }
      ]
      };
    }
  };
  </script>
  
  <style scoped>
  .por-que-elegirnos {
    text-align: center;
    padding: 2rem;
    background-color: #f9f9f9;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .por-que-elegirnos h2 {
    font-size: 2rem;
    margin-bottom: 1.5rem;
    color: #333;
  }
  
  .razones {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    gap: 1.5rem;
  }
  
  .razon {
    flex: 1 1 calc(25% - 1rem);
    background-color: white;
    padding: 1rem;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
  }
  
  .razon:hover {
    transform: translateY(-10px);
  }
  
  .icono {
    width: 50px;
    height: 50px;
    margin-bottom: 1rem;
  }
  
  .razon h3 {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
    color: #333;
  }
  
  .razon p {
    font-size: 1rem;
    color: #666;
  }
  .material-symbols-outlined {
    font-size: 60px;
  }

</style>
  