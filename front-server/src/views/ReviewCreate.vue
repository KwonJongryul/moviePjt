<template>
  <div>
    <form @submit.prevent="create">
      <p>
        <label for="title"><strong>제목</strong></label>
        <input type="text" v-model.trim="title" id="title">
      </p>
      <p>
        <label for="movie"><strong>영화 </strong></label>
        <input type="text" list="movies" id="movie" v-model="keyWord" @input="onInput" placeholder="영화를 입력해 주세요!" @change="selectMovie">
        <datalist id ="movies">
          <option v-for="movie in movies" :key="movie.id" :data-icon="'https://image.tmdb.org/t/p/w500' + movie.poster_path" :data-movieId="movie.id">
            <a @click="selectMovie">{{ movie.title }}</a>
          </option>
        </datalist>
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
        <input type="submit" value="작성하기">
      </p>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
// import SelectItem from '../components/SelectItem.vue'
const URL = 'http://127.0.0.1:8000'
export default {
  name : 'ReviewCreate',
  components:{
    // SelectItem
  },
  data () {
    return {
      title : null,
      context : null,
      watch_date : null,
      quotes : null,
      movie : null,
      vote : 0,
      watch_with : null,
      // 셀렉트 검색
      keyWord : null,
      movies : null
    }
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
        console.log(movie)
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
    onInput(){
      if (this.keyWord){
        axios({
          method  : 'get',
          url : `${URL}/api/v1/movies/option/${this.keyWord}/`,
        })
        .then((res) => {
          this.movies = res.data
        })
        .catch((err) => {
          console.log(err)
        })
      }else{
        this.movieId = null
      }
    },
    selectMovie(event){
      const option = event.target.parentElement.querySelector('option')
      const movieId = option.getAttribute('data-movieId')
      this.movie = movieId
      console.log(this.movie)
    }
  }
}
</script>

<style>

</style>