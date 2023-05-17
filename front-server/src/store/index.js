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
      console.log(movies, 'sksk') 
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
        console.log(genre_movies, '왜안나옴????????????')
        commit('GET_MOVIES', res.data)
        commit('GET_GENREMOVIE', genre_movies)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getGenremovie(){
      // console.log(movies, 'dkdkdkdkdk') 
    }
  },
  modules: {
  }
})
