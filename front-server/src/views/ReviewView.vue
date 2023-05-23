<template>
  <div style="width: 1100px;">
    <h1>회원님들이 작성한 리뷰</h1>
    <router-link :to="{name:'ReviewCreate'}" class="my-5"><button>작성하러 가기</button></router-link>
    <ul>
      <hr style="border: solid white;">
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
      // reviews : this.$store.state.reviews
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
  mounted(){
    this.getRivews()
  },
  methods: {
    getRivews(){
      this.$store.dispatch("getRivews")
    },
  },
}
</script>

<style>

</style>