<template>
  <div>
  <form @submit.prevent="create">
    <div class="review_box" style="width:1100px;">
      <!-- <h1 class="mb-2">{{ review?.title }}</h1> -->
      <!-- <label for="title"><strong>제목</strong></label> -->
      <h1>
        <input type="text" v-model.trim="title" id="title" 
        class="input_r" placeholder="제목">
      </h1>
    
    <div class="row">
      <div class="col-md-4">
        <p style="margin-top:10px; text-align:center;">
          <!-- <label for="movies"><strong>영화 </strong></label> -->
          <select class="movieSelect" style="width: 250px;">
            <option value="">영화를 선택해 주세요!</option>
            <option v-for="movie in movies" :key="movie.id" :value="movie.id+','+movie.poster_path">{{ movie.title }}</option>
          </select>
          <img v-if="movie_img" :src="`https://image.tmdb.org/t/p/w500/${ movie_img }`" 
          alt="이미지 준비중입니다." width="300px" style="margin-top: 80px;">
        </p>
      </div>

      <div class="col-md-8">
        <div>
          <h5>
            <label for="vote" style="margin-right:10px;">평점</label>
              <input type="range" v-model="vote" id="vote" 
              class="my-3" min="0" max="10" step="0.5">
              {{ '⭐'.repeat(parseInt(vote/2)) }}
          </h5>
        </div>
        <h5>
          <input class="input_r" type="date" v-model="watch_date" id="date">
          에
        </h5>
        <h5>
          <input class="input_r" type="text" v-model.trim="watch_with" id="watch_with">
          님과 함께 감상했어요
        </h5>

        <p class="review_content">
          <textarea class="input_r" cols="30" rows="10" v-model="context" id="context"></textarea>
        </p>
        <!-- <h5>{{ review?.watch_with }}와 함께 봤어요</h5> -->
        <h5 style="margin-top:30px;">기억에 남는 대사</h5>
        <h5 class="daesa">"
          <input class="input_r" type="text" style="width:640px;"
          v-model.trim="quotes" id="quotes">"</h5>
        
        <div class="d-grid gap-2 col-6 mx-auto my-4">
          <button type="submit" class="btn btn-primary">작성하기</button>
        </div>
      </div>
    </div>
    </div>
  </form>

  </div>
</template>

<script src="https://code.jquery.com/jquery-1.12.4.js"></script>

<script>
import axios from 'axios'
const URL = 'http://127.0.0.1:8000'
export default {
  name : 'ReviewCreate',
  data () {
    return {
      title : null,
      context : null,
      watch_date : null,
      quotes : null,
      movie : null,
      vote : 0,
      watch_with : null,
      keyWord : null,
      movies : null,
      movie_img : null,
    }
  },
  mounted() {
    $(this.$el)
    .find(".movieSelect")
    .select2();
    $(document).ready(function() {
      $('.movieSelect').select2({
        templateResult: function(movie) {
          if (!movie.id) {
            return movie.text;
          }
          var $movie = $('<span style="color: black;">' + movie.text + '</span>');
          return $movie;
        },
        templateSelection: function(movie) {
          return movie.text;
        }
      });
    });
    // $('#movieSelect').on('change',function(event){ console.log(event.target.value) })
    $('.movieSelect').on('change', this.updateMovie)
  },
  created() {
    this.moviesAll()
  },
  methods : {
    create(){
      const title = this.title
      const context = this.context
      const watch_date = this.watch_date
      const quotes = this.quotes
      const movie = this.movie
      const vote = this.vote
      const watch_with = this.watch_with
      console.log(movie)
      if(!title){
        alert('제목을 입력해 주세요')
        return
      }else if(!vote){
        alert('평점을 입력해 주세요')
        return
      }else if(!context){
        alert('내용을 입력해 주세요')
        return
      }else if(!movie){
        alert('영화를 선택해 주세요')
        return
      }
      axios({
        method : 'post',
        url : `${URL}/api/v1/reviews/`,
        headers : {
          Authorization : `Token ${ this.$store.state.token }`
        },
        data:{
          title, context, watch_date, quotes, movie, vote, watch_with
        }
      })
        .then(() => {
          this.$router.push({name:'review'})
        })
        .catch((err) => {
          console.log(err)
        })
    },
    moviesAll(){
      axios({
        method : 'get',
        url : `${URL}/api/v1/movies/all/`
      })
      .then((res) => {
        this.movies=res.data
      })
    },
    updateMovie(event){
      const tmp = event.target.value.split(',')
      this.movie = tmp[0]
      this.movie_img = tmp[1]
      // this.movie = event.target.value
      // console.log(event.target.value)
      this.getReviewImg()
    },
    getReviewImg(){
      axios({
        method : 'get',
        url : `${URL}/api/v1/movies/${this.movie_img}/`
      })
      .then((res) => {
        this.movie_info=res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
}

</script>

<style>
  /* #movies > option{
    color: black;
  } */

  textarea {
    width: 670px;
  }

  .input_r {
    border: none;
    border-radius: 5px;;
    outline: none;
    padding: 5px;
    opacity: 0.7;
    
  }

</style>