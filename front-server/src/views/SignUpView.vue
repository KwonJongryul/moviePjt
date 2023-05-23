<template>
  <div class="back">
    <div class="container">
    <h1>회원가입</h1>
    <form @submit.prevent="signup" class="form-holder">
      <!-- <label for="username">ID : </label> -->
      <input type="text" id="username" v-model="username" class="input" placeholder="ID를 입력해주세요"><br>
      <!-- <label for="password1">password1 : </label> -->
      <input type="password" id="password1" v-model="password1" class="input" placeholder="패스워드를 입력해주세요"><br>
      <!-- <label for="password2">password2 : </label> -->
      <input type="password" id="password2" v-model="password2" class="input" placeholder="패스워드를 한 번 더 입력해주세요"><br>
      <span>{{ message }}</span>
      <input type="submit" value="가입하기" class="submit-btn">
    </form>
    </div>
  </div>
</template>

<script>
export default {
  name:'SignUpView',
  data(){
    return {
      username : null,
      password1 : null,
      password2 : null,
      
    }
  },
  computed:{ 
    message(){
      if (!this.password1){
        return ''
      }
      else if (this.password1 === this.password2 && this.password1){
        return '패스워드가 일치합니다.'
      }
      return '패스워드가 일치하지 않습니다.'
    }
  },
  methods: {
    signup(){
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      if(password1 != password2){
        alert('패스워드가 일치하지 않습니다.')
        this.password1 = ''
        this.password2 = ''
        return
      }
      const payload = {
        username, password1, password2
      }
      this.$store.dispatch('signup', payload)
    }
  }
}
</script>

<style>
  .container {
    margin-top: 30px;
  }
</style>