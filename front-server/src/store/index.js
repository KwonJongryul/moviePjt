import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from "../router"
import createPersistedState from 'vuex-persistedstate'
// import _ from 'lodash'
Vue.use(Vuex)

export default new Vuex.Store({
  plugins :[
    createPersistedState()
  ],
  state: {
    movies : [],
    token : null,
    reviews : null,
    user: null,
    redirectPath: '/',
  },
  getters: {
    islogin(state){
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state, movies){
      state.movies = movies
    },
    GET_GENREMOVIE(state, list){
      state.genre_movies = list
    },
    GET_REVIEWS(state, reviews){
      state.reviews = reviews
    },
    SAVE_TOKEN(state, key){
      state.token = key
      router.push({name:'HomeView'})
    },
    LOGOUT_TOKEN(state){
      state.token = null
    },
    SET_REDIRECT_PATH(state, path){
      state.redirectPath = path
      console.log(state.redirectPath)
    },
    GET_USER(state, user){
      state.user = user
    }
  },
  actions: {
    // 영화 목록 얻어오기
    getMovies(context){
      let URL = null
      // 로그인 됐을때
      if (context.getters.islogin){
        URL = `http://127.0.0.1:8000/api/v1/genremovies/`
      }else{ // 안됐을때
        URL = 'https://api.themoviedb.org/3/movie/now_playing?api_key=3c1824cd40b0044d7944ab5a55d4cb16&language=ko-KR&page=1'
      }
      axios({
        methods : 'get',
        url: URL
      })
      .then((res) => {
        const movies = res.data.results
        const genre_movies = []
        for(let i = 0; i < 11; i++){
          genre_movies.push(movies[i])
        }
        context.commit('GET_MOVIES', res.data)
        context.commit('GET_GENREMOVIE', genre_movies)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    login({commit, state}, payload){
      const username = payload.username
      const password = payload.password
      axios({
        method : 'post',
        url : 'http://127.0.0.1:8000/accounts/login/',
        data : {
          username, password
        },
      })
      .then((res) => {
        const key = res.data.key
        commit('SAVE_TOKEN', key)
        // 로그인전에 이동하려던 페이지로 이동
        if(state.redirectPath!='/'){
          router.push(state.redirectPath||'/')
          commit('SET_REDIRECT_PATH', '/')
        }
      })
      .then(()=> {
        this.dispatch('getUser')
      })
      .catch((err)=> {
        console.log(err)
        alert('로그인에 실패했습니다. 다시 시도해주세요')
      })
    },
    getUser({commit, state}){
      axios({
        method : 'get',
        url : 'http://127.0.0.1:8000/api/v1/getid/',
        headers : {
          Authorization : `Token ${ state.token }`
        }
      })
      .then((res) => {
        commit('GET_USER', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    signup(context, payload){
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      axios({
        method : 'post',
        url : 'http://127.0.0.1:8000/accounts/signup/',
        data : {
          username, password1, password2
        },
      })
      .then(() => {
        // console.log(res)
        // commit('SAVE_TOKEN', res.data.key)
        alert('정상적으로 회원가입되었습니다. 로그인해 주세요.')
        router.push({name:'HomeView'})
      })
      .catch((err) => {
        console.log(err)
        alert('이미 존재하는 아이디입니다')
      })
    },
    logout({commit}){
      axios({
        method: 'post',
        url : 'http://127.0.0.1:8000/accounts/logout/',
      })
      // 로그아웃만 하면 안되고 로컬스토리지에서 삭제해주고
      // save token으로 null값 저장해주기
      .then(()=>{
        localStorage.removeItem('authToken')
        commit('LOGOUT_TOKEN')
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getRivews(context){
      const URL = 'http://127.0.0.1:8000/api/v1/reviews/'
      axios({
        method : 'get',
        url : URL,
        headers : {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
          context.commit('GET_REVIEWS', res.data.reverse())
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  modules: {
  }
})
