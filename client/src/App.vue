<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@100;400;600&display=swap');

#app {
  background-color:  #C6D2E3;
  background-image: linear-gradient(180deg, #D6E0FC 0%, #EAF2F8 50.35%, #FEF9E7);
  font-family: 'Poppins', sans-serif;
  right: 0;
  bottom: 0;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  z-index: -100;
}
</style>
