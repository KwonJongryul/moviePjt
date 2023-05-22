<template>
  <div>
    
  <div style="display:flex; align-items:center;">
    <div class="dropdown">
      <p style="font-size:40px; color:white; border:none;" class="btn dropdown-toggle" data-bs-toggle="dropdown">
        {{ era }}
      </p>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" @click="selectEra('2020')">2020</a></li>
        <li><a class="dropdown-item" @click="selectEra('2010')">2010</a></li>
        <li><a class="dropdown-item" @click="selectEra('2000')">2000</a></li>
        <li><a class="dropdown-item" @click="selectEra('1990')">1990</a></li>
        <li><a class="dropdown-item" @click="selectEra('1980')">1980</a></li>
        <li><a class="dropdown-item" @click="selectEra('1980 이전')">1980 이전</a></li>
      </ul>
    </div>
    <h1>년대 인기작</h1>
    <button class="btn btn-danger m-3" type="button"
    @click="getMovieEra()">
    RESET</button>
  </div>
  
  <h4 style="text-align:end; margin-bottom:20px;">가로로 밀어보세요</h4>
    <div class="swiper-container movie-slider">
      <div class="swiper-wrapper">
        <div class="swiper-slide movie-slider-item" v-for="movie in movies" :key="movie.id">
          <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id}}">
          <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path"  class="img" alt="Movie Poster">
          </router-link>
          <h5 style="margin-top:10px; font-size:18px;">{{ movie.title }}</h5>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios';
// 이거 npm install Swiper해야해요
import Swiper from 'swiper';
import 'swiper/swiper-bundle.css';

export default {
  name: 'EraMovie',
  data() {
    return {
      movies: null,
      era: '2020',
    };
  },
  created() {
    this.getMovieEra();
  },
  methods: {
    getMovieEra() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/movies/era/${this.era}`,
      })
        .then((res) => {
          this.movies = res.data;
          this.initSwiper();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    initSwiper() {
      new Swiper('.movie-slider', {
        slidesPerView: 5,
        spaceBetween: 50,
        loop : true,
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
        },
      });
    },
    selectEra(selectedEra){
      this.era = selectedEra
      this.getMovieEra()
    }
  },
};
</script>

<style>
.movie-slider {
  width: 100%;
  overflow: hidden;
}

.swiper-slide {
  text-align: center;
}

.movie-slider-item {
  display: inline-block;
  margin-right: 20px;
}

.img{
  width: 200px;
  height: 300px;
}
</style>
