<template>
  <div id="app">
    <nav>
      <img src="./assets/N.png" width="50px">
      <router-link :to="{ name: 'HomeView' }">Home</router-link> | 
      <router-link :to="{ name: 'SignUpView' }">회원가입</router-link> | 
      <router-link :to="{ name: 'HomeView' }">Search</router-link>
    </nav>
    <div class="d-flex justify-content-center">
      <router-view/>
    </div>
  </div>
</template>

<style>

</style>
