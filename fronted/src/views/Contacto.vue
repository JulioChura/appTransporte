<script setup>
import FooterVue from '../components/Footer.vue';
import Header from '../components/Header.vue';
</script>

<template>
  <Header />
  <h3 class="titulo">Nos pondremos en contacto contigo</h3>
  
  <div class="container">
    <div class="contact-form">
      <h2>Contacto</h2>
      <form action="mailto:jchuraaca@unsa.edu.pe" method="post" enctype="text/plain">
        <div class="form-group">
          <label for="name">Nombre:</label>
          <input type="text" id="name" name="name" required>
        </div>
        <div class="form-group">
          <label for="email">Correo Electrónico:</label>
          <input type="email" id="email" name="email" required>
        </div>
        <div class="form-group">
          <label for="message">Mensaje:</label>
          <textarea id="message" name="message" rows="4" required></textarea>
        </div>
        <div class="form-group">
          <button type="submit">Enviar</button>
        </div>
      </form>
    </div>
  </div>

  <FooterVue />
</template>

<style scoped>
body {
  font-family: 'Arial', sans-serif;
  background-color: #f0f2f5;
  margin: 0;
  padding: 0;
  color: #333;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 60px);
  padding: 2rem;
}

.contact-form {
  background-color: #ffffff;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
  max-width: 500px;
  width: 100%;
}

.contact-form h2 {
  margin-top: 0;
  margin-bottom: 1.5rem;
  font-size: 2rem;
  color: #2c3e50;
  text-align: center;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: #34495e;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #3498db;
  box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
}

.form-group textarea {
  resize: vertical;
  min-height: 100px;
}

.form-group button {
  background-color: #3498db;
  color: #ffffff;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: background-color 0.3s ease;
  width: 100%;
}

.form-group button:hover {
  background-color: #2980b9;
}

.titulo {
  text-align: center;
  margin: 3rem 0;
  color: #2c3e50;
  font-size: 2rem;
  font-weight: 700;
}

@media (max-width: 768px) {
  .container {
    padding: 1rem;
  }
  
  .contact-form {
    padding: 1.5rem;
  }
}
</style>
