<template>
  <div class="detail-back">
    <!-- 이거는 뒷배경 -->
    <div class="background" :style="{ backgroundImage: 'url(' + backdropImageUrl + ')' }"></div>
    
    <div class="detail_movie">
      <!-- 포스터 -->
      <img :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" 
      style="width:500px; height:700px; margin-right:50px; 
      box-shadow:10px 10px 10px rgba(0, 0, 0, 0.589);"
      alt="Movie Poster">

      <div>
        <!-- 여기는 영화 설명임 -->
        <p style="font-size:50px; margin-bottom:20px; background-color: transparent;">
          {{ movie.title }}</p>
        <div style="font-size:20px; margin-bottom:50px;
        display: flex; justify-content: space-between;">
          <span>
            {{ movie.original_title }} | {{ movie.release_date }}
          </span>
          <button type="button" class="btn btn-danger" @click="showTrailer">
            {{ buttonText }}
          </button>
        </div>

        <div v-if="trailer">
          <h5 class="overview">{{ movie.overview }}</h5>
          <input type="checkbox" class="overview__more-btn" id="overview-toggle">
          <label for="overview-toggle" class="overview__more-btn-label"></label>
          <!-- 요고는 전체별점임 -->
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
            <h5 style="margin: 0 0 -30px 10px;">전체 평점 {{ this.movie.vote_average / 2 }} ( {{ movie.vote_count }} )</h5>
          </div>
        </div>

        <!-- 예고편한번 가져와본다내가 -->
        <div v-if="!trailer">
          <iframe width="950" height="500" 
          :src="`https://www.youtube.com/embed/${ video.results[0].key }`" 
          frameborder="0" allowfullscreen></iframe>
        </div>
        
      </div>
    </div>

    <!-- 여기서부터는 credit입니다 -->
    <div class="credit_detail">
      <hr style="border:3px solid white;">
      <h1 class="mb-4">감독</h1>
      <div class="people">
      <div v-for="crew in credits.crew" :key="crew.id">
        <div v-if="crew.job === 'Director'" class="person">
          <img :src="'https://image.tmdb.org/t/p/original' + crew.profile_path" 
          style="width:150px; height:200px;"
          alt="Director">
          <p style="font-size:20px; margin-bottom:0">{{ crew.name }}</p>
          <p style="font-size:17px; color:gray">{{ crew.job }}</p>
        </div>
      </div>
      </div>
      <h1 class="mb-4">출연</h1>
      <div class="people">
      <div v-for="(cast, index) in credits.cast" :key="cast.id">
        <div v-if="cast.known_for_department === 'Acting' && index < 7" class="person">
          <img :src="'https://image.tmdb.org/t/p/original' + cast.profile_path" 
          style="width:150px; height:200px;">
          <p style="font-size:20px; margin-bottom:0;">{{ cast.name }}</p>
          <p style="font-size:17px; color:gray">{{ cast.character }} 역</p>
        </div>
      </div>
      </div>
    </div>


  </div>
</template>

<script>
import axios from 'axios'
// import CreditMovie from "@/components/CreditMovie"

export default {
  name : 'MovieDetailView',
  data(){
    return {
      movie: [],
      credits : [],
      video : [],
      trailer : true,
      buttonText : '예고편 보러가기'
    }
  },
  // components :{
  //   CreditMovie
  // },
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
    this.getCreditMovie()
    this.getTrailer()
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
    },
    getCreditMovie(){
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.$route.params.id}/credits?language=ko-KR`,
        headers: {
          // 'Accept' : 'application/json',
          'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzE4MjRjZDQwYjAwNDRkNzk0NGFiNWE1NWQ0Y2IxNiIsInN1YiI6IjYzZDMxNzgwY2I3MWI4MDBhMTBkOTRiYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8hiV71qR0GYKuQVn3fOLORjfCqbz4DglPhvAe3SlhQY'
        },
      })
      .then((res)=>{
        this.credits = res.data
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    getTrailer(){
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.$route.params.id}/videos?language=en-US`,
        headers: {
          'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzE4MjRjZDQwYjAwNDRkNzk0NGFiNWE1NWQ0Y2IxNiIsInN1YiI6IjYzZDMxNzgwY2I3MWI4MDBhMTBkOTRiYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8hiV71qR0GYKuQVn3fOLORjfCqbz4DglPhvAe3SlhQY'
        },
      })
      .then((res)=>{
        this.video = res.data
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    showTrailer(){
      this.trailer = !this.trailer
      if (this.trailer){
        this.buttonText = '예고편 보러가기'
      } else {
        this.buttonText = '줄거리 보러가기'
      }
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
  -webkit-line-clamp: 8; /* 최대 3줄까지 표시 */
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

.overview__more-btn-label::before {
  content: '더보기';
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

.credit_detail {
  /* display:flex;  */
  width:1500px; 
  margin-top:50px;
  margin-left: auto;
  margin-right: auto;
}

.people {
  display:flex;
  text-align: center;
  margin-bottom: 20px;
}

.person {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-right: 60px;
  flex:1;
  width:150px;
}
</style>