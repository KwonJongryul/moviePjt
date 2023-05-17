<template>
  <div id="app">
    <nav>
      <img src="./assets/N.png" width="50px">
      <router-link :to="{ name: 'HomeView' }">Home</router-link> | 
      <router-link :to="{ name: 'HomeView' }">Rivew</router-link> | 
      <router-link :to="{ name: 'HomeView' }">Search</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>

</style>
