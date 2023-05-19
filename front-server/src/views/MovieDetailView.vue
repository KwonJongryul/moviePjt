<template>
  <div>
    <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" alt="Movie Poster">
    <p>제목 : {{ movie.title }}</p>
    <p>개봉일 : {{ movie.release_date }}</p>
    <p>줄거리 : {{ movie.overview }}</p>
    <p>평균별점 : {{ movie.vote_average }}</p>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name : 'MovieDetailView',
  data(){
    return {
      movie: []
    }
  },
  mounted(){
    this.getMovieDetail()
  },
  methods : {
    getMovieDetail(){
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/movies/${this.$route.params.id}`,
      })
      .then((res)=>{
        this.movie = res.data
      })
      .catch(()=>{
        this.getMovieDetailAPI()
      })
    },
    getMovieDetailAPI(){
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.$route.params.id}?language=ko-KR`,
        headers: {
          'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzE4MjRjZDQwYjAwNDRkNzk0NGFiNWE1NWQ0Y2IxNiIsInN1YiI6IjYzZDMxNzgwY2I3MWI4MDBhMTBkOTRiYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8hiV71qR0GYKuQVn3fOLORjfCqbz4DglPhvAe3SlhQY'
        },
      })
      .then((res)=>{
        this.movie = res.data
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  }

}
</script>

<style>

</style>