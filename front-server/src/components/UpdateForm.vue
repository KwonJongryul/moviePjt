<template>
  <div>
    <form @submit.prevent="create">
      <p>
        <label for="title"><strong>제목</strong></label>
        <input type="text" v-model.trim="title" id="title">
      </p>
      <p>
        <label for="movies"><strong>영화 </strong></label>
        <select id="movieSelect" style="width: 250px;">
          <option value="">영화를 선택해 주세요!</option>
          <option v-for="movie in movies" :key="movie.id" :value="movie.id">{{ movie.title }}</option>
        </select>
      </p>
      <p>
        <label for="date"><strong>감상날짜</strong></label>
        <input type="date" v-model="watch_date" id="date">
      </p>
      <p>
        <label for="vote"><strong>내 평점</strong></label>
        <input type="range" v-model="vote" id="vote" min="0" max="10" step="0.5">
      </p>
      <p>
        <label for="context"><strong>내용</strong></label><br>
        <textarea cols="30" rows="10" v-model="context" id="context"></textarea>
      </p>
      <p>
        <label for="quotes"><strong>명대사를 적어주세요!</strong></label><br>
        <input type="text" v-model.trim="quotes" id="quotes">
      </p>
      <p>
        <label for="watch_with"><strong>누구랑 보셨나요?</strong></label><br>
        <input type="text" v-model.trim="watch_with" id="watch_with">
      </p>
      
      <p>
        <input type="submit" value="수정하기">
      </p>
    </form>
  </div>
</template>

<script src="https://code.jquery.com/jquery-1.12.4.js">

</script>
<script>
import axios from 'axios'


const URL = 'http://127.0.0.1:8000'
export default {
  name : 'UpdateForm',
  props:{
    review : Object
  },
  data () {
    return {
      title : this.review.title,
      context : this.review.context,
      watch_date : this.review.watch_date,
      quotes : this.review.quotes,
      movie : this.review.movie,
      vote : this.review.vote,
      watch_with : this.review.watch_with,
      movies : null
    }
  },
  mounted() {
  $(this.$el)
    .find("#movieSelect")
    .select2();
    $(document).ready(function() {
      $('#movieSelect').select2({
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
    $('#movieSelect').on('change', this.updateMovie)
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
        method : 'put',
        url : `${URL}/api/v1/reviews/${this.review.id}/`,
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
      .catch((err) => {
        console.log(err)
      })
    },
    updateMovie(event){
      this.movie = event.target.value
    }
  },
}

</script>

<style>
  /* #movies > option{
    color: black;
  } */
</style>