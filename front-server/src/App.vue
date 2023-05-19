<template>
  <div id="app">
    <nav>
      <img src="./assets/N.png" width="50px">
      <router-link :to="{ name: 'HomeView' }" class="mx-1">Home</router-link>
      <router-link :to="{ name: 'SearchView' }">Search</router-link>
      <router-link :to="{ name: 'SignUpView' }" v-show="!islogin" class="mx-1">회원가입</router-link>
      <router-link :to="{ name: 'LoginView' }" v-show="!islogin" class="mx-1">로그인</router-link>
      <router-link :to="{ name: 'HomeView' }" class="mx-1"><span @click.prevent="logout" v-if="islogin">로그아웃</span></router-link>
    </nav>
    <div class="d-flex justify-content-center">
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

</style>
