<template>
  <div>
    <h1 class="mb-5">리뷰 상세 페이지</h1>
    <div class="d-flex justify-content-center">
      <img :src="`https://image.tmdb.org/t/p/w500/${imgUrl}`" alt="이미지 준비중입니다" style="width: 300px;" class="me-5">
      <div>
        <h3>
          <span>제목 : {{ review?.title }}</span>&nbsp;&nbsp;&nbsp;
          <span>작성자 : {{ review?.username }}</span>
        </h3>
        <h3>{{ title }}</h3>
        <p>
          <span>작성일 : {{ review?.created_at.slice(0, 10)}}</span>
        </p>
        <p>
          <span>감상일 : {{ review?.watch_date}}</span>
        </p>
        <p id="like" @click="like">
          <span>👍 : {{ likeUsers }}</span>
        </p>
        <p>
          <span>평점 : {{ '⭐'.repeat(parseInt(review?.vote/2)) }}</span>
        </p>
        <p>
          <span>{{ review?.context }}</span>
        </p>
        <p>
          <span>함께 본 사람 : {{ review?.watch_with }}</span>
        </p>
        <p>
          <span>명대사 : {{ review?.watch_with }}</span>
        </p>
        <router-link :to="{name:'review'}"><button>목록으로</button></router-link>&nbsp;
        <router-link :to="{name:'ReviewUpdate', params: { id : review.id }}" v-if="review?.username===username"><button>수정하기</button></router-link>&nbsp;
        <button @click="reviewDelete" v-if="review?.username===username">삭제하기</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const URL = 'http://127.0.0.1:8000'

export default {
  name:'ReviewDetail',
  data (){
    return {
      review : null,
      username : null,
      imgUrl : null,
      title : null,
    }
  },
  computed:{
    likeUsers(){
      if(this.review){
        return this.review.like_users.length
      }
      return 0
    }
  },
  created(){
    this.getReview(),
    this.getUser()
  },
  methods:{
    getReview(){
      if(!this.$store.getters.islogin){
        this.$router.push({name:'HomeView'})
      }
      axios({
        method : 'get',
        url : `${URL}/api/v1/reviews/${this.$route.params.id}/`,
        headers : {
          Authorization : `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.review = res.data
        this.getImg()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getUser(){
      this.username = this.$store.state.user.username
    },
    reviewDelete(){
      if(!confirm('정말로 삭제하시겠습니까?')){
        alert('취소되었습니다')
        return
      }else{
        axios({
          method : 'delete',
          url : `${URL}/api/v1/reviews/${this.$route.params.id}/`,
          headers : {
            Authorization : `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        alert('삭제되었습니다')
        this.$router.push({name:'review'})
      })
      .catch(() => {
            alert('삭제에 실패하였습니다')
            return
          })
      }
    },
    like(){
      axios({
        method : 'post',
        url : `${URL}/api/v1/like/${this.$route.params.id}/`,
        headers:{
          Authorization : `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          // 좋아요 한 뒤 정보를 다시 가져와 좋아요 수가 화면에
          // 반영되게 함
          this.getReview()
        })
        .catch((err) =>  {
          console.log(err)
        })
    },
    getImg(){
      axios({
        method : 'get',
        url : `http://127.0.0.1:8000/api/v1/movies/${this.review.movie}/`
      })
      .then((res) => {
        this.imgUrl = res.data.poster_path
        this.title = res.data.title
        // console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
  #like{
    cursor: pointer;
  }
</style>