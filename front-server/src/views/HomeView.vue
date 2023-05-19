<template>
    <div style="width: 600px;">
      <h1>최근 작품</h1>
      <GenreRec :genremovies="genremovies"/>
    </div>
</template>

<script>
import GenreRec from "@/components/GenreRec"

export default {
  name: 'HomeView',
  data(){
    return {
    }
  },
  components :{
    GenreRec
  },
  computed : {
    // 아직 임의로 만들어 놓음!!!!로직 없음
    movies(){
      const ms = this.$store.state.movies
      // for(let i = 0; i < 21; i++){
      //   ms.push(this.$store.state.movies[i])
      // }

      return ms
    },
    genremovies(){
      return this.$store.state.genre_movies
    }
  },
  created () {
    this.getMovies()
  },
  methods: {
    getMovies(){
      this.$store.dispatch('getMovies')
    },
  }
}
</script>

<style>

</style>