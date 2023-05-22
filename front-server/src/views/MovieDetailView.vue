<template>
  <div class="detail-back">
    <div class="background" :style="{ backgroundImage: 'url(' + backdropImageUrl + ')' }"></div>
    
    <div class="detail_movie">
      <img :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" 
      style="width:500px; height:700px; margin-right:50px; 
      box-shadow:10px 10px 10px rgba(0, 0, 0, 0.589);"
      alt="Movie Poster">

      <div>
        <p style="font-size:60px; margin-bottom:30px;">
          {{ movie.title }}</p>
        <h5 style="text-align:end; margin-bottom:50px;">
          {{ movie.original_title }} | {{ movie.release_date }}</h5>
        <h5 class="overview">{{ movie.overview }}</h5>
        <input type="checkbox" class="overview__more-btn" id="overview-toggle">
        <label for="overview-toggle" class="overview__more-btn-label">더보기</label>
        
        <div style="display:flex; align-items: center; justify-content: end;">
          <div class="star-ratings">
            <div 
              class="star-ratings-fill space-x-2 text-lg"
              :style="{ width: ratingToPercent + '%' }">
              <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
            </div>
            <div class="star-ratings-base space-x-2 text-lg">
              <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
            </div>
          </div>
          <h5 style="margin: 0 0 -30px 10px;">( {{ movie.vote_count }} )</h5>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name : 'MovieDetailView',
  data(){
    return {
      movie: []
    }
  },
  computed : {
    ratingToPercent(){
      const score = +this.movie.vote_average * 10
      return score
    },
    backdropImageUrl() {
      return 'https://image.tmdb.org/t/p/original' + this.movie.backdrop_path
    }
  },
  mounted(){
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
      .catch(()=>{
        this.getMovieDetailAPI()
      })
    },
    getMovieDetailAPI(){
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.$route.params.id}?language=ko-KR`,
        headers: {
          'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzE4MjRjZDQwYjAwNDRkNzk0NGFiNWE1NWQ0Y2IxNiIsInN1YiI6IjYzZDMxNzgwY2I3MWI4MDBhMTBkOTRiYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8hiV71qR0GYKuQVn3fOLORjfCqbz4DglPhvAe3SlhQY'
        },
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

.detail-back {
  position: relative;
  width: 100vw; /* 화면 전체 너비 */
  height: 300px;
}

.detail_movie {
  display:flex; 
  width:1500px; 
  margin-top:200px;
  margin-left: auto;
  margin-right: auto;
}

.background {
  position:absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 400px;
  background-size: cover;
  background-position: center;
  opacity: 0.6;
  margin-top: -40px;
  z-index: -1;
}

.overview {
  font-size: 25px;
  line-height: 45px;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 3; /* 최대 3줄까지 표시 */
  -webkit-box-orient: vertical;
}

.overview__more-btn {
  display: none;
}

.overview__more-btn:checked + .overview {
  -webkit-line-clamp: unset;
}

.overview__more-btn-label {
  appearance: none;
  border: 1px solid white;
  padding: 0.5em;
  border-radius: 0.25em;
  cursor: pointer;
  margin: 5px;
}

.overview__more-btn:checked + .overview__more-btn-label::before {
  content: '닫기';
}

.overview:has(+ .overview__more-btn:checked) {
  -webkit-line-clamp:unset;
}


  .star-ratings {
  color: #000000; 
  position: relative;
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent;
  -webkit-text-stroke-width: 1.3px;
  -webkit-text-stroke-color: rgb(243, 227, 87);
  font-size: 50px;
  }
 
.star-ratings-fill {
  /* color: #ffffff; */
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: rgb(243, 227, 87);
}
 
.star-ratings-base {
  z-index: 0;
  padding: 0;
}
</style>