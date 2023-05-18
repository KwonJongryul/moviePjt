<template>
    <div style="width: 600px;">
      <h1>홈화면</h1>
      <!-- <p v-for="movie in movies" :key="movie.id">{{ movie.title }}</p> -->
      <GenreRec :genremovies="genremovies"/>
    </div>
</template>

<script>
import GenreRec from "@/components/GenreRec"

export default {
  name: 'HomeView',
  data(){
    return {
      // movies : [],
      // getGenremovie : []
    }
  },
  components :{
    GenreRec
  },
  computed : {
    movies(){
      const ms = this.$store.state.movies
      // for(let i = 0; i < 21; i++){
      //   ms.push(this.$store.state.movies[i])
      // }
      return ms
    },
    genremovies(){
      console.log(this.$store.state.genre_movies, '????')
      return this.$store.state.genre_movies
    }
  },
  created () {
    this.getMovies()
  },
  methods: {
    getMovies(){
      this.$store.dispatch('getMovies')
      this.$store.dispatch('getGenremovie')
    },
  }
}
</script>

<style>

</style>