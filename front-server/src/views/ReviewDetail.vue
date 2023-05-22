<template>
  <div>
    <h1 class="mb-5">리뷰 상세 페이지</h1>
      <h2>
        <span>제목 : {{ review?.title }}</span>&nbsp;&nbsp;&nbsp;
        <span>작성자 : {{ review?.username }}</span>
      </h2>
    <p>
      <span>작성일 : {{ review?.created_at.slice(0, 10)}}</span>
    </p>
    <p>
      <span>감상일 : {{ review?.watch_date}}</span>
    </p>
    <p>
      <span>👍 : {{ review?.like_users.length }}</span>
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
    <router-link :to="{name:'ReviewUpdate'}" v-if="review?.username===username"><button>수정하기</button></router-link>
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
      username : null
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
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getUser(){
      this.username = this.$store.state.username
    }
  }
}
</script>

<style>

</style>