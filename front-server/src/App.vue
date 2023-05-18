<template>
  <div id="app">
    <nav>
      <img src="./assets/N.png" width="50px">
      <router-link :to="{ name: 'HomeView' }" replace>Home</router-link> | 
      <router-link :to="{ name: 'SignUpView' }" v-show="!islogin">회원가입</router-link> | 
      <router-link :to="{ name: 'LoginView' }" v-show="!islogin">로그인</router-link>
      <a @click.prevent="logout"  replace>로그아웃</a>
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
      // axios({
      //   method: 'post',
      //   url : 'http://127.0.0.1:8000/accounts/logout/',
      // })
      // .then(()=>{
      //   localStorage.removeItem('authToken')
      //   console.log(this.$store.getters.islogin)
      //   this.$router.push({name:'HomeView'})
      // })
      // .catch((err) => {
      //   console.log(err)
      // })
      this.$router.push({name:'HomeView'})
    }
  },
}
</script>
<style>

</style>
