<template>
  <div class="carousel-item" data-bs-interval="2000">
    <router-link :to="{ name: 'MovieDetailView', params: { id: genremovie.id}}">
      <img :src="`${URL+genremovie.backdrop_path}`" class="d-block w-100">
    </router-link>
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