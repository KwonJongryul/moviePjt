import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
// import _ from 'lodash'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies : [],
    genre_movies : []
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state, movies){
      state.movies = movies
    },
    GET_GENREMOVIE(state, list){
      state.genre_movies = list
    }
  },
  actions: {
    getMovies({commit}){
      axios({
        methods : 'get',
        url: `http://127.0.0.1:8000/api/v1/movies/`
      })
      .then((res) => {
        const movies = res.data
        const genre_movies = []
        for(let i = 0; i < 3; i++){
          genre_movies.push(movies[i])
        }
        commit('GET_MOVIES', res.data)
        commit('GET_GENREMOVIE', genre_movies)
      })
      .catch((err) => {
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
        
      })
    }
  },
  modules: {
  }
})
