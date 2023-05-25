<template>
  <div style="width: 1100px;">
    <div style="margin-bottom:100px;">
      <h1>최근 작품</h1>
      <GenreRec :genremovies="genremovies"/>
    </div> 
    <div>
      <EraMovie>0</EraMovie>
    </div>
    <RealGengre/>
  </div>

</template>

<script>
import GenreRec from "@/components/GenreRec"
import EraMovie from "@/components/EraMovie"
import RealGengre from '@/components/RealGengre.vue'
export default {
name: 'HomeView',
data(){
  return {
  }
},
components :{
  GenreRec,
  EraMovie,
  RealGengre
},
computed : {
  // 아직 임의로 만들어 놓음!!!!로직 없음
  movies(){
    const ms = this.$store.state.movies
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