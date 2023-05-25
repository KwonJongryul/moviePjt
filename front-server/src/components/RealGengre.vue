<template>
  <div>
    <!-- 임시 로직 이름 바꾸기 힘들어서 그냥 이걸로 -->
  <div style="display:flex; align-items:center;">
    <div class="dropdown">
      <p style="font-size:40px; color:white; border:none;" class="btn dropdown-toggle" data-bs-toggle="dropdown">
				장르 {{ genre }}
      </p>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item"
				@click="selectGenre(genre.name)"
				v-for="genre in genres"
				:key="genre.id"
				>{{ genre.name }}</a></li>
      </ul>
    </div>
    <h1>의 추천작!</h1>
    <button class="btn btn-danger m-3" type="button"
    @click="getMovies()">
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
const URL = 'http://127.0.0.1:8000'
export default {
  name: 'EraMovie',
  data() {
    return {
      movies: null,
      genres : null,
			genre : '모험'
    };
  },
  created() {
		this.getGenre()
    this.getMovies();
  },
  methods: {
		// 장르받아오기---------------------
		getGenre(){
			axios({
				method: 'get',
				url : `${URL}/api/v1/genres/`
			})
			.then((res) =>{
				this.genres = res.data.filter(el => el.id!='9999')
			})
			.catch((err) => {
				console.log(err)
			})
		},
    getMovies() {
			axios({
				method: 'get',
        url: `${URL}/api/v1/movies/genre/${this.genre}/`,
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
    selectGenre(selectGenre){
      this.genre = selectGenre
      this.getMovies()
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
