<template>
    <div class="carousel-item active" data-bs-interval="2000">
      <img :src="`${URL+genremovie.backdrop_path}`" class="d-block w-100">
      <h1>{{ genremovie.title }}</h1>
      <!-- {{ genremovie }} -->
    </div>
</template>

<script>
export default {
  name:'GenreItem',
  data(){
    return {
      URL : 'https://image.tmdb.org/t/p/w500/'
    }
  },
  props:{
    genremovie : Object
  }
}
</script>

<style>

</style>