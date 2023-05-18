<template>
  <!-- 장르별 추천영화 -->
  <div>
    <div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="10000">
          <img :src="`${URL+genremovies[0].backdrop_path}`" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item" data-bs-interval="2000">
          <img :src="`${URL+genremovies[1].backdrop_path}`" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img :src="`${URL+genremovies[2].backdrop_path}`" class="d-block w-100" alt="...">
        </div>
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
  </div>
</template>

<script>
export default {
  name: 'GenreRec',
  data(){
    return {
      URL : 'https://image.tmdb.org/t/p/w500/'
    }
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