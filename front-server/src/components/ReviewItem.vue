<template>
  <router-link :to="{name:'ReviewDetail', params: {id: review.id}}" style="text-decoration: none;">  
    <li class="d-flex row justify-content-start">
        <!-- <div id="item" class="d-flex align-items-top mt-3">
          <div  class="col-2">
            <img :src="`https://image.tmdb.org/t/p/w500/${ imgUrl }`" alt="이미지 준비중입니다." width="100px">
          </div>
          <div class="col-7">
            <p class="row">제목 : {{ review.title }}</p>
            <p class="row">영화명 : {{ title }}</p>
            <p class="row">작성자 : {{ review.username }}</p>
            <p class="row">작성일 : {{ review.created_at.slice(0, 10) }}</p>
          </div>
          <div class="col-3 align-items-center">
            <div class="row">
              <p>좋아요 {{ review?.like_users.length }}</p>
            </div>
            <div class="row">
              <p>평점 {{ '⭐'.repeat(parseInt(review?.vote/2)) }}</p>
            </div>
          </div>
        </div> -->
      
      <div class="card mb-3 p-0 w-1000"
        style="opacity: 0.8;"
        onmouseover="this.style.opacity='0.9';"
        onmouseout="this.style.opacity='0.8';">
      <div class="row g-0">
          <div class="col-2">
            <img :src="`https://image.tmdb.org/t/p/w500/${ imgUrl }`" 
            class="img-fluid rounded-start" style="height:100%"
            alt="이미지 준비중입니다.">
          </div>
          <div class="col-10 px-3">
            <div class="card-body review_text">
              <p class="card-text" style="text-align:right; color:gray;">
                {{ review.created_at.slice(0, 10) }}</p>
              
              <p class="card-text">"{{ title }}"에 대한 {{ review.username }}님의 후기</p>
              <h1 class="card-title">{{ review.title }}</h1>
              <p class="card-text" style="text-align:right;">
                {{ review.username }}님의 평점 {{ '⭐'.repeat(parseInt(review?.vote/2)) }}</p>
              <p class="card-text" style="text-align:right;">
                💖 {{ review?.like_users.length }}명이 이 리뷰를 좋아해요</p>
            </div>
          </div>
        </div>
      </div>

    </li>
  </router-link>
</template>

<script>
import axios from "axios"
export default {
  name: 'ReviewItem',
  data (){
    return {
      imgUrl : null,
      title  : null
    }
  },
  props:{
    review : Object
  },
  computed:{
  },
  created(){
    this.getImg()
  },
  methods : {
    getImg(){
      axios({
        method : 'get',
        url : `http://127.0.0.1:8000/api/v1/movies/${this.review.movie}/`
      })
      .then((res) => {
        this.imgUrl = res.data.poster_path
        this.title = res.data.title
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
  li{
    list-style: none;
  }

  .review_text {
    font-family: 'Hahmlet', serif;
    background-color : transparent;
    color : black;
    font-size: 23px;
  }

</style>