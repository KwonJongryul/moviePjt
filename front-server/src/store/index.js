import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies : [],
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state, movies){
      state.movies = movies
      console.log(movies)
    }
  },
  actions: {
    getMovies({commit}){
      axios({
        methods : 'get',
        url: `http://127.0.0.1:8000/api/v1/movies/`
      })
        .then((res) => {
          commit('GET_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err, 'gdgd')
        })
    }
  },
  modules: {
  }
})
