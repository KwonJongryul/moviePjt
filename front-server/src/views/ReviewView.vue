<template>
  <div>
    <div style="display:flex; width: 1300px;">
      <p style="margin-bottom:50px; font-size:70px;">회원 리뷰</p>
      <div style="margin-left:auto;">
      <router-link :to="{name:'ReviewCreate'}">
        <button class="btn btn-light">작성하기</button>
      </router-link>
      </div>
    </div>

    <ul>
      <!-- <hr style="border: solid white;"> -->
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