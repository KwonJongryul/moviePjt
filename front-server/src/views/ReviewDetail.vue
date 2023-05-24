<template>
  <div class="review_box" style="width:1100px;">
    <h1 class="mb-2">{{ review?.title }}</h1>
    <div class="row">
      <div class="col-md-5">
        <p id="like" @click="like">
          <span v-if="liked">❤️</span>
          <span v-else>🤍</span>
        </p>
        <p style="font-size:20px; display:inline">{{ likeUsers }}명이 좋아하는 리뷰</p>
      </div>
      <div class="col-md-7" style="text-align:right; margin-bottom:50px;">
        <h5 style="color:rgb(102, 102, 102); margin-bottom:30px;">
          <span class="me-5" style="cursor: pointer;" @click="goProfile">
            작성자 : &nbsp;
            <img :src="`${url+user_img}`" alt="프로필 사진" id="userProfile">&nbsp;&nbsp;
            {{ review?.username }}</span>
          <span>작성일 : {{ review?.created_at.slice(0, 10)}}</span>
        </h5>
        <router-link :to="{name:'review'}">
          <button class="btn btn-light">목록으로</button></router-link>&nbsp;
        <router-link :to="{name:'ReviewUpdate', params: { id : review.id }}" v-if="review?.username===username">
          <button class="btn btn-secondary">수정하기</button></router-link>&nbsp;
        <button @click="reviewDelete" v-if="review?.username===username"
          class="btn btn-danger">
          삭제하기</button>
      </div>
    </div>
    
    <div class="row">
      <div class="col-md-4">
        <router-link :to="{ name: 'MovieDetailView', params: { id: review.movie}}">
          <img :src="`https://image.tmdb.org/t/p/w500/${imgUrl}`" 
          style="width:100%;"
          alt="이미지 준비중입니다">
        </router-link>
        <p style="margin-top:10px; text-align:center;">{{ title }}</p>
      </div>
      <div class="col-md-8">
        <h3>{{ review?.username }}님의 평점 {{ '⭐'.repeat(parseInt(review?.vote/2)) }}</h3>
        <h5 style="margin-top:30px;">{{ review?.watch_date}}에</h5>
        <h5>{{ review?.watch_with}}님과 함께 감상했어요</h5>
        <!-- <h3>{{ title }}</h3> -->
        <!-- <h5> 감상일 : {{ review?.watch_date}}</h5> -->
        <p class="review_content">{{ review?.context }}</p>
        <!-- <h5>{{ review?.watch_with }}와 함께 봤어요</h5> -->
        <h5 style="margin-top:30px;">기억에 남는 대사</h5>
        <h5 class="daesa">"{{ review?.quotes }}"</h5>
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
      // liked: false,
      user_img : null,
      url : URL
    }
  },
  computed:{
    likeUsers(){
      if(this.review){
        return this.review.like_users.length
      }
      return 0
    },
    liked(){
      if(this.review.like_users.includes(this.$store.state.user.id)){
        return true
      }
      return false
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
        this.getUserImg()
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
    },
    getUserImg(){
      axios({
        method:'post',
        url: `${URL}/api/v1/getuser/${this.review.user}/`,
        headers:{
          Authorization : `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.user_img = res.data.user_img
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goProfile(){
      this.$router.push({name:'ProfileView', params : {id:this.review?.user}})
    }
  }
}
</script>

<style>
  #like{
    cursor: pointer;
    font-size: 60px;
    display:inline;
    color: rgb(253, 44, 44);
  }
  .review_content {
    background-color:rgba(255, 255, 255, 0.842);
    padding:15px;
    color:black;
    border-radius: 5px;
    margin-top:40px;
  }

  .daesa {
    background-color:rgba(180, 180, 180, 0.897);
    padding:15px;
    color:black;
    border-radius: 5px;
  }

  .review_box {
    background-color:rgba(255, 255, 255, 0.808);
    border-radius: 20px;
    padding:20px;
    color:black;
  }
  #userProfile{
  width: 50px;
  height: 50px;
  clip-path: circle(50%); /* 가로 길이를 반지름으로 사용 */
  }
</style>