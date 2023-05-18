import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
// import router from "@/router"
import createPersistedState from 'vuex-persistedstate'
// import _ from 'lodash'
Vue.use(Vuex)

export default new Vuex.Store({
  plugins :[
    createPersistedState()
  ],
  state: {
    movies : [],
    token : null
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
    SAVE_TOKEN(state, key){
      state.token = key
      // router.push({name:'HomeView'})
    }
  },
  actions: {
    getMovies(context){
      let URL = null
      if (context.getters){
        URL = `http://127.0.0.1:8000/api/v1/genremovies/`
      }else{
        URL = `http://127.0.0.1:8000/api/v1/latestmovies/`
      }
      axios({
        methods : 'get',
        url: URL
      })
      .then((res) => {
        const movies = res.data
        const genre_movies = []
        for(let i = 0; i < 3; i++){
          genre_movies.push(movies[i])
        }
        context.commit('GET_MOVIES', res.data)
        context.commit('GET_GENREMOVIE', genre_movies)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    login({commit}, payload){
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
        commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err)=> {
        console.log(err)
      })
    },
    signup({commit}, payload){
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
      .then((res) => {
        console.log(res)
        commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    logout({commit}){
      axios({
        method: 'post',
        url : 'http://127.0.0.1:8000/accounts/logout/',
      })
      .then(()=>{
        localStorage.removeItem('authToken')
        commit('SAVE_TOKEN', null)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})
