<template>
  <div class="row">
    <div class="col-2">
      <p style="font-size: small; text-align: center;">{{ recomment?.created_at.slice(0, 10) }}</p>
      <img :src="`${url + user_img}`" alt="profile" width="50px" style="cursor: pointer; clip-path: circle(50% at center);" class="ms-5" id="profile" @click="goProfile">
    </div>
    <div class="col-10 d-flex align-items-center">
      <span>{{ recomment?.context }}</span>
    </div>
    <div class="d-flex justify-content-between my-3">
      <span style="font-size: small;margin-left: 60px; cursor: pointer;" @click="goProfile">{{ recomment?.username }}</span>
      <i class="far fa-trash-alt" style="cursor: pointer; margin-right: 90px;" @click.prevent="recommentDelete"></i>
    </div>
    <hr style="width: 85%; margin-left: auto; margin-right: 80px;" class="mt-1">
  </div>
</template>

<script>
import axios from "axios"

const URL = 'http://127.0.0.1:8000'
export default {
  name:'RecommentItem',
  data(){
    return {
      recomment : null,
      now_user : this.$store.state.user.id,
      user_img : null,
      url : URL,
    }
  },
  created(){
    this.getRecomment()
  },
  props:{
    recomment_id : Number
  },
  methods:{
    getRecomment(){
      axios({
        method : 'get',
        url : `${URL}/api/v1/recomment/${this.recomment_id}/`
      })
      .then((res) => {
        this.recomment = res.data
        this.getUserImg()
      })
      .catch((err) => {
        console.log(err)
      })
    },
        // 유저이미지--------------
    getUserImg(){
      axios({
        method:'post',
        url: `${URL}/api/v1/getuser/${this.recomment.user}/`,
        headers:{
          Authorization : `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.user_img = res.data.user_img
      })
      .catch((err) => {
        console.log(err)
      })
    },
    recommentDelete(){
      if(!confirm("삭제하시겠습니까?")){
        return
      }
      axios({
        method : 'delete',
        url : `${URL}/api/v1/recomment/${this.recomment.id}/`
      })
      .then(() => {
        alert('삭제되었습니다')
        this.$emit('deleted')
      })
      .catch((err) => {
        console.log(err)
        alert('실패했습니다')
      })
    },
    goProfile(){
      this.$router.push({name:'ProfileView', params : {id:this.recomment?.user}})
    },
  }
}
</script>

<style>

</style>