<template>
  <div style="width: 1100px;" class="d-flex row mt-5">
    <div class="col-4">
      <div class="row justify-content-center">
        <div class="">
          <img :src="url + user.user_img" alt="이미지가 없어요 😢" id="profile2">
          <h3>{{ user.username }}</h3>
        </div>
      </div>
    </div>
    <div class="col-8">

    </div>
  </div>
</template>

<script>
import axios from "axios"
const URL = 'http://127.0.0.1:8000'
export default {
  name:'ProfileView',
  data(){
    return {
      user : null,
      url : URL
    }
  },
  created(){
    this.getUser()
  },
  methods:{
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
        console.log(this.user)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
#profile2{
  width: 200px;
  height: 200px;
  clip-path: circle(50%); /* 가로 길이를 반지름으로 사용 */
}
</style>