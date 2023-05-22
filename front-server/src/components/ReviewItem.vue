<template>
  <router-link :to="{name:'ReviewDetail', params: {id: review.id}}" style="text-decoration: none;">  
    <li class="d-flex row justify-content-start">
        <div id="item" class="d-flex align-items-top mt-3">
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
        </div>
    </li>
    <hr style="border: solid white;">
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
  p{
    font-family: 'Hahmlet', serif;
    background-color : black;
    color : white;
  }

</style>