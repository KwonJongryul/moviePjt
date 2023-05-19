<template>
  <li>
    <img :src="`https://image.tmdb.org/t/p/w500/${ imgUrl }`" alt="이미지 준비중입니다." width="100px">
    {{ review }}
  </li>
</template>

<script>
import axios from "axios"
export default {
  name: 'ReviewItem',
  data (){
    return {
      imgUrl : null
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
</style>