<template>
  <div id="app">
    <nav class="nav navbar navbar-expand-lg fixed-top">
      <div class="container-fluid">
        <router-link :to="{ name: 'HomeView' }">
          <img src="./assets/CGB.png" width="80px">
        </router-link>

        <div style="margin-right:auto; display:flex;">
        <router-link :to="{ name: 'HomeView' }" class="nav-link navfont" :class="{ 'active': $route.name === 'HomeView'}">Home</router-link>
        <router-link :to="{ name: 'review' }" class="nav-link navfont" :class="{ 'active': $route.name === 'review'}">Review</router-link>
        <router-link :to="{ name: 'SearchView' }" class="nav-link navfont" :class="{ 'active': $route.name === 'SearchView'}">Search</router-link>
        </div>

        <div v-if="$route.name !== 'SearchView'" style="display:flex; justify-content: center; align-items:center;">
        <input type="text" v-model="search_movie" class="main_search"
        @keydown.enter="searchMovies" placeholder="검색어를 입력해 주세요.">
        <button @click="searchMovies" class="main_search_button">🔍︎</button>
        </div>

        <div style="margin-left:auto; display:flex;">
        <router-link :to="{ name: 'SignUpView' }" v-show="!islogin" class="nav-link navfont" :class="{ 'active': $route.name === 'SignUpView'}">SignUp</router-link>
        <router-link :to="{ name: 'LoginView' }" v-show="!islogin" class="nav-link navfont" :class="{ 'active': $route.name === 'LoginView'}">LogIn</router-link>
        <router-link :to="{ name: 'HomeView' }" class="nav-link navfont"><span @click.prevent="logout" v-if="islogin">LogOut</span></router-link>
        <router-link v-if="islogin&&user" :to="{ name: 'ProfileView', params: {id : user.id} }"><img :src="`${URL + user.user_img}`" alt="profile" width="50px" style="clip-path: circle(50% at center);" class="mx-2" id="profile"></router-link>
        </div>
      </div>
    </nav>

    <div class="d-flex justify-content-center" style="margin-top: 100px;">
      <router-view/>
    </div>
    <footer style="height: 300px;">
    </footer>
  </div>
</template>
<script>


export default{
  name : 'AppView',
  data(){
    return {
      search_movie:null,
      // user : this.$store.state.user,
      URL : 'http://127.0.0.1:8000'
    }
  },
  computed:{
    islogin(){
      return this.$store.getters.islogin
    },
    user(){
      return this.$store.state.user
    }
  },
  created() {
    this.updateUser()
  },
  methods: {
    logout(){
      this.$store.dispatch('logout')
      alert('로그아웃 되었습니다')
      if (this.$route.path != '/') {
      this.$router.push({name:'HomeView'}); // 중복된 네비게이션을 피하기 위해 네비게이션을 수행하지 않음
      }
    },
    searchMovies() {
      // if (this.$route.path === '/searchlist') {
      // return; // 중복된 네비게이션을 피하기 위해 네비게이션을 수행하지 않음
      // }
      this.$router.push({ name: 'SearchView', params: { word: this.search_movie } });
      this.search_movie = null
    },
    updateUser() {
      this.user = this.$store.state.user
    },
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
#profile{
  width: 50px;
  height: 50px;
  clip-path: circle(50%); /* 가로 길이를 반지름으로 사용 */
}
</style>