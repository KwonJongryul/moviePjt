<template>
  <div id="app">
    <nav class="nav navbar navbar-expand-lg fixed-top">
      <div class="container-fluid">
        <router-link :to="{ name: 'HomeView' }">
          <img src="./assets/N.png" width="40px">
        </router-link>

        <div style="margin-right:auto; display:flex;">
        <router-link :to="{ name: 'HomeView' }" class="nav-link navfont" :class="{ 'active': $route.name === 'HomeView'}">Home</router-link>
        <router-link :to="{ name: 'review' }" class="nav-link navfont" :class="{ 'active': $route.name === 'review'}">Review</router-link>
        <router-link :to="{ name: 'SearchView' }" class="nav-link navfont" :class="{ 'active': $route.name === 'SearchView'}">Search</router-link>
        </div>

        <div style="display:flex; justify-content: center; align-items:center;">
        <input type="text" v-model="search_movie" class="main_search"
        @keydown.enter="searchMovies" placeholder="검색어를 입력하세요.">
        <button @click="searchMovies" class="main_search_button">🔍︎</button>
        </div>

        <div style="margin-left:auto; display:flex;">
        <router-link :to="{ name: 'SignUpView' }" v-show="!islogin" class="nav-link navfont" :class="{ 'active': $route.name === 'SignUpView'}">SignUp</router-link>
        <router-link :to="{ name: 'LoginView' }" v-show="!islogin" class="nav-link navfont" :class="{ 'active': $route.name === 'LoginView'}">LogIn</router-link>
        <router-link :to="{ name: 'HomeView' }" class="nav-link navfont"><span @click.prevent="logout" v-if="islogin">LogOut</span></router-link>
        </div>
      </div>
    </nav>

    <div class="d-flex justify-content-center" style="margin-top: 100px;">
      <router-view/>
    </div>
  </div>
</template>
<script>
// import axios from "axios"

export default{
  name : 'AppView',
  data(){
    return {
      search_movie:null
    }
  },
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
    },
    searchMovies() {
      // if (this.$route.path === '/searchlist') {
      // return; // 중복된 네비게이션을 피하기 위해 네비게이션을 수행하지 않음
      // }
      this.$router.push({ name: 'SearchView', query: { search: this.search_movie } });
      this.search_movie = null
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

.main_search {
    padding: 20px;
    border : white;
    border-radius: 50px;
    width: 500px;
    height: 30px;
    font-size: 20px;
    background-color: white;
    color: black;
    outline: none;
    box-shadow: 3px 3px 3px rgb(180, 180, 180);
}

.main_search_button {
    background-color: transparent;
    border: none;
    cursor: pointer;
    color: black;
    font-size: 30px;
    background-color: transparent;
    margin-left: 10px;
    text-decoration: none;
  }
</style>