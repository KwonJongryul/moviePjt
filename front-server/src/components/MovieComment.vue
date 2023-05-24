<template>
  <div>
		<h1 class="mb-5">댓글</h1>
		<div class="mb-5" @click="onchangeForm" style="background-color: white; color: black; max-width: 720px; min-height: 60px; padding: 10px;">
			<form v-if="islogin" @submit.prevent="onCreate">
				<span v-if="!changeForm">
				댓글을 남겨주세요
				</span>
				<div v-else>
					<p><img :src="`${URL + user.user_img}`" alt="profile" width="50px" style="clip-path: circle(50% at center);" class="mx-2" id="profile">{{ user.username }}</p>
					<textarea style="width: 700px; height: 143px; resize: none; padding: 0; overflow: auto;" 
					placeholder="타인의 권리를 침해하거나 명예를 훼손하는 댓글은 운영원칙 및 관련 법률에 제재를 받을 수 있습니다."
					v-if="changeForm"
					v-model="inputComment"
					/>
					<input type="submit" value="등록하기">
				</div>
			</form>
		</div>
		<p class="mb-4">전체 댓글 {{ comments.length }}개</p>
		<div class="card mb-3 p-0 w-1000 comments"
		style="opacity: 0.8;"
		onmouseover="this.style.opacity='0.9';"
		onmouseout="this.style.opacity='0.8';"
		v-for="(comment, i) in comments.slice().reverse()"
		:key="i"
		>
		{{ comment }}
		</div>
  </div>
</template>

<script>
import axios from 'axios'
const URL = 'http://127.0.0.1:8000'
export default {
	name:'MovieComment',
	data(){
		return {
			// comments : this.movie.comments,
			changeForm : false,
			inputComment : null,
			URL : URL
		}
	},
	props:{
		movie : Object
	},
	computed : {
		islogin(){
			return this.$store.getters.islogin
		},
		comments(){
			return this.movie.comments
		},
		user(){
			return this.$store.state.user
		}
	},
	methods:{
		onchangeForm(){
			this.changeForm = true
		},
		onCreate(){
			if (!this.inputComment){
				alert('내용을 입력해 주세요')
				return
			}
			axios({
				method : 'post',
				url : `${URL}/api/v1/comment/`,
				headers:{
					Authorization : `Token ${this.$store.state.token}`
				},
				data : {
					context : this.inputComment,
					movie : this.movie.id
				}
			})
			.then(() =>  {
				alert('등록되었습니다')
				this.changeForm = false
				location.reload()
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
.comments{
	font-family: 'Hahmlet', serif;
	color : black;
	font-size: 23px;
}
</style>