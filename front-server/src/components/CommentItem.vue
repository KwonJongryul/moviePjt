<template>
  <div>
    <div class="card mb-3 p-0 comment pb-3">
      <div class="d-flex justify-content-between p-4">
        <span>{{ comment?.created_at.slice(0,10) }}</span>
        <span style="cursor: pointer;" @click="goProfile"><img :src="`${url + user_img}`" alt="profile" width="50px" style="clip-path: circle(50% at center);" class="mx-2" id="profile">{{ comment?.username }}</span>
      </div>
      <div class="px-4 py-2" v-if="isUpdate">
        <textarea cols="30" rows="10" style="resize: none;" v-model="comment.context"></textarea><br>
        <button @click="onUpdate">수정하기</button>
      </div>
      <div class="d-flex justify-content-between px-4 py-2" v-if="!isUpdate">
        <span>{{ comment?.context }}</span>
      </div>
      <div class="d-flex justify-content-between px-4 py-2">
        <div id="like_comment" class="mt-4 d-flex align-items-center">
          <span style="cursor: pointer;" @click="onlike">
            <img src="../assets/like_button2.png" alt="like" v-if="is_liked" width="30px">
            <img src="../assets/like_button.png" alt="like" v-else width="30px">
            <span :class="{'liked_comment' : is_liked}" style="vertical-align: bottom;">&nbsp; {{ comment?.like_users?.length }}</span>
          </span>
        </div>
        <div class="dropdown-center">
          <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            <i class="fas fa-ellipsis-v fa-2x"></i>
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item CommentUpdate" @click="changeReply">답글달기&nbsp;&nbsp;<i class="fa fa-reply"></i></a></li>
            <li><a class="dropdown-item CommentUpdate" @click="changeUpdate" v-if="now_user?.id==comment?.user">수정하기&nbsp;&nbsp;<i class="fa fa-pen-square"></i></a></li>
            <li><a class="dropdown-item CommentDelete" @click="onDelete" v-if="now_user?.id==comment?.user">삭제하기&nbsp; <i class="far fa-trash-alt"></i></a></li>
          </ul>
        </div>
      </div>
      <hr style="width: 85%; margin-left: auto; margin-right: 80px;" v-if="isReply || comment.recomments">
      <div v-if="isReply">
        <div class="row mt-3">
          <div class="d-flex col-2 justify-content-center">
            <img :src="`${url + now_user?.user_img}`" alt="profile" width="50px" style="clip-path: circle(50% at center);" class="ms-5" id="profile">
          </div>
          <div class="col-10">
            <textarea cols="30" rows="5" style="resize: none;" v-model="inputRecomment"></textarea><br>
            <button style="margin-left: 570px;" @click="onRecomment">등록</button>
            <button class="ms-2" @click="changeReply">취소</button>
          </div>
        </div>
      </div>
      <RecommentItem
      v-for="recomment in comment.recomments"
      :key="recomment.id"
      :recomment_id="recomment.id"
      @deleted="get_comment"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios"
import RecommentItem from '@/components/RecommentItem'
const URL = 'http://127.0.0.1:8000'
export default {
  name : 'CommentItem',
  components:{
    RecommentItem
  },
  data(){
    return {
      now_user : this.$store.state.user,
      comment : null,
      user_img : null,
      url : URL,
      isUpdate : false,
      isReply : false,
      inputRecomment : null
    }
  },
  computed:{
    is_liked(){
      if(this.comment?.like_users?.includes(this.now_user.id)){
        return true
      }
      return false
    }
  },
  created(){
    this.get_comment()
  },
  props:{
    comment_id : Number,
  },
  methods:{
    // 코멘트 로드------
    get_comment(){
      axios({
        method : 'get',
        url : `${URL}/api/v1/comment/${this.comment_id}`
      })
      .then((res) => {
        this.comment = res.data
        this.getUserImg()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 좋아요----------
    onlike(){
      axios({
        method : 'post',
        url : `${URL}/api/v1/comment/like/${this.comment_id}/`,
        headers:{
          Authorization : `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          // 좋아요 한 뒤 정보를 다시 가져와 좋아요 수가 화면에
          // 반영되게 함
          this.get_comment()
        })
        .catch((err) =>  {
          console.log(err)
        })
    },
    // 유저이미지--------------
    getUserImg(){
      axios({
        method:'post',
        url: `${URL}/api/v1/getuser/${this.comment.user}/`,
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
    // 프로필로 이동-------
    goProfile(){
      this.$router.push({name:'ProfileView', params : {id:this.comment?.user}})
    },
    // 업데이트 폼 보여주기-------
    changeUpdate(){
      this.isUpdate = true
    },
    // 업데이트 하기--------
    onUpdate(){
      axios({
        method : 'put',
        url : `${URL}/api/v1/comment/${this.comment_id}`,
        data : this.comment
      })
      .then(() => {
        alert('수정되었습니다')
        this.isUpdate = false
      })
      .catch((err) => {
        console.log(err)
        alert('취소되었습니다.')
      })
    },
    // 삭제---------
    onDelete(){
      axios({
        method : 'delete',
        url : `${URL}/api/v1/comment/${this.comment_id}`,
        data : this.comment
      })
      .then(() => {
        alert('삭제되었습니다')
        this.isUpdate = false
        location.reload()
      })
      .catch((err) => {
        console.log(err)
        alert('실패하였습니다.')
      })
    },
    // 리플폼 on off
    changeReply(){
      this.isReply = !this.isReply
    },
    // 대댓글 달기
    onRecomment(){
			if (!this.inputRecomment){
				alert('내용을 입력해 주세요')
				return
			}
			axios({
				method : 'post',
				url : `${URL}/api/v1/recomment/`,
				headers:{
					Authorization : `Token ${this.$store.state.token}`
				},
				data : {
          context : this.inputRecomment,
					comment : this.comment.id
				}
			})
			.then(() =>  {
				alert('등록되었습니다')
				this.isReply = false
        this.get_comment()
        this.inputRecomment = null
        console.log(this.comment)
			})
			.catch((err)  => {
				console.log(err)
				alert('다시 시도해 주세요')
			})
    }
  }
}
</script>

<style>
  .comment{
    width: 1000px;
    color: black;
    background-color: rgb(196, 196, 196);
  }
  .liked_comment{
    color: blue;
  }
  .CommentDelete{
    color: rgb(204, 25, 25);
  }
  /* 드롭다운 기본아이콘 없애는 css */
  .dropdown-toggle::after {
    display: none !important;
  }
  .dropdown-item{
    cursor: pointer;
  }
</style>