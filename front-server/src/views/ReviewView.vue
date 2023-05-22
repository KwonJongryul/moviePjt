<template>
  <div style="width: 600px;">
    <h1>회원님들이 작성한 리뷰</h1>
    <button @click="goCreate">작성하러 가기</button>
    <ul>
      <ReviewItem 
      v-for="review in reviews" 
      :key="review.id"
      :review="review"
      />
    </ul>
  </div>
</template>

<script>
// import axios from 'axios'
import ReviewItem from "@/components/ReviewItem"
export default {
  name: 'ReviewView',
  data(){
    return {
    }
  },
  computed:{
    reviews(){
      return this.$store.state.reviews
    },
    islogin(){
      return this.$store.getters.islogin
    }
  },
  components : {
    ReviewItem
  },
  created(){
    this.getRivews()
  },
  methods: {
    getRivews(){
      this.$store.dispatch("getRivews")
    },
    goCreate(){
      if (this.islogin){
        this.$router.push({name:'ReviewCreate'})
      }else{
        this.$router.push({name : 'LoginView'})
      }
    },
  },
}
</script>

<style>

</style>