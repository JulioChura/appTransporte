<script setup>
</script>

<template>
    <header class="header">
        <div class="header__nav">
            <h1 class="header__nav-titulo"><a href="#" class="nombre">ViajesAQP</a></h1>
            <div class="header__nav__enlaces">
            </div>
        </div>

    </header>
</template>

<style scoped>
.header {
    margin: 0;
    padding: 0;
    width: 100%;
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

  
</style>
