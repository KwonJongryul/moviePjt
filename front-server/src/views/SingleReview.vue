<template>
  <div>
    <div style="display:flex; width: 1000px;">
      <p style="margin-bottom:30px; font-size:50px;">{{ user.username }}님의 리뷰</p>
    </div>
    <div style="display:flex; justify-content:flex-end; margin-bottom:30px;">
      <router-link :to="{name:'ReviewCreate'}">
        <button class="btn btn-primary ml-auto">작성하기</button>
      </router-link>
    </div>

    <ul>
      <!-- <hr style="border: solid white;"> -->
      <!-- 여기수정 -->
      <ReviewItem 
        v-for="review in paginatedReviews" 
        :key="review.id"
        :review="review"
      />
    </ul>

    <!-- <div>
      <button @click="previousPage" :disabled="currentPage === 1">이전</button>
      <button @click="nextPage" :disabled="currentPage === totalPages">다음</button>
    </div> -->

    <nav aria-label="Page navigation example" class="d-flex justify-content-center">
      <ul class="pagination">
        <li class="page-item">
          <a class="page-link" href="#" aria-label="Previous" @click="previousPage" :disabled="currentPage === 1">
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>
        <li class="page-item" v-for="page in totalPages" :key="page" :class="{ active: page === currentPage }">
          <a class="page-link" href="#" @click="goToPage(page)">{{ page }}</a>
        </li>
        <li class="page-item">
          <a class="page-link" href="#" aria-label="Next" @click="nextPage" :disabled="currentPage === totalPages">
            <span aria-hidden="true">&raquo;</span>
          </a>
        </li>
      </ul>
    </nav>

  </div>
</template>

<script>
import axios from 'axios'
import ReviewItem from "@/components/ReviewItem"
const URL = 'http://127.0.0.1:8000'
export default {
  name: 'ReviewView',
  data(){
    return {
      // reviews : this.$store.state.reviews
      revies: [],
      currentPage: 1,
      reviewsPerPage: 5,
			user: null
    }
  },
  computed:{
    reviews(){
      return this.$store.state.s_reviews
    },
    islogin(){
      return this.$store.getters.islogin
    },
    totalPages() {
    // 전체 페이지 수 계산
    return Math.ceil(this.reviews.length / this.reviewsPerPage);
    },
    paginatedReviews() {
      // 현재 페이지에 해당하는 리뷰만 반환
      const startIndex = (this.currentPage - 1) * this.reviewsPerPage;
      const endIndex = startIndex + this.reviewsPerPage;
      return this.reviews.slice(startIndex, endIndex);
    }
  },
  components : {
    ReviewItem
  },
  mounted(){
		this.getUser()
    
  },
  methods: {
    getUser(){
      axios({
        method:'post',
        url: `${URL}/api/v1/getuser/${this.$route.params.id}/`,
        headers:{
          Authorization : `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.user = res.data
				this.getRivews()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getRivews(){
			console.log(this.$store.state.s_reviews)
			console.log(this.user)
      this.$store.dispatch("getSingleRivews", this.user.id)
    },
    previousPage() {
    // 이전 페이지로 이동
    if (this.currentPage > 1) {
      this.currentPage--;
    }
    },
    nextPage() {
      // 다음 페이지로 이동
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    goToPage(page) {
    this.currentPage = page;
    }
  },
}
</script>

<style>

</style>