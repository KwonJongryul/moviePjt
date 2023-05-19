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
      movie: null
    }
  },
  created(){
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
      .catch((err)=>{
        console.log(err)
      })
    }
  }

}
</script>

<style>

</style>