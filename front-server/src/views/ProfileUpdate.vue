<template>
  <div>
    <h1>회원정보 수정</h1>
    <form @submit.prevent="update" enctype="multipart/form-data">
      <div class="profile">
        <h2>프로필 사진</h2>
        <img :src="`${URL + profile.user_img}`" alt="이미지가 없어요 😢" id="profileImg" style="margin-top: 30px;margin-bottom: 30px;"><br>
        <input type="file" @change="onImg">
      </div>
      <div class="items">
        <span>소개글 : </span>
        <input type="text" v-model="profile.One_liner">
      </div>
      <div class="items">
        <span>Email : </span>
        <input type="email" v-model="profile.email">
      </div>
      <div class="items">
        <p>선호 장르를 선택해 주세요</p>
        <span v-for="(genre, i) in genres" :key="genre.id">
          <button 
          @click="pick_genre" 
          :value="genre.id" 
          :class="{ selectedButton: selecteds.includes(genre.name) }"
          type="button"
          >
            {{ genre.name }}
          </button>
          <br v-if="(i+1) % 5 ===0">
        </span>
      </div>
      <div class="items">
        <h4>선택된 장르 : 
          <span v-for="(selected, i) in selecteds" :key="selected">
            {{ selected }}
            <span v-if="i!=profile.like_genres.length-1">, </span>
          </span></h4>
        </div>
          <input type="submit" value="변경하기">
    </form>
  </div>
</template>
<script>
const URL = 'http://127.0.0.1:8000'
import axios from "axios"
export default {
  name: 'ProfileUpdate',
  data(){
    return {
      profile : this.$store.state.user,
      URL : URL,
      userImg : null,
      genres : null,
      // 사진 변화 감지 변수
      ischange : false
    }
  },
  computed:{
    selecteds(){
      const arr = []
      for(const i of this.profile.like_genres){
        for(const j of this.genres){
          if(i==j.id){
            arr.push(j.name)
            break
          }
        }
      }
      return arr
    }
  },
  created() {
    this.getGenres()
  },
  methods:{
    onImg(event){
      console.log(this.profile.user_img)
      this.profile.user_img = event.target.files[0]
      console.log(this.profile.user_img)
      this.ischange = true
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
    pick_genre(e){
      if(!this.profile.like_genres.includes(e.target.value) && this.profile.like_genres.length < 3){
        this.profile.like_genres.push(e.target.value)
      }else{
        this.profile.like_genres = this.profile.like_genres.filter((element) => element !== e.target.value)
      }
    },
    update(){
      console.log(this.profile)
      this.updateform()
    },
    updateform(){
      const user_img = this.profile.user_img
      const email = this.profile.email
      const One_liner = this.profile.One_liner
      const like_genres = this.profile.like_genres
      const formData = new FormData()
      if (this.ischange){
        formData.append('user_img', user_img)
      }
      formData.append('email', email)
      formData.append('One_liner', One_liner)
      formData.append('like_genres', like_genres)
      console.log(like_genres)
      // 이미지 저장, url받고 폼 업데이트
      axios({
        method : 'patch',
        url : `${URL}/api/v1/getuser/${this.profile.id}/`,
        headers:{
          Authorization : `Token ${this.$store.state.token}`,
        },
        data : formData
      })
      .then(() => {
        alert('저장되었습니다')
        this.$router.push({name:'ProfileView', params:{id:this.profile.id}})
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
#profileImg{
  width: 200px;
  height: 200px;
  clip-path: circle(50%); /* 가로 길이를 반지름으로 사용 */
}
.selectedButton{
  background-color: bisque;
}
.items{
  margin-bottom: 30px;
}
</style>