<template>
  <div class="carousel-item" data-bs-interval="2000">
    <img :src="`${URL+genremovie.backdrop_path}`" class="d-block w-100">
    <h3 style="text-align:end;">{{ genremovie.title }}</h3>
  </div>


</template>

<script>
export default {
  name:'GenreItem',
  data(){
    return {
      URL : 'https://image.tmdb.org/t/p/original/'
    }
  },
  props:{
    genremovie : Object
  }
}
</script>

<style>

</style>