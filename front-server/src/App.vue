<template>
  <div id="app">
    <nav class="nav navbar navbar-expand-lg">
      <div class="container-fluid">
          <router-link :to="{ name: 'HomeView' }">
            <img src="./assets/N.png" width="40px">
          </router-link>
          <router-link :to="{ name: 'HomeView' }" class="nav-link navfont" :class="{ 'active': $route.name === 'HomeView'}">Home</router-link>
          <router-link :to="{ name: 'review' }" class="nav-link navfont" :class="{ 'active': $route.name === 'review'}">review</router-link>
          <router-link :to="{ name: 'SearchView' }" class="nav-link navfont" :class="{ 'active': $route.name === 'SearchView'}">Search</router-link>
          <router-link :to="{ name: 'SignUpView' }" v-show="!islogin" class="nav-link navfont" :class="{ 'active': $route.name === 'SignUpView'}">SignUp</router-link>
          <router-link :to="{ name: 'LoginView' }" v-show="!islogin" class="nav-link navfont" :class="{ 'active': $route.name === 'LoginView'}">LogIn</router-link>
          <router-link :to="{ name: 'HomeView' }" class="nav-link navfont"><span @click.prevent="logout" v-if="islogin">LogOut</span></router-link>
      </div>
    </nav>

    <div class="d-flex justify-content-center m-5">
      <router-view/>
    </div>
  </div>
</template>
<script>
// import axios from "axios"

export default{
  name : 'AppView',
  computed:{
    islogin(){
      return this.$store.getters.islogin
    }
  },
  created() {
  },
  methods: {
    logout(){
      this.$store.dispatch('logout')
    }
  },
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Carter+One&family=Hahmlet:wght@200;300;400;500;600;700&family=Noto+Serif+KR:wght@200;500;900&display=swap');

body {
  font-family: 'Hahmlet', serif;
  background-color : black;
  color : white;
}

.nav {
  background-color: #ede5d7;
}

.navfont {
  color : black;
  font-family: 'Carter One', cursive;
  font-weight : bold;
  font-size : 25px;
}

.nav-link.active {
  color: #ba1b10;
}


</style>