<template>
  <div>
    <div style="display: flex; align-items: center;">
      <button v-if="!liked" @click="like" class="btn btn-secondary">❤</button>
      <button v-if="liked" @click="like" class="btn btn-danger">❤</button>
      <h3 style="margin-left: 20px;">좋아요</h3>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LikeMovie',
  data(){
    return {
      liked : false
    }
  },
  props: {
    movie: Object
  },
  methods:{
    like(){
      axios({
        method : 'post',
        url : `http://127.0.0.1:8000/api/v1/movielike/${this.$route.params.id}/`,
        headers:{
          Authorization : `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          // 좋아요 한 뒤 정보를 다시 가져와 좋아요 수가 화면에
          // 반영되게 함
          console.log('되냐?')
        })
        .catch((err) =>  {
          console.log(err)
        })
      this.liked = !this.liked
    },
  }
}
</script>

<style>

</style>