<template>
    <footer class="footer">
      <div class="footer__content">
        <h2 class="footer__title">AQPTransporte</h2>
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
      </div>
    </footer>
  </template>
  
  <style scoped>
  .footer {
    background-color: #333;
    color: white;
    padding: 20px;
    text-align: center;
  }
  
  .footer__title {
    font-size: 2rem;
    margin-bottom: 20px;
  }
  
  .contacto__contenido {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .contacto__item {
    margin: 10px 0;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .contacto__item span {
    font-size: 24px; /* Tamaño de los íconos */
    margin-right: 10px;
  }
  
  .contacto__item p {
    margin: 0; /* Elimina el margen predeterminado de los párrafos */
    font-size: 16px;
  }
  </style>