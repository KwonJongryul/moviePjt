<template>
  <div>
    <div>
      <input type="text" v-model="search_movie">
      <button @click="getSearchMovie">🔍</button>
    </div>
    <!-- <div v-if="search_results">
      <div v-for="movie in search_results" :key="movie.id">
        <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" alt="Movie Poster">
        <p>{{ movie.title }}</p>
      </div>
    </div> -->


    <div v-if="search_results" class="row row-cols-1 row-cols-md-3 g-4">
      <div v-for="movie in search_results" :key="movie.id" class="col">
        <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" class="card-img-top" alt="Movie Poster">
        <h5 class="card-title">{{ movie.title }}</h5>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SearchView',
  data(){
    return {
      search_movie: '',
      search_results: null,
    }
  },
  methods: {
    getSearchMovie(){
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/search/movie`,
        headers: {
          'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzE4MjRjZDQwYjAwNDRkNzk0NGFiNWE1NWQ0Y2IxNiIsInN1YiI6IjYzZDMxNzgwY2I3MWI4MDBhMTBkOTRiYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8hiV71qR0GYKuQVn3fOLORjfCqbz4DglPhvAe3SlhQY'
        },
        params: {
          query: this.search_movie,
          include_adult: true,
          language: 'ko-KR',
          page: 1
        }
      })
      .then((res)=>{
        this.search_results = res.data.results;
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