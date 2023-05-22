<template>
  <div>
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img :src="'https://image.tmdb.org/t/p/w500' + movies[0].poster_path" alt="Movie Poster">
      </div>
      <div v-for="(movie, index) in movies" :key="movie.id" class="carousel-item" :class="{ 'active': index === 0 }">
      <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" alt="Movie Poster">
      </div> 
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>


  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'EraMovie',
  data() {
    return {
      movies : null
    }
  },
  created(){
    this.getMovieEra()
  },
  methods : {
    getMovieEra(){
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/movies/era`,
      })
      .then((res)=>{
        this.movies = res.data
      })
      .catch((err)=>{
        console.log(err)
      })
    },
  }
}
</script>

<style>

</style>