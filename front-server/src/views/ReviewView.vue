<template>
  <div style="width: 600px;">
    <h1>회원님들이 작성한 리뷰</h1>
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
    }
  },
}
</script>

<style>

</style>