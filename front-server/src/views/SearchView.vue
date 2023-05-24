<template>
  <div>
    <div class="search-container">
      <input type="text" v-model="search_movie" 
      @keydown.enter="enterSearch" class="search_input" 
      placeholder="검색어를 입력하세요">
      <router-link :to="{ name: 'SearchView', params: { word: search_movie } }">
        <button @click="getSearchMovie" class="search-button">🔍︎</button>
      </router-link>
    </div>
    
    <div class="search-container" style="font-size:20px;">
        "<span style="color:rgb(79, 208, 234);">{{ search_movie }}</span>
        "검색 결과 총<span style="color:rgb(79, 208, 234);"> {{ search_results && search_results.length }}</span>건의 영화가 발견되었습니다.
    </div>

    <div class="search-results">
    <div v-if="search_results" class="row row-cols-1 row-cols-md-3 g-4">
      <div v-for="movie in search_results" :key="movie.id" class="col">
        <div class="card" 
        style="display: flex; justify-content: center; align-items: center; 
        width:300px;">

        <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id}}">
        <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" 
        class="card-img-top" style="width:300px; height:430px;"
        alt="Movie Poster">
        </router-link>

        <h5 class="card-title" 
        style="width:300px; height:60px; text-align: center; font-size:15px; 
        display:flex; justify-content:center; align-items:center; padding:15px; color:black;">
        {{ movie.title }}</h5>
        </div>
      </div>
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
  created() {
    const { word } = this.$route.params;
    if (word) {
      this.search_movie = word;
      this.getSearchMovie()
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
    },
    enterSearch() {
      // const keyword = this.search_movie.trim();
      //   if (keyword) {
      this.$router.push(`/searchlist/${this.search_movie}`);
      this.getSearchMovie()
        // }
    },
  },
}
</script>

<style>
  .search-container {
    position: relative;
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
  }

  .search_input {
    padding: 20px;
    border: 3px solid white;
    border-radius: 50px;
    margin-right: 10px;
    height: 60px;
    font-size: 26px;
    background-color: transparent;
    color: white;
    outline: none;
  }

  .search-button {
    background-color: transparent;
    border: none;
    cursor: pointer;
    color: white;
    font-size: 40px;
    background-color: transparent;
  }

  .search-results {
    /* margin-top: 80px; */
    padding: 20px;
    width: 1100px;
  }
</style>