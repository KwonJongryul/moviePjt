<template>
  <div class="back">
    <div class="container">
      <div>
        <h1>로그인</h1>
      </div>
      <div>
      <form @submit.prevent="login" class="form-holder">
        <!-- <label for="username">ID : </label> -->
        <input type="text" id="username" v-model="username" class="input" placeholder="ID를 입력해주세요"><br>
        <!-- <label for="password">PW : </label> -->
        <input type="password" id="password" v-model="password" class="input" placeholder="패스워드를 입력해주세요"><br>
        <input type="submit" value="로그인" class="submit-btn">
      </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data(){
    return {
      username : null,
      password : null,
    }
  },
  methods : {
    login(){
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }
      this.$store.dispatch('login', payload)
    }
  }
}
</script>

<style>    
  .back {
    /* background-image: url("../assets/theater.jpg"); */
    /* background-size: cover;
    background-color: rgba(0, 0, 0, 0.1); */
    
    /* background-repeat: no-repeat; */
    background-position: center;
    width : 2000px;
    height : 800px;
  }

  .back::after {
  content: "";
  position: absolute;
  opacity: 60%;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("../assets/theater.jpg");
  background-size: cover;
  background-position: center;
  filter: blur(3px); /* 원하는 흐림 효과 크기를 설정하세요 */
  z-index: -1;
}

  .container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    /* display: flex; */
    /* justify-content: center; */
    align-items: center;
    border-radius : 10px;
    background-color: white;
    opacity: 80%;
    color : black;
    width : 400px;
    height : 400px;
    text-align: center;
    padding: 50px;
  }

  .form-holder {
      border-radius: 15px;
      background-color: #fff;
      overflow: hidden;
      margin-top: 50px;
      opacity: 1;
      visibility: visible;
  }

  .input {
    border: 0;
    outline: none;
    box-shadow: none;
    display: block;
    height: 30px;
    line-height: 30px;
    padding: 8px 15px;
    border-bottom: 1px solid gray;
    width: 100%;
    font-size: 15px;
  }

  .input:focus {
    border-bottom-color: #ba1b10; /* 원하는 색상으로 수정하세요 */
  }

  .submit-btn {
      background-color: #ba1b10;
      color: white;
      border:0;
      border-radius: 15px;
      display: block;
      margin: 15px auto; 
      padding: 15px 45px;
      width: 100%;
      font-size: 20px;
    }
</style>