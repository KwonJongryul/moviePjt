<template>
  <!-- 장르별 추천영화 -->
  <div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active" data-bs-interval="2000">
        <img :src="`${URL+genremovies[0].backdrop_path}`" class="d-block w-100">
        <h1>{{ genremovies[0].title }}</h1>
      </div>
      <GenreItem v-for="movie in movies" :key="movie.id" :genremovie="movie"/>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>

<script>
import GenreItem from "@/components/GenreItem"

export default {
  name: 'GenreRec',
  data(){
    return {
      URL : 'https://image.tmdb.org/t/p/w500/',
      // 여기 carousel-item active엔 첫번째 사진 무조건 넣어야 해서 
      // GenreItem에 넣을 애들은 잘랐습니다
      movies : this.genremovies.slice(1)
    }
  },
  components:{
    GenreItem
  },
  props:{
    genremovies : Array
  },
  computed:{
  }
}

</script>

<style>

</style>