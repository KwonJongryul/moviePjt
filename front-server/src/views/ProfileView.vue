<template>
<div style="width: 1200px;" class="d-flex row mt-5">
  <div class="col-4 d-flex justify-content-center divBox">
    <div align="center">
      <img :src="url + user?.user_img" alt="이미지가 없어요 😢" id="profile2">
      <h3 style="text-align: center; margin-top: 30px;">{{ user?.username }}</h3>
      <button v-if="user?.id!=now_user?.id && false==isFollowed" @click="onFollow">팔로우 하기</button>
      <button v-if="isFollowed" @click="onFollow">팔로우 취소</button>
      <div class="row mt-4">
        <div class="col">
          <p>{{ user?.followers.length }}</p>
          <p>Followers</p>
        </div>
        <div class="col">
          <p>{{ user?.followings.length }}</p>
          <p>Following</p>
        </div>
      </div>
      <div style="border: solid 1px brown; height: 50px; cursor: pointer;" class="d-flex align-items-ceter justify-content-center mt-4"
      @click="goUpdate"
      >
        <span style="margin: auto 0;">{{ user?.username }}님이 쓴 리뷰 보러가기</span>
      </div>
      <div style="border: solid 1px brown; height: 50px; cursor: pointer;" class="d-flex align-items-ceter justify-content-center mt-4"
      v-if="user?.id==now_user"
      @click="goUpdate"
      >
        <span style="margin: auto 0;">회원정보 수정하기</span>
      </div>
      <div style="border: solid 1px brown; height: 50px; cursor: pointer;" class="d-flex align-items-ceter justify-content-center mt-4"
      v-if="user?.id==now_user"
      @click="changeForms"
      >
        <span style="margin: auto 0;">비밀번호 변경하기</span>
      </div>
    </div>
  </div>
  <div class="col-1"></div>
  <div class="col-7 divBox"  style="height: 500px;">
    <div style="padding: 25px;border-bottom: solid snow 1px;">
      <h1>{{ user?.username }}님의 프로필</h1><br>
      <h2>{{ user?.One_liner }}</h2>
    </div>
    <div style="padding: 25px;">
      <h3>E-mail</h3>
      <h4 v-if="user?.email">{{ user?.email }}</h4>
      <h4 v-else class="mt-3 mb-5">이메일이 없습니다.</h4>
      <h4 class="mt-5">선호 장르 : <span v-for="(genre, i) in genreNames" :key="genre.id">{{ genre }}<span v-if="i<genreNames.length-1">, </span></span>
        <span v-if="!genreNames">아직 선택된 장르가 없어요!</span>
      </h4>
    </div>
  </div>
  <div style="border: solid 1px brown;" class=" mt-4 p-3"
  v-if="changeForm" >
  <form @submit.prevent="changePassword">
    <div>
      <span style="margin: auto 0;">새 비밀번호 : </span><input type="password" v-model="new_password1"><br>
    </div>
    <div class="mt-5">
      <span style="margin: auto 0;">한번 더 입력해주세요 : </span><input type="password" v-model="new_password2">
    </div>
    <div class="mt-4">
      <span v-if="new_password1 && new_password1!==new_password2">
        비밀번호가 일치하지않습니다!
      </span>
      <span v-else-if="new_password1 &&new_password1==new_password2">
        비밀번호가 일치합니다!
      </span>
    </div>
    <input type="submit" class="mt-5 me-3" @click="changePassword" value="변경하기">
    <button @click="changeForms">취소하기</button>
  </form>
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
      url : URL,
      now_user : this.$store.state.user?.id,
      genres : null,
      genreNames : [],
      changeForm : false,
      new_password1 : null,
      new_password2 : null,
      user_id : this.$route.params.id
    }
  },
  computed:{
    isFollowed(){
      for(let i of this.user?.followers){
        if(i.id == this.now_user){
          return true
        }
      }
      return false
    }
  },
  created(){
    this.getGenres()
    this.getUser()
  },
  watch: {
    '$route': {
      immediate: true,
      handler(to) {
        this.user_id = to.params.id;
        this.getUser();
      }
    }
  },

  mounted(){
  },
  methods:{
    getGenreNames(){
      const arr = []
      for(const i of this.user.like_genres){
        for(const j of this.genres){
          if(i==j.id){
            arr.push(j.name)
          }
        }
      }
      this.genreNames = arr
    },
    getUser(){
      axios({
        method:'post',
        url: `${URL}/api/v1/getuser/${this.user_id}/`,
        headers:{
          Authorization : `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.user = res.data
        this.getGenreNames()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getGenres(){
      axios({
        method : 'get',
        url : `${URL}/api/v1/genres/`
      })
      .then((res) => {
        this.genres = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goUpdate(){
      this.$router.push({name:'ProfileUpdate', params:{id:this.user_id}})
    },
    changeForms(){
      this.changeForm = !this.changeForm
    },
    changePassword(){
      const new_password1 = this.new_password1
      const new_password2 = this.new_password2
      axios({
        method : 'post',
        url : `${URL}/accounts/password/change/`,
        headers : {
          Authorization : `Token ${this.$store.state.token}`
        },
        data : { new_password1, new_password2 }
      })
      .then(() => {
        alert('변경되었습니다')
        this.changeForm = false
        location.reload()
      })
      .catch((err) => {
        alert('다시 시도해 주세요')
        console.log(err)
      })
    },
    onFollow(){
      axios({
        method:'patch',
        url: `${URL}/api/v1/${this.user_id}/follow/`,
        headers:{
          Authorization : `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.getUser()
        // console.log(this.isFollowed)
        // console.log(this.user)
        // console.log(this.now_user)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    }
  
}
</script>

<style>
#profile2{
  width: 200px;
  height: 200px;
  clip-path: circle(50%); /* 가로 길이를 반지름으로 사용 */
}
.divBox{
  /* background-color: rgb(122, 122, 122); */
  border: solid 2px rgb(197, 197, 197);
  padding: 30px;
}
.divBox p{
  text-align: center;
  line-height: 100%;
}
</style>