<template>
  <div>
    <h1>홈화면</h1>
    <p v-for="movie in movies" :key="movie">{{ movie.title }}</p>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data(){
    return {
      // movies : []
    }
  },
  computed : {
    movies(){
      const ms = this.$store.state.movies
      // for(let i = 0; i < 21; i++){
      //   ms.push(this.$store.state.movies[i])
      // }
      // console.log(this.$store.state.movies, "??")
      return ms
    }
  },
  created () {
    this.getMovies()
  },
  methods: {
    getMovies(){
      this.$store.dispatch('getMovies')
    }
  }
}
</script>

<style>

</style>