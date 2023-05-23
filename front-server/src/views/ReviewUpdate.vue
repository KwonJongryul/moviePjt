<template>
  <div v-if="review">
    <UpdateForm
      :review="review"
    />
  </div>
</template>


<script>
import axios from "axios"
import UpdateForm from '@/components/UpdateForm'
const URL = 'http://127.0.0.1:8000'
export default {
  name: 'UpdateView',
  data (){
    return {
      review : null,
      movies : null
    }
  },
  components:{
    UpdateForm
  },
  created(){
    this.getReview()
  },
  methods:{
    getReview(){
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
  },
}
</script>

<style>

</style>